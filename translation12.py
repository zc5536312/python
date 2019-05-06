from urllib import request 
import urllib
import re
import os     

var=1
while (var== 1):
    key = input("输入内容：")
    if key=="exit":
        var =0
    if key=="clr":
        os.system('cls')
        continue 
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    h1= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

    data1={
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15541995020902",
    "sign": "babe75d1fb4356be51422177ad87e82c",
    "ts": "1554199502090",
    "bv": "66745c2bd404c2f62490e4e8dadb4b0e",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
    "typoResult": "false"
    }


    data1=urllib.parse.urlencode(data1).encode(encoding='utf-8')
    try:
        req=request.Request(url,data=data1,headers=h1)

        res=request.urlopen(req).read().decode()
        pat=r'"tgt":"(.*?)"}]]'
        result=re.findall(pat,res)
        print("翻译结果   "+result[0])
        print("")

    except Exception as e:
        print(e)


