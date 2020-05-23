import urllib.request, urllib.parse, urllib.error
import sys


def percent_encode(encode_str):
    encode_str = str(encode_str)
    if sys.stdin.encoding is None:
        res = urllib.parse.quote(encode_str.decode('cp936').encode('utf8'), '')
    else:
        res = urllib.parse.quote(encode_str.decode(sys.stdin.encoding).encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res
