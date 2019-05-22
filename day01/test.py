import re

str1 ='18731313511'
phone = re.findall('13[0-9]{9}',str1)
print(phone)

# 贪心算法，
str2 = '232xxfdlgidddxxww222jxxfsdjlkxxdsjlk88xxjfeiedeffeedxxee'
# phone = re.findall('xx.*xx',str2)   把xx中间的东西展示出来
# phone = re.findall('xx(.*)xx',str2)   加了括号，匹配的条件结果没有两边的xx
phone = re.findall('xx.(.*?)xx',str2)
print(phone)
