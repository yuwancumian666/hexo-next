---
layout: post
title: Hbase 的安装配置
date: 2018-01-29 00:00:00 +0800
categories:
- 大数据
- HBase
tags: [大数据, Hbase] 
---

{% blockquote 泰戈尔, 飞鸟集 %}
	Take my wine in my own cup, friend. It lose its wreath of foam when poured into that of others. 
	在我自己的杯中，饮了我的酒吧，朋友。一倒在别人的杯里，这酒的腾跳的泡沫便要消失了。
{% endblockquote %}

<!-- more -->

### 环境变量配置

在家目录的 “.bashrc” 文件里边配置环境变量，内容应当包括 JDK、Hadoop 和 Hbase。

``` shell
export JAVA_HOME=/home/user/bigdata/jdk
export HADOOP_HOME=/home/user/bigdata/hadoop
export HBASE_HOME=/home/user/bigdata/hbase
export CLASS_PATH=.:$CLASSPATH:$JAVA_HOME/lib:$JAVA_HOME/jre/lib
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HABASE_HOME/bin:${PATH}
```

为了方便操作 hbase，以上已经添加了配置的 Hbase 环境变量： *HBASE_HOME* （非必须）

### 配置文件

**hbase-env.sh**

在 hbase/conf 文件夹下，打开 hbase-env.sh，找到 jdk 的路径配置，添加 ```export JAVA_HOME=/home/user/bigdata/jdk```
配置完 jdk 路径后，在下方可以看到配置 HBASE_CLASSPATH 的提示，添加 ```export HBASE_CLASSPATH=/home/user/bigdata/hadoop/etc/hadoop```
![exp](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-29-hbase-env.png)

**hbase-site.xml**

进入编辑模式，在 ```<configuration>``` 下添加以下字段：

``` xml
<property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/home/user/bigdata/zookeeper</value>  <!-- Zookeeper下载包解压的位置 -->
</property>
<property>
    <name>hbase.cluster.distributed</name>
    <value>true</value>
</property>
<!-- 使用hdfs：//// URI语法将hbase.rootdir从本地文件系统更改为HDFS实例的地址。 
	在此例中，HDFS在端口8020的本地主机上运行。 -->
<property>
    <name>hbase.rootdir</name>
    <value>hdfs://localhost:8020/hbase</value>
</property>
<property>
    <name>hbase.zookeeper.quorum</name>
    <value>node-a.example.com,node-b.example.com</value>  <!-- 这里填写集群中的主机名 -->
</property>
<property>
   <name>hbase.zookeeper.property.clientPort</name>
   <value>2181</value>
</property>
``` 

此外，如果应用单独Zookeeper，需发更改/conf/hbase-env.sh下配置参数HBASE_MANAGES_ZK的值为true，即：
`export HBASE_MANAGES_ZK=true`

### Hbase 启动、停止、监控

**启动、停止**

`start-hbase.sh(stop-hbase.sh)`，该文件在 hbase/bin 文件夹下，已经添加环境变量，所以可以在任意目录执行。（同 Hadoop）

**查看守护进程**

jps 命令查看守护进程，有 Hmaster 字样说明启动成功。

**浏览器页面查看**

在0.98.x以后的 Hbase 版本中，HBase Web UI使用的HTTP端口从主服务器的60010和每个RegionServer的60030更改为主服务器的16010和RegionServer的16030。