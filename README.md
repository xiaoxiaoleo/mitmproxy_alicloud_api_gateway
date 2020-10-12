# mitmproxy_alicloud_api_gateway

Use mitmproxy tamper http request, add signature header to make test autmate.

测试阿里API网关时候需要给每个包计算一个完整性签名头，可通过mitmproxy来自动化完成签名头添加操作。

使用方式：
1. 启动MITM监听8080端口：
> mitmweb -v  -s mitm.py  
2. 跑个sqlmap：
> proxychains sqlmap -u  https://xxx.cn/xx/xx/xx--data \{\"xxx\":\"xx\",\"xx\":\"xx*\"\}  --ignore-code=400  -v 7


More info:
https://www.cnblogs.com/xiaoxiaoleo/p/12945042.html
