import urllib
import urllib2
import re
import json
import xlwt
import time

workbook = xlwt.Workbook(encoding='utf-8')  #新建一个Excel
booksheet = workbook.add_sheet('IP反查域名结果', cell_overwrite_ok=True) #创建sheet
title = ['IP','域名'] #提前定义表头
a = 0
i = 0
for i,row in enumerate(title,start=i):#循环读取并写入表头
    booksheet.write(0,i,row)
    i +=1
fp = open('IP.txt')
for ip in fp.readlines():
    addr = ip.strip()#根据情况linux \r\n win \n或者直接空，删除默认空白符号
    url = "https://dns.aizhan.com/"+str(addr)+"/" 
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        time.sleep(0.3) #avoid 429
        content = response.read().decode('utf-8')
        pattern = re.compile('<td class="domain">.*?<a href=".*?" rel="nofollow" target="_blank">(.*?)</a>',re.S)
        items = re.findall(pattern,content) 
        for i,row in enumerate(items):
            booksheet.write(a+1,1,row)
            booksheet.write(a+1,0,addr)
            a +=1
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
fp.close() #close the file
workbook.save('result.xls')  #保存Excel名称
