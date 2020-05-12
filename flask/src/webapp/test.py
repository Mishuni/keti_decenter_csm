
import requests, json

## application/json 으로 보내기
url = "http://127.0.0.1:5005"+"/result"
data = {'groupName':'B', 'confidence':0.9}
headers = {'Content-Type': 'application/json; charset=utf-8'}
r = requests.post(url, data = json.dumps(data), headers=headers)    
print(r.text)


## 그냥 몸체 통으로 보내기
url = "http://127.0.0.1:5005"+"/result"
data = {'groupName':'A', 'confidence':0.9}
#headers = {'Content-Type': 'application/json; charset=utf-8'}
r = requests.post(url, data = data) #headers=headers)    
print(r.text)