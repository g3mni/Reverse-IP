# Reverse-IP
## 0.前言
18年有批量的需求，时间紧又没有接口的资源，用爬虫做了一个代查询，现学现卖
## 1.实现功能
逐行将IP.txt（文件中每行一个IP）中的IP通过某网站反查域名，将结果输出
## 2.运行环境
python2.7  
xlwt
## 3.运行方式
````
python ReverseIP.py
````
## 4.文件描述
ReverseIP.py主体脚本  
## 5.后续完善计划
- [ ] 增加用户输入，-help功能
- [ ] 文件名由用户指定或根据时间，有区分
- [ ] 正对多维数组处理
## 6.遇到的问题
1.接口网站不稳定，time.sleep解决  
2.xls的循环写入  
````python
  for i,row in enumerate(items):
    booksheet.write(a+1,1,row)
    booksheet.write(a+1,0,addr)
    a +=1
````
3.表头的写入  
