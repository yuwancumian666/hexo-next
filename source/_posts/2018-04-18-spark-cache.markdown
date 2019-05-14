---
layout: post
title: Spark 持久化
date: 2018-04-18 18:18:18 +0800
description:
categories:
- Spark
tags: 
- Spark 
- 缓存
---

{% blockquote 泰戈尔, 飞鸟集 %}
	The power that boasts of its mischiefs is laughed at by the yellow leaves that fall, and clouds that pass by. 
	权威以它的恶行自夸；落下的黄叶与浮游过的云片都在笑它。
{% endblockquote %}

<!-- more -->

### 持久化策略

rdd.cache(): 相当于调用无参的 persist 方法 (206th in `RDD.scala`)
rdd.persist(): 无参数相当于调用其默认的 "MOMORY_ONLY" 持久化策略(201th in `RDD.scala`)
rdd.unpersist(): 手动把持久化的 RDD 从缓存中移除

<table>
  <tbody>
    <tr>
      <td style="width:140px">级别</td>
      <td style="width:30px">使用空间</td>
      <td style="width:30px">CPU时间</td>
      <td style="width:30px">内存中</td>
      <td style="width:30px">在磁盘</td>
      <td style="width:150px">备注</td>
    </tr>
    <tr>
      <td>NONE</td>
      <td> </td>
      <td> </td>
      <td> </td>
      <td> </td>
      <td> </td>
    </tr>
    <tr>
      <td>MEMORY_ONLY</td>
      <td>高</td>
      <td>低</td>
      <td>是</td>
      <td>否</td>
      <td> </td>
    </tr>
    <tr>
      <td>MEMORY_ONLY_SER</td>
      <td>低</td>
      <td>高</td>
      <td>是</td>
      <td>否</td>
      <td> </td>
    </tr>
    <tr>
      <td>MEMORY_AND_DISK</td>
      <td>高</td>
      <td>中等</td>
      <td>部分</td>
      <td>部分</td>
      <td>如果内存中放不下，则溢写到磁盘上</td>
    </tr>
    <tr>
      <td>MEMORY_AND_DISK_SER</td>
      <td>低</td>
      <td>高</td>
      <td>部分</td>
      <td>部分</td>
      <td>如果内存中放不下，则溢写到磁盘上，在内存中存放序列化后的数据</td>
    </tr>
    <tr>
      <td>DISK_ONLY</td>
      <td>低</td>
      <td>高</td>
      <td>否</td>
      <td>是</td>
      <td> </td>
    </tr>
  </tbody>
</table>

补充：
1. MEMORY_ONLY 和 MEMORY_ONLY_SER 的区别： 前者是以对象的形式存储，后者以序列化的形式（字节数组）存储。
2. MEMORY_ONLY 和 MEMORY_AND_DISK 的区别: 前者先在内存存储，如果内存存不下，就不存了。直接从HDFS上读取数据重新计算。后者先在内存存储，如果内存存不下，把剩下的存入到磁盘当中
3. 选择 MEMORY_ONLY 为默认级别的原因: 按照 Spark 速度快的特性，即使从 HDFS 上取数据重新计算也比多一次 IO 读写要快。记得用我是最好的
4. 在序列化级别后加 "_2"可以把持久化数据存为两份
5. 如果当前 RDD 计算比较复杂，可考虑使用 MEMORY_AND_DISK

以下是其源码：

``` scala
val NONE = new StorageLevel(false, false, false, false)
val DISK_ONLY = new StorageLevel(true, false, false, false)
val DISK_ONLY_2 = new StorageLevel(true, false, false, false, 2)
val MEMORY_ONLY = new StorageLevel(false, true, false, true)
val MEMORY_ONLY_2 = new StorageLevel(false, true, false, true, 2)
val MEMORY_ONLY_SER = new StorageLevel(false, true, false, false)
val MEMORY_ONLY_SER_2 = new StorageLevel(false, true, false, false, 2)
val MEMORY_AND_DISK = new StorageLevel(true, true, false, true)
val MEMORY_AND_DISK_2 = new StorageLevel(true, true, false, true, 2)
val MEMORY_AND_DISK_SER = new StorageLevel(true, true, false, false)
val MEMORY_AND_DISK_SER_2 = new StorageLevel(true, true, false, false, 2)
val OFF_HEAP = new StorageLevel(true, true, true, false, 1)
``` 

### checkpoint——检查点

checkpoint作为容错的设计，基本思路是把当前运行的状态，保存在容错的存储系统中(一般是hdfs)。对于容错的处理，肯定是围绕作业紧密相关的，保存内容包括元数据和数据两部分。

``` scala
sc.setCheckPointDir("path") #设置检查点路径
rdd.checkpoint 
```

使用条件：前面的计算极其复杂，流程特别长。创建checkpoint之后，所有的父级RDD依赖关系全部被移除，本身成为顶级父RDD。使用前应先持久化，否则需要重新计算一次。

### 查看存储级别

先用 Thread.sleep(1000000), 再在 localhost:4040 查看
或者用代码 `rdd.getStorageLevel.description`


