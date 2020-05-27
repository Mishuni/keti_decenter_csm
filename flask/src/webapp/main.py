# web (application)
from flask import Flask,render_template,jsonify,request
# from .logic import process_list, connectDB
from . import config
from random import randint,random

import datetime,time
import pytz

utc=pytz.UTC
app = Flask(__name__)
listA = []
listB = []
limit = config.RESULT_CONFIG['limit']
threshold = config.RESULT_CONFIG['threshold']

def countMaxConf(groupList,standard):
    maxCon = 0
    result = "False"

    for i in range(len(groupList)-1,-1,-1):
        if(groupList[i]["timeStamp"]>=standard):
            print("============TIME=============")
            print(groupList[i]["groupName"],groupList[i]["timeStamp"])
            print("==============================")
            if(groupList[i]["confidence"]>maxCon):
                maxCon = groupList[i]["confidence"]
                result = groupList[i]["result"]
            else:
                break
    
    return result,maxCon


@app.route('/')
def hello(): 
    return render_template('index.html')

@app.route('/list')
def getList():
    return str(len(listA))

# GET method
@app.route('/calculate')
def countServer():
    global listA
    global listB
    #standard = datetime.datetime.strptime("2020-05-25 10:31:41",'%Y-%m-%d %H:%M:%S')- datetime.timedelta(seconds = 1)
    standard = datetime.datetime.now(datetime.timezone.utc)- datetime.timedelta(seconds = 2)
    start = time.time()
    resultA, maxA = countMaxConf(listA,standard)
    resultB, maxB = countMaxConf(listB,standard)
    listA.clear()
    listB.clear()

    print("===============RESULT================")
    print("time :", (time.time() - start) * 1000,"ms") 
    print("NOW:",standard)
    print("maxA:",resultA,maxA)
    print("maxB:",resultB,maxB)
    print("=====================================")
    
    if(resultA=="True" and maxA > threshold and resultB=="True" and maxB > threshold):
        if(maxA>=maxB): return "A"
        return "B"
    elif(resultA=="True" and maxA > threshold ):
        return "A"
    elif(resultB=="True" and maxB > threshold ):
        return "B"
    return "NA"

# collect result of A,B
@app.route('/result', methods=['POST'])
def getResult():
    global listA
    global listB
    if(len(listA)>200 or len(listB)>200):
        listA.clear()
        listB.clear()
    # {"confidence":0.92,"groupName":"A","result":True,"timeStamp":"2020-05-25 10:31:41"}
    res = request.get_json()
    date = datetime.datetime.strptime(res["timeStamp"],'%Y-%m-%d %H:%M:%S')
    date = date.replace(tzinfo=utc)
    res["timeStamp"]=date
    if(res["groupName"]=="A"):
        listA.append(res)
    elif(res["groupName"]=="B"):
        listB.append(res)
    return res

    
#app.run()
