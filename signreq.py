# -*- coding: UTF-8 -*-

import json
import requests
from sdk.util import UUIDUtil, DateUtil
from sdk.auth import md5_tool, signature_composer, sha_hmac256
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse




def signreq(data,aurl, appKey, appSecret, request_method):   
    if not isinstance(data, dict):
        data = json.loads(data)
    print(20*'-') 

    
    u = urlparse(aurl)
    host = u.scheme + '://' + u.netloc
    url = u.path 
    if u.query:
        url = u.path + '?' + u.query
    print(url)
    timestamp =  DateUtil.get_timestamp()
    Datet = DateUtil.get_rfc_2616_date() 
 
    accept = '*/*' 
    xcanonce = UUIDUtil.get_uuid()
    contentmd5 = md5_tool.get_md5_base64_str(data)

    
    str_to_sign = ''

    if request_method == "POST":
        headers = {
        'Content-MD5': contentmd5, 
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN',
        #'Content-Length':'',  =
        'Content-Type': 'application/json',
        "Accept": '*/*',
        "Date": Datet
        }

        
    if request_method == "GET":
        headers = { 
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN',
        #'Content-Length':'',
        'Content-Type': 'application/json',
        "Accept": '*/*',
        "Date": Datet
        }

    headers['x-ca-signaturemethod'] = 'HmacSHA356'
    headers['x-ca-nonce'] = xcanonce
    headers['x-ca-key']= appKey
    headers['X-ca-stage']= 'RELEASE'
    str_to_sign = signature_composer.build_sign_str(uri=url, method=request_method,
     
                                                           headers=headers)

    #print(str_to_sign)
    xcasignature = sha_hmac256.sign(str_to_sign, appSecret)
    headers['X-Ca-Signature'] = xcasignature
    headers['X-Ca-Signature-headers'] = "x-ca-key,x-ca-nonce,x-ca-signaturemethod"
    

    tstr_to_sign = str_to_sign.replace('\n','#',100)

    #print(100*'-'+ tstr_to_sign + 100*'-')

    headers['x-ca-signature'] = xcasignature
 
    #print(headers)
    print(20*'-')
    return (headers,data)


if __name__ == '__main__':
    data = {"xx": "xx"}
    url = 'https://api.xx.xxx.cn/tier/get'
    head = signreq(data,url)
    r = requests.post(url, data=json.dumps(data), headers=head, verify=False)
    print(r.headers, r.text)

 
