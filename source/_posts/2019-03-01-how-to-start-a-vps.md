---
layout: post
title: VPS使用指南
date: 2019-03-02 00:00:00 +0800
description: 
categories:
- Software
tags: 
- ssr
- Linux
---

{% cq %} 默念二十四字社会主义核心价值观 {% endcq %}

<!-- more -->

# 安装ShadowsocksR

使用root用户登录，运行以下命令：

``` shell
# 安装ShadowsocksR
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh
chmod +x shadowsocksR.sh
./shadowsocksR.sh 2>&1 | tee shadowsocksR.log

# 卸载ShadowsocksR
./shadowsocksR.sh uninstall

# 安装 BBR
wget --no-check-certificate https://raw.githubusercontent.com/moeext/how-to-start-a-new-VPS/master/tcp.sh
chmod +x tcp.sh
./tcp.sh
```

## 多用户配置示例

``` json
{
    "server":"0.0.0.0",
    "server_ipv6":"[::]",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
        "10657":"***",
        "10658":"***",
        "10659":"***",
        "10660":"***"
    },
    "timeout":120,
    "method":"aes-256-cfb",
    "protocol":"origin",
    "protocol_param":"",
    "obfs":"plain",
    "obfs_param":"",
    "redirect":"",
    "dns_ipv6":false,
    "fast_open":false,
    "workers":1
}
```


# 更改Python软连接

查看已安装python版本 `ls /usr/bin`

``` shell
rm /usr/bin/python
ln -s /usr/bin/python3.5 /usr/bin/python
```

# 定时任务 crontab

``` bash
crontab -e
#30 22 * * * python ~/email/pymail.py >> ~/email/pymail.log
# 修改默认编辑器
select-editor
```
