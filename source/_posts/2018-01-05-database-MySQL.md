---
layout: post
title: MySQL 进阶
date: 2018-01-05 00:00:00 +0800
categories: 
- MySQL
tags: 
- 数据库
- MySQL
---


{% blockquote 泰戈尔, 飞鸟集 %}
	My day is done, and I am like a boat drawn on the beach, listening to the dance-music of the tide in the evening.
	日间的工作完了，于是我像一只托在海滩上的小船，静静地听着晚潮跳舞的乐声。
{% endblockquote %}

<!-- more -->

## 基础语法

#### 简介

数据库（Database）是按照数据结构来组织、存储和管理数据的仓库，是一款高效存储数据和提供分析计算功能的软件。它描述的是数据和信息之间的关系。<br>
众所周知，MySQL 为*关系型数据库*(Relational Database Management System)，这种数据库存储数据的模型称为“关系模型”，这种关系模型将生活中的每种数据抽象成一个表。

  表       | table  是关系型数据库中基本存储单位 
  表里有行 | row 
  表里有列 | column 

MySQL所使用的 SQL（结构化查询语言）语言是用于访问数据库的最常用标准化语言。主要分为四类：

分类 |   说明   | 关键字
---- | -------- | ------
 DDL | 定义语言 | creat
 DML | 操作语言 | insert、delete、update
 DCL | 控制语言 | grant、remove
 DQL | 查询语言 | select

#### 登陆数据库 

mysql [-D 所选择的数据库名] -h 主机名 -u 用户名 -p，括号中内容可选。

#### PROMPT 提示符的修改

\D | 完整的日期
\d | 当前数据库
\h | 服务器名称
\u | 当前用户

#### 数据库操作

create database name | 创建数据库
show databases       | 查看所有数据库
drop database name   | 删除某数据库
use xxx              | 在下文使用某数据库
truncate 表明        | 清空表中的记录

#### 表操作

create table 表名 (列名 数据类型 约束, 列名1···, ···约束) | 创建表，表名一般是以tb_ 开头 
drop table  表名  | 删除表
alter table  表名 | 添加列
add/drop  column  | 添加/删除行

####约束

not null      | 非空约束
unique        | 唯一约束
primary key   | 主键约束
foreigner key | 外键约束
checked       | 检查约束   

#### 增删查改（CRUD）

插入数据 | insert into 表名 (列名1,列名2,...) values (值1,值2,...); <br>insert into 表名 values (值1,值2,...,值N); <br>insert into 表名 xxx values (),(),();
修改数据 | update 表名 set 列名 = 列值 ,列名1=列值1,...;
删除数据 | delete from 表名 where;

``` sql
-- 基本查询语法
select * from tableName --
-- where 子句功能是增加选择条件  
select 列名1,... from tb_name where 条件 
/*where 的条件{
  > < >= <= = != <> 
  is null is not null
  between and 
  in (1,2,3,4)
  not in (1,2)
  并且 and 或者 or}*/
```

## 高级查询

#### 模糊查询

select \* from tb_name where usr_name like '条件' 

%     | 表示任意0个或多个字符。可匹配任意类型和长度的字符 <br> select \* from tb_name where usr_name like 'A%' 会找出所有名字以‘A'开头的记录，可使用‘and’增加条件
_     | 表示任意单个字符，常用来限制表达式的字符长度语句 <br> select \* from tb_name where usr_name like '_b' 会找出所有名字第二位是‘b’的记录
[]    | 表示括号内所列字符中的一个 <br> select \* from tb_name where usr_name like '_[a-c]' 会找出所有名字第二位为‘a、b、c’的记录
[^]   | 表示不在括号所列之内的单个字符 <br> select \* from tb_name where usr_name like '_[a-c]' 会找出所有名字第二位为不是‘a、b、c’的记录

#### 分组查询

语法：“*group by 要分组的列*，”列可以选择多个。一般都和聚合函数搭配使用，而聚合函数可以单独使用。<br>
*聚合函数：* avg()、sum()、max()、min()、count()、group_concat()、select avg(sal)、depto from 表名 group by 列名 <br>
注意：查询结果里只能出现被分组的列和聚合的列

#### 排序

在查询语句后加 *order by 要排序的列 desc(或asc)，*其中 desc 为降序，asc 为升序。

#### 分页

limit m,n  限制，
m=(页码-1)\*n，
topN 问题：先排序，再分页

#### 去重查询
关键字：*distinct，*去掉重复记录，在select后使用即可。

#### 子查询

子查询就是在查询里写查询，一般用于解决一步不能查询求解的问题。其用法非常灵活，几乎可以写在查询的任何位置。<br>
语法：<br>
1. 子查询可以写在select后，作为查询结果
2. 子查询可以写在 from 后，作为查询源
3. 子查询可以写在 where 后，作为查询条件
4. 子查询可以使用主查询的资源，子查询要加括号包裹使用
5. 当子查询作为数据源在 from 后时，要起别名
6. 子查询还可以用在 update、insert、delete 里
7. **having** 限制条件和 where 的功能一样但是having是可以先分组再过滤，但where是先过滤再分组

#### 表连接

表连接的作用是将多个表放在一起查询，解决一个表的数据不满足查询需求的问题。<br>
语法：*from a, b* <br>
需要注意的是，表连接会产生笛卡尔积，使用的时候一定要使用条件加以限制。











