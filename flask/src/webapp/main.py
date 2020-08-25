# web (application)
from flask import Flask,render_template,jsonify,request
# from .logic import process_list, connectDB
#from . import config
import config
from random import randint,random

import datetime,time, pytz, copy
import json
import logging

# 로그 생성
logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()

utc=pytz.UTC
app = Flask(__name__)
app.config['SECRET_KEY'] = 'seceret'
listA = []
limit = config.RESULT_CONFIG['limit']
threshold = config.RESULT_CONFIG['threshold']

def countMaxConf(groupList,standard):
    groupList_copy = copy.deepcopy(groupList)
    maxA = 0
    resultA = "False"
    maxB = 0
    resultB = "False"

    for i in range(len(groupList_copy)-1,-1,-1):
        if(groupList_copy[i]["timeStamp"]>=standard):
            
            if(groupList_copy[i]["result"]=="False"):
                # print("Reverse",groupList_copy[i]["confidence"])
                groupList_copy[i]["confidence"]=1-groupList_copy[i]["confidence"]
            # print("============TIME CONF=============")
            # print(groupList_copy[i]["groupName"],groupList_copy[i]["result"],groupList_copy[i]["timeStamp"],groupList_copy[i]["confidence"])
            # print("==============================")
            if(groupList_copy[i]['groupName']=="A" and groupList_copy[i]["confidence"]>maxA):
                maxA = groupList_copy[i]["confidence"]
                resultA = groupList_copy[i]["result"]
            elif(groupList_copy[i]['groupName']=="B" and groupList_copy[i]["confidence"]>maxB):
                maxB = groupList_copy[i]["confidence"]
                resultB = groupList_copy[i]["result"]
            
        else:
            break
    
    return resultA,maxA,resultB,maxB


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
    #standard = datetime.datetime.strptime("2020-05-25 10:31:41",'%Y-%m-%d %H:%M:%S')- datetime.timedelta(seconds = 1)
    # start = time.time()
    standard = datetime.datetime.now(datetime.timezone.utc)- datetime.timedelta(seconds = 2)
    resultA, maxA, resultB, maxB = countMaxConf(listA,standard)
    #resultB, maxB = countMaxConf(listB,standard)

    # print("===============RESULT================")
    # print("time :", (time.time() - start) * 1000,"ms") 
    # print("NOW:",standard)
    # print("maxA:",resultA,maxA)
    # print("maxB:",resultB,maxB)
    # print("=====================================")
    
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
    if(len(listA)>200):

        listA.clear()

    res = request.get_json()
    if(res==None):
        res = str(request.get_data())
        res = res[2:-1].replace("'",'"')
        res = json.loads(res)
    res["confidence"]=float(res["confidence"])
    date = datetime.datetime.strptime(res["timeStamp"],'%Y-%m-%d %H:%M:%S')
    date = date.replace(tzinfo=utc)
    res["timeStamp"]=date
    listA.append(res)

    return res
if __name__ == '__main__':  
    app.run(host="0.0.0.0",port=5000, debug=True)
