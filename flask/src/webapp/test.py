
import requests, json
import random
import time
import datetime
import datetime as pydatetime
def get_now():
    return pydatetime.datetime.now()

def get_now_timestamp():
    return get_now().timestamp()

## application/json 으로 보내기
url = "http://localhost:9000"+"/result"

## data example
# {"confidence":0.92,"groupName":"A","result":True,"timeStamp":"2020-05-25 10:31:41"}

group = ["A","B"]
#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
while(True):
    ran = random.randrange(2)
    f = random.uniform(0.8, 1) 
    today = get_now_timestamp()
    #print(today)
    t = random.uniform(0.8,0.9) 
    data = {"confidence":str(f),"groupName":group[ran],"result":"True","timeStamp":today,"processingTime":str(t)}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    
    r = requests.post(url, data = str(data))
    print(r.text)
    time.sleep(0.01)