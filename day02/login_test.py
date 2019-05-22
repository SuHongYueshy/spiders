import urllib.request
import http.cookiejar
from lxml import etree

# from spiderImg import getImg

head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


def makeMyOpener(head):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
    opener.addheaders = header
    return opener


oper = makeMyOpener(head)
uop = oper.open('https://accounts.douban.com/login', timeout=1000)
data = uop.read()
html = data.decode()
spath = './doubanLogin.html'
f = open(spath, "w", encoding='utf-8')
f.write(html)
f.close()
print(html)