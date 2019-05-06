import requests
from lxml import etree

url="https://www.qiushibaike.com/"

h1={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"
}
req=requests.get(url,headers=h1).text

a1=etree.HTML(req)

print(req)
'''
<a class="recmd-content" href="/article/121193018" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">昨天在开车遇到一个开摩托车的高手，路上狂飙超了一路的
车，还带着的dj，低音很深沉。后来过天桥的时候看到他了，他的摩托在压在别人车底，自己在路边抱
着腿呻吟。</a>

'''

b1=a1.xpath("//div//a//@href=")

print(b1)