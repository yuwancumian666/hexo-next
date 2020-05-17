---
layout: post
title: Python 自动登陆 WiFi 和 拨号
date: 2018-01-24 00:00:00 +0300
categories:
- Python
tags: [Python, 网络编程] # add tag
---


{% blockquote 泰戈尔, 飞鸟集 %}
The mighty desert is burning for the love of a blade of grass who shakes her head and laughs and flies away. 
    广袤无垠的沙漠热烈地追求着一叶绿草的爱，但她摇摇头，笑起来，飞了开去。
{% endblockquote %}

<!-- more -->
    
## 登陆 WiFi

用 Python 自动登陆WiFi的原理是利用 Requests 发送一个http请求，并得到相应的回复，以完成登陆 WiFi 的目的。
我们学校用的是深澜的校园网认证系统。

### 获取请求头

获取请求头最好的办法是在登陆页面查看 Headers：F12 打开开发者工具，选择 Network 选项，但是现在该选项是空的，刷新一次即可看到所有网络请求。

Name 一栏，点击当前主页，选中 Headers，在 Request Headers 里即可看到你打开该页面时浏览器向服务器发送的所有请求。

### 获取 data

要知道你点击登陆时浏览器发送了那些数据(当然是有用户名和密码的)，就要点击登陆进行测试。该测试最好在断开 WiFi 的情况下进行。
登陆页面上点击登陆或注销，在 Network-Name 一栏里就会出现相应的数据报，点击查看 Form Data 并记录，即完成信息的收集

*注意：*登陆时的密码是已经加密了的，仔细观察 network-Name 栏会发现如 base64.js （或MD5）的js文件，说明密码的加密是用的 base64 加密，这样子如果想自己加密密码的话可以导入 base64 的包自行加密。当然也可以直接写入 Form Data 的加密过了的密码。

### 代码

*注意：*代码为美观已把制表符 ('\t') 全部替换为四个空格

``` python
#! python2
#encoding: utf-8

import os
import requests as Req

class conn(object):
    def __init__(self):
        self.post_url = "http://10.10.8.2:801/srun_portal_pc.php?ac_id=3&"
        self.username = # 这里填写用户名
        self.password = # 这里填写密码
        self.login_headers = {
            'Host': '10.10.8.2:801',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;\
                q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://10.10.8.2/index_3.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYylaKZYk0c%\
                252Fq867bbRsRHvJQZaJnkCcFccbII9J6frGj6wJSCrpp%252Blg9n1pbnr4\
                ywa7fTlPvrkdU62P6Evm5v0udhgtIcVXLjCUfu9%252BDEmyZUVldnmfPop6\
                1pjVIRxZ5KLhArGI9tCOvJNxdTMmLCBU%252Fwukw%252BuvtiKv9J9RYUVP\
                5nAPFqLBoHp12OtUq3dRN%252FIAxfnHsqNeIsQ%253D%253D'
            }
        self.login_data = {
            'action': 'login',
            'username': self.username,
            'password': ,# 这里填写加密了的密码，通常是 "{B}"+base64.b64.encode(password)
            'ac_id': '3',
            'save_me': '1',
            'ajax': '1'
            }
        self.logout_headers = {
            'Host': '10.10.8.2:801',
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '57',
            'Accept': '*/*',
            'Origin': 'http://10.10.8.2:803',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://10.10.8.2:803/srun_portal_pc.php?ac_id=3&',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYylaKZYk0c%\
                252Fq867bbRsRHvJQZaJnkCcFccbII9J6frGj6wJSCrpp%252Blg9n1pbnr4\
                ywa7fTlPvrkdU62P6Evm5v0udhgtIcVXLjCUfu9%252BDEmyZUVldnmfPop6\
                1pjVIRxZ5KLhArGI9tCOvJNxdTMmLCBU%252Fwukw%252BuvtiKv9J9RYUVP\
                5nAPFqLBoHp12OtUq3dRN%252FIAxfnHsqNeIsQ%253D%253D',
            }
        self.logout_data = {
            'action': 'logout',
            'username': self.username,
            'password': self.password,
            'ajax': '1'
            }
    
    def wifi_connect(self):
        response = Req.post(url=self.post_url, data=self.login_data, headers=self.login_headers)
        print ("状态码: ", response.status_code)
        print ("响应头: ", response.headers)
        print ("响应内容", response.text.encode('UTF-8'))
        os.system('pause')

    def wifi_disconn(self):
        response = Req.post(url=self.post_url, data=self.logout_data, headers=self.logout_headers)
        print ("状态码: ", response.status_code)
        print ("响应头: ", response.headers)
        print ("响应内容", response.text.encode('UTF-8'))
        os.system('pause')

def main():
    connect = conn()
    detect = os.system('ping baidu.com -n 1')
    if detect:
        connect.wifi_connect()
    else:
        connect.wifi_disconn()

if __name__ == '__main__':
    main()
    
``` 

## 自动拨号

Windows 下自动拨号比较简单，就是利用 os 库模拟 cmd 命令，没有技术含量。但是值得注意的是，在我的电脑上，命令行执行没有问题，但是放到脚本里会报错。

"你没有连接到 xxx。<br>
命令已完成。"

``` python
#coding: utf-8
import os

conn=u"rasdial 鱼丸粗面a 2015212605 ****"
disc="rasdial 鱼丸粗面a /disconnect"

os.system(conn) # 连接
os.system(disc) # 断开
``` 