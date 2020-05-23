import requests
import json

if __name__ == '__main__':
    data = {
    "idCardNumber": "6275980334017200691"
    }
    url = 'https://api.family.xxx.cn/tier/get'
    #head = signreq(data,url)
    head = {}
    r = requests.post(url, data=json.dumps(data), headers=head, verify=False)
    print(r.headers, r.text)

 