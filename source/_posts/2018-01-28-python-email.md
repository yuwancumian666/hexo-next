---
layout: post
title: Python SMTP 发送邮件
date: 2018-01-28 00:00:00 +0800
categories: 
- Python
tags: [Python, 网络编程]
---

{% blockquote 泰戈尔, 飞鸟集 %}
	Like the metting of the seagulls and the waves we meet and come near. The seagulls fly off, the waves roll away and we depart. 
	我们如海鸥之于波涛相遇似的，遇见了，走近了。海鸥飞去，波涛滚滚地流开，我们也分别了。
{% endblockquote %}

<!-- more -->

### 模块简介

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。这里发送邮件使用了 smtplib 和 email 两个模块。

发送邮件常用的模块：
``` python
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
```

### 语法简介

smtplib 模块为发送邮件提供了一种很方便的途径，它对 SMTP 协议进行了简单的封装。其定义的 SMTP 客户端会话对象可使用 SMTP 或 ESMTP 侦听器守护程序向任何互联网机器发送邮件。

创建 smtp 对象的方法是```smtp=smtplib.SMTP([host [, port [, local_hostname]]])```，简单粗暴

* host：SMTP 服务器主机，可指定 IP 或 域名，可选。
* port：一般情况下默认端口号为25.
* local_hostname：如果 SMTP 服务器在本机上运行，则只需指定服务器地址为 localhost 即可。

smtp 对象使用 sendmail 方法发送邮件：```smtp.sendmail(sender, receivers, msg.as_string())```

* sender：发件人邮箱，字符串
* receivers：收件人邮箱，列表
* msg：特定格式的邮件

**注意：**msg是字符串，表示邮件内容。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要指定msg的格式。这个格式就是smtp协议中定义的格式。

### 发送文本格式邮件

这里使用新浪邮箱示例，QQ邮箱登录需要16位授权码，而且验证还过不去(lll￢ω￢)

``` python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host="smtp.sina.com"  #设置服务器
mail_user="yuwancumiana@sina.cn"  #用户名
mail_pass=""  #登陆密码
sender = 'yuwancumiana@sina.cn'
receivers = ['moeext@gmail.com'] 
message = MIMEText('从windows发来的一封测试信', 'plain', 'utf-8')  # 这里指定邮件内容
message['From'] = "yuwancumiana@sina.cn" 
message['To'] =  "鱼丸粗面"
subject = '测试' #主题-title
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException as e:
    print "Error: cannot send my email"
    print e
``` 

接收到的邮件如图：![example-receiver](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-28-example1.png)

### 发送附件

``` python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_SERVER = 'smtp.sina.com'
SMTP_PORT = 25
sender = 'yuwancumiana@sina.cn' 
recipient = 'moeext@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'Python 附件'
msg['To'] = recipient
msg['From'] = sender
subject = 'Python annex'

# 附件1，图片
img = MIMEImage(open(r'img/girl.jpg', 'rb').read(), _subtype='jpg')
img.add_header('Content-Disposition', 'attachment', filename = 'Girl.jpg')
msg.attach(img)

# 附件2，文本
part = MIMEText(open('test.txt','rb').read(), 'plain')
# part["Content-Type"] = 'application/octet-stream'
part["Content-Disposition"] = 'attachment; filename="test.txt"'
part.set_payload("text annex")
msg.attach(part)
try:
    session = smtplib.SMTP()
    session.connect(SMTP_SERVER, 25)
    '''
    session.ehlo()
    session.starttls() 以TLS加密方式传输，可选
    session.ehlo()
    '''
    session.login(sender, 'mq2020.')
    session.sendmail(sender, recipient, msg.as_string())
    print u'发送成功'
    session.quit()
except smtplib.SMTPException,e:  
    print e 
``` 

效果图：![example-receiver](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-28-example2.png)

### 发送 HTML 附件

这里使用的 HTML 是一个小爬虫爬到的数据，经简单包装后返回一个字符串，把字符串作为附件发送。

``` python
#!/usr/bin/python
#coding:utf-8 
import sys 
import smtplib 
import traceback
import make_html_bs
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText    
 
reload(sys)
sys.setdefaultencoding('utf-8')
# 第三方 SMTP 服务  
mail_host="smtp.sina.com"  #设置服务器  
mail_user="yuwancumiana@sina.cn"    #用户名  
mail_pass=""   #密码
  
sender = 'yuwancumiana@sina.cn'  
receivers = ['yuwancumian666@gmail.com','2535257276@qq.com','635936876@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  
   
mail = MIMEMultipart("mixed")  
mail['From'] = "yuwancumiana@sina.cn"  
mail['To'] = "鱼丸粗面" 
mail['Subject'] = Header('福利','utf-8')
message = MIMEText("今日福利(windows)", 'plain', 'utf-8')
mail.attach(message)
try:
    html = make_html_bs.get_html().encode('utf-8') # 这里使用的是另一个爬虫模块返回的数据，为 HTML 格式
except Exception as e:
    print traceback.print_exc()
    sys.exit(u"loading pages failed...")
HTML = MIMEText(html, _subtype='html', _charset='utf-8')
mail.attach(HTML)

try:  

    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)    
    smtp.sendmail(sender, receivers, mail.as_string())
    smtp.close()
    print u"send mail success"  
except smtplib.SMTPException,e:
    print e 

``` 

结果（你猜猜内容是啥😄）：![exp3](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-28-example3.png)

### 总结

因为发送邮件的方式（不加密、SSL、TLS、）和类型（附件类型、附件头，附件内容）多种多样，邮件服务器总结起来也非常他喵的麻烦。我之前是做了不少的测试脚本，最后挑了一个经常用的。我对于这个 python 邮件的想法是：能用就成~O(∩_∩)O
