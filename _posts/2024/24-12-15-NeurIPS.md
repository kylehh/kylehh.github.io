---
title: Interesting papers
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

This past week is NeurIPS and I would like to share some paper I read recently.


趁这周NeurIPS，分享几篇最近刷到有意思的paper。开始之前先谈感想：听过很多关于大模型不会思考的论调，我觉得这是人类的一种傲慢。学习AI对我来说就是对大脑祛魅的过程，模拟所谓的思维，逻辑，甚至情感，我都认为没有不可跨越的鸿沟。


[第一篇](https://arxiv.org/pdf/2411.07191)来自苹果，说的是大模型几百亿个参数里面会有个别超级参数，还举个栗子改一个超参，就能让大模型输出乱码。好比一个脑细胞坏了，你就不会说话了。这跟武侠点穴异曲同工，牵一发而动全身

后两篇是Meta。[一](https://ai.meta.com/research/publications/byte-latent-transformer-patches-scale-better-than-tokens/)是说不用tokenzier直接训练字节也成了。tokenizier是大模型一大软肋，任何进展都值得观望。

[第二](https://arxiv.org/abs/2412.06769)出自渊栋田大神的团队，背后的原理非常符合直觉：人类思考并不是全部都表达成语言，所以应该直接在潜空间训练模型思考，而不是在token空间。模型思考最近大火，我猜OAI的o1估计也用了类似的技术。

碳基们，你还能嘚瑟几天？