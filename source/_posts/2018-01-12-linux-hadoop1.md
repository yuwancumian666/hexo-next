---
layout: post
title: Hadoop 的安装
date: 2018-01-12 00:00:00 +0800
categories:
- 大数据
- Hadoop
tags: 
- Hadoop
- HDFS
---


{% blockquote 泰戈尔, 飞鸟集 %}
My heart beats her waves at the shore of the world and writes upon it her signature in tears with the words, "I love thee."
我的心冲激着她的波浪在“世界”的海岸上，蘸着眼泪在上边写着她的题记：“我爱你。”
{% endblockquote %}

<!-- more -->

### 大数据与 Hadoop 简单介绍

**什么是大数据？**

大数据的4V特性：海量的数据规模（volume）、快速的数据流转和动态的数据体系（velocity）、多样的数据类型（variety）和巨大的数据价值（value）。

**Hadoop**

Hadoop 解决的就是 数据的存储（HDFS）和计算分析（MapReduce）的问题。

分布式集群：集群里的每台机器叫一个节点，伪分布式只有一个节点。master 节点负责管理元数据 (Name Node)，slave 负责存储数据 (Data Node)。

保存数据块的信息的数据叫元数据，数据块默认为128MB(Hadoop2)，默认备份3份。
### Hadoop 平台的搭建

**Hadoop 搭建前提：**需要安装 jdk 和 SSH 免密。

**搭建步骤**

1. 上传 Jdk 和 Hadoop 的包到服务器
2. 解压
3. 修改解压后文件夹名，方便以后升级而不用修改环境变量
4. 配置环境变量，路径：用户家目录的 “.bashrc”
``` shell
export JAVA_HOME=/home/groot/soft/jdk
export HADOOP_HOME=/home/groot/soft/hadoop
export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:${PATH}
```
5. 修改配置文件，路径 /home/groot/hadoop/etc/hadoop/
> `A: hadoop-env.sh 找到 “# export JAVA_HOME=${JAVA_HOME}” 字样，在下方修改 jdk 的安装路径 ` <br>
> `B: core-site.xml 配置访问的主机名和端口 (8020)，<name>fs.default.name</name> <value>hdfs://master:8020</value>` <br>
> `C: hdfs-site 配置备份数，指定元数据和数据块的存储目录` <br>
> `D: 用户名不一样的地方都需要改` <br>
> `E: 配置主机名：/etc/sysconfig/network 文件中，修改为 master/slave` <br>
> `F: 配置 IP 和主机名的映射：/etc/hosts 文件，master 和 slave 都要改` <br>
> `G: 配置 SSH 免密，假设在 master 节点家目录的 “.ssh” 文件夹` <br>
>> `a: 生成密钥，ssh-keygen -t rsa -p '' ` <br>
>> `b: 这是本机免密，cat id_rsa.pub >> authorized_keys` <br>
>> `c: 上传公钥到slave，scp id_rsa.pub groot@slave:/home/groot/.ssh/aa.pub` <br>
>> `d: 免密登陆另一台机器，cat aa.pub >> authorized_keys` <br>
>> `e: slave 节点重复 master 节点的做法` <br>
6. `./start-all.sh` 启动 Hadoop
7. 关闭防火墙（需要 root 权限）：`service iptables stop` <br>
8. 浏览器访问50070端口进入 HDFS 的管理界面
9. jps 命令查看进程 主要是查看 Name Node 和 Data Node

### HDFS 的 shell 命令

**操作 HDFS 的三种手段**

1. 通过客户端管理界面查看
2. 通过 HDFS 的 shell 命令
3. 通过 Java 的 API

**Shell 命令**

执行 Shell 命令的根目录应该是 `hdfs:192.168.208.132:8020/`，但是我们一般用 / 代替

1. 创建目录：`hadoop fs -mkdir` 目录名
2. 查看目录：`hadoop fs -ls`
3. 上传文件：`hadoop fs -put` 文件名 路径名

