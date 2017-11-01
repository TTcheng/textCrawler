# 文本爬虫 抓取jikexueyuan.com/course的课程封面

import re
import requests

# 读取文件
f = open("text_src.html",'r')
html = f.read()
f.close()

# 匹配图片网址
pic_urls = re.findall('img src="(.*?)"',html,re.S)
i= 0
for url in pic_urls:
    if url.__contains__("png"): # 出去png结尾的
        continue
    print('now downloading '+url)
    pic = requests.get(url)
    fp = open('pic\\'+str(i)+'.png','wb')
    fp.write(pic.content)
    fp.close()
    i += 1

