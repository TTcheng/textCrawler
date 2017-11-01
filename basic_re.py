
# 正则表达式
import re

secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

# .的使用举例 匹配任意字符一次(\n除外)
# a = 'xy123'
# b = re.findall('x..',a)
# print(b)

# *的使用举例 匹配前一个字符0次 或者无限次
# a = 'xyxy123'
# b = re.findall('x*',a)
# print(b)

# ?的使用举例 匹配前一个字符0次 或1次
# a = 'xy123'
# b = re.findall('x?',a)
# print(b)

# .*的使用举例 贪心算法，尽可能多得匹配
b = re.findall('xx.*xx',secret_code)
print(b)

# .*?的使用举例  “少量多餐”式得匹配
c = re.findall('xx.*?xx',secret_code)
print(c)

# ()得使用举例  只返回括号内数据
d = re.findall('xx(.*?)xx',secret_code)
print(d)
print(d.__len__())
decoded_msg = ''

for each in d:
    decoded_msg += each
    if each is d[2]:
        decoded_msg += '.'
    else:decoded_msg += ' '
print(decoded_msg)