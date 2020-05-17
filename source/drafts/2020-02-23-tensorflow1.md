---
title: TensorFlow
date: 2020-02-23 15:06:28
categories:
- 机器学习
tags:
- TensorFlow
- Keras
- 深度学习
---

TensorFlow2.0 实战笔记

## TensorFlow-Keras

### TensorFlow-Keras 是什么？

+ TensorFlow 对 keras API 规范的实现
+ 相对于以 tensorFlow 为后端的 keras，TensorFlow-Keras 与 TensorFlow 结合更加紧密
+ 实现在tf.keras空间下

<!-- more -->

### TF-Keras 和 Keras联系

+ 基于同一套API
  + keras 程序可以通过更改导入方式轻松转化为 tf.keras 程序
  + 反之可能不成立，因为 tf.keras 有其他特性
+ 相同的 JSON 和 HDF5模型序列化格式和语义

### TF-Keras 和 Keras 区别

+ tf.keras 全面支持[eager mode]()
  + 只用keras.Sequential 和 keras.Model 时没有影响
  + 自定义 Model 内部运算逻辑的时候会有影响
    + TF 底层 API 可以使用 keras 的 model.fit 等抽象
    + 适用于研究人员
+ tf.keras 支持基于 tf.data 的模型训练
+ tf.keras 支持 TPU 训练
+ tf.keras 支持 tf.distribution 中的分布式策略
  + tf.keras 可以和 TensorFlow 中的 estimator 集成
  + tf.keras 可以保存为 SavedModel

我要用哪个？

+ 如果想用 tf.keras 的任何一个特性，选 tf.keras
+ 如果后端互换性很重要（TensorFlow、Theano、CNTK），选keras


## 分类与回归

分类问题预测的是类别，模型输出的是概率分布；回归问题预测的是值，模型输出的是一个实数值

## 目标函数
