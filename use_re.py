import re

f = open('web_page.html','r')
html = f.read()
f.close()

# 爬取标题
title = re.search('<title>(.*?)</title>',html,re.S).group(1)
print(title)

# 爬取链接
links = re.findall('href="(.*?)"',html,re.S)
for each in links:
    print(each)

# 抓取部分文字
# 先抓大
text_field = re.findall('<ul>(.*?)</ul>',html,re.S)[0]
# 再抓小
the_text = re.findall('">(.*?)</a>',text_field,re.S)

for every_text in the_text:
    print(every_text)


# sub实现翻页
root_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

for i in range(2,total_page+1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,root_url,re.S) # pageNum=%d替换pageNum=\d+
    print(new_link)