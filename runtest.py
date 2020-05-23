import requests
import json

if __name__ == '__main__':
    data = {
    "xx": "xx"
    }
    url = 'https://api.xx.xxx.cn/tier/get'
    #head = signreq(data,url)
    head = {}
    r = requests.post(url, data=json.dumps(data), headers=head, verify=False)
    print(r.headers, r.text)

 
