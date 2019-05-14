---
layout: post
title: Hive 分桶
subtitle: 哈哈哈
date: 2018-02-06 00:00:00 +0800
categories:
- 大数据
- Hive
tags: [Hive, 大数据] 
---

哈希分区 （不能再用）
分桶：为解决数据倾斜以及推行机制带来的负面效应 （P131，`Hive编程指南`）

<!-- more -->

## 排序
ORDER BY：运行时走 MapReduce,DISTINCT 走MapReduce
对查询的结果进行全局排序，有一个数据通过一个 Reducer 进行处理。
弊端：大数据集运行过程消耗太多时间

DISTRIBUTE BY：保证具有相同 Key 记录分发到同一个 Reduce 上

SORT BY：对数据进行局部排序 （P110）

CLUSTER BY：如果 distribute by 和 sort by 中涉及到的字段完全相同，且都是升序的时候，CLUSTER BY 就相当于前两个语句。

## 分桶

分区其实是按指定的格式在表下面分出若干个（有限的）文件夹，把相应的文件分到指定的文件夹下，加快查询速度。
分桶：默认采用 HashPartition 分区，能够满足把数据近似均匀地分配到不同的桶里，例如有

``` sql
create table users(
userId INT,
username STRING)
CLUSTERED BY (userid) # 把userid当作key传给hash
SORTED BY (userid ASC) # 归并排序
INTO 2 BUCKETS
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
```

-------------------------------------------------------------

## 视图和索引

### 视图

一组 HiveQL 语句，没有实际的数据

#### 建立视图

1. create view 视图名[(字段名1，字段名2，……)]
   as
   HiveQL
   
#### 查询视图

数据：可以像查表一样查询视图
结构：desc 视图名

#### 删除视图

drop view 视图名

### 索引

#### 建立

``` sql
hive> create index index_stocks on table stocks(symbol)
hive> AS 'org.apache.hadoop.hive.ql.indx.compact.CompactIndexHandler'
hive> with deferred rebuild;
```

#### 查询

`show formatted index on stocks;`

#### 删除

`drop index if exists index_stocks on stocks;`

### 总结

1. 透彻地掌握分区、分桶
2. 透彻地掌握表连接（坑）
3. 掌握排序、视图
4. 了解优化
5. 了解索引

### 会启动 MapReduce 的命令

+ 改索引
+ ORDER BY
+ DISTINCT