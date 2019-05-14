---
layout: post
title: Hive 数据类型
subtitle: 哈哈哈
date: 2018-02-06 00:00:00 +0800
categories:
- 大数据
- Hive
tags: [Hive, 大数据] 
---

{% blockquote 泰戈尔, 飞鸟集 %}
	I cannot tell why this heart languishes in silence. It is for small needs it never asks, or knows or remembers.
	我说不出这心为什么那样颓丧着，是为了它那不曾要求，不曾知道，不曾记得的小小的需要。
{% endblockquote %}

<!-- more -->

## 基本数据类型

未完待续……

## 复杂数据类型

关系型数据库强烈不建议重复存储
我们接触过的大数据数据库比如 Hbase、Hive 不怕重复，但要求的是存储数据的文件不要太小。

类型 | 说明 | 举例 
Array （数组） | 一组数据类型相同的值 | [1,2,3]
Map（集合）| 一组 <K, V>，要求所有键类型相同，所有值类型相同 | {<K, V>, <K, V>}
Struct（结构） | 一组不同字段，且每个字段的类型可以不同 | ("str", 1, 0)

### 数组

假如我们有以下数据：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-array.jpg)

在 Hive 里创建一个表：

``` sql
CREATE TABLE loginArray(
ip STRING,
userid ARRAY<BIGINT>
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
;
```

然后导入数据：` LOAD DATA LOCAL INPATH '/home/user/test_data/login_array.txt' INTO TABLE loginArray```

查询数据：`SELECT id,userid FROM loginArray`

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-array-id-userid.jpg)

指定数组元素查询：

`SELECT id,userid[0] FROM loginArray` 

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-array-ip-userid%5B1%5D.jpg.jpg)

查询数组长度（-1为空）：`SELECT size(userid) FROM loginArray`

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-array-length.jpg)

### 集合

#### 标准数据表处理

给定测试数据：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-map-1.jpg)

数据表示某用户(id)，在某 IP 的主机上玩了哪些游戏以及游戏次数

开始建表：

``` sql
CREATE TBALE loginmap(
IP STRING,
userid BIGINT,
gameinfo MAP<STRING, INT>
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
MAP KEYS TERMINATED BY ':'
;
```

导入数据：```LOAD DATA LOCAL INPATH '/home/user/test_data/loginmap1.txt' INTO TABLE loginmap;```

插入数据后表结构如图：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-map-1-all.jpg)

#### 含脏数据的表处理

测试数据：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-map-2.jpg)

导入数据时可以直接覆盖上一张表：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-map-2-all.jpg)

在查询某一个键时，因为数据的不统一（如“ wow” 和 “wow”，前者含空格）导致结果不同

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-map-different-info.jpg)

### 结构

数据：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-struct.jpg)

建表：

``` sql
CREATE TABLE loginstruct(
IP STRING,
USRINFO STRUCT<userid:BIGINT, uname:STRING>
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
;
```

导入数据：```LOAD DATA LOCAL INPATH '/home/user/test_data/login_array/loginstruct.txt' INTO TABLE loginstruct```

插入后表信息：

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-02-06-struct-all.jpg)

