"""
./mitmproxy --listen-host 0.0.0.0 --listen-port    -s mitm.py



"""
import json
from signreq import signreq
from mitmproxy import ctx

def request(flow):
    # 获取
    req= flow.request
    #print(req.headers)
    #print(dir(req))
    print(flow.request.pretty_url)
    url = flow.request.pretty_url
    body  = req.content.decode('UTF-8')
    data = json.loads(body)
    print(url)
    print(data)
    new_headers = signreq(data,url)
    #print(new_headers)
    for k,v in new_headers.items():
      req.headers[k] = v 


def response(flow):
    response = flow.response 
    print(response.text)
    ctx.log.info(str(response.status_code))