import requests
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

#Session对象，模拟服务器端的Session
session = requests.Session()

url = "https://accounts.douban.com/j/mobile/login/basic"#提交表单的URL
data={
    "ck":"",
    "name":"13776097761",
    "password":"zhangtao",
    "remember":"true",
    "ticket":""
}
result = session.post(url,data=data,headers=header)
result =result.json()#转换为python的字典格式
#登陆成功
html = session.get("https://www.douban.com/people/168443006/notes",headers=header)
print(html.text)






