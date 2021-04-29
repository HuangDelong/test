import urllib.request,urllib.error

#获取一个get请求
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码
# import urllib.parse
# #获取一个post请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")
# response = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
# print(response.getheader("Server"))

# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
#     }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
import urllib.parse
url = "https://www.douban.com"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))