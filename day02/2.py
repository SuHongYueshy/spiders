import requests
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}


with open("cookie.txt","r",encoding="UTF-8") as f:
    cookies_str=f.readline()

#将cookies字符串转换为字典型
cookie_list = cookies_str.split(";")
cookie_dict={}
for cookie in cookie_list:
    key=cookie.split("=")[0].replace(" ","")
    value=cookie.split("=")[1]
    cookie_dict[key] = value

html=requests.get("https://www.douban.com/people/168443006/notes",headers=header,cookies=cookie_dict)
print(html.text)



