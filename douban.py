from bs4 import BeautifulSoup   #网页解析，获取数据
import re    #正则表达式，进行文字匹配
import urllib.request,urllib.error   #指定URL，获取网页数据
import xlwt  #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\douban_Top250.xls"
    saveData(savepath)
    askURL("https://movie.douban.com/top250?start=")
    print(datalist)

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
    #2.逐一解析数据
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的服务器，浏览器
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

 #3.保存数据
def saveData(savepath):
#      print("save....")
    print("save...")
if __name__ == "__main__":
    main()