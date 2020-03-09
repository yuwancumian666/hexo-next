---
title: 深度学习笔记
date: 2019-05-29 00:36:26
categories:
- 深度学习
tags:
- TensorFlow
- Keras
- 深度学习
- 笔记
---

{% blockquote %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
{% endblockquote %}

<!-- more -->

# 模型

## Dropout层

Dropout在训练过程中每次更新参数时按一定概率（rate）随机断开输入神经元，Dropout层用于防止过拟合。


# 调整参数

{% note info %}
    准确率或损失率一直不变的话，可以尝试调整学习率，效果很不错
    我常用的学习率有：0.001、0.0005、0.0001
    `sgd = SGD(lr=0.0001, decay=1e-6, momentum=0.01, nesterov=True)`
{% endnote %}

{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-05-29-same-lr.png %}
