---
title: Context Extension by YaRN
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

LLM context length can be extended in the post training process. They are all RoPE based algorithem, like [YaRN(Yet Another RoPE extensioN)](https://arxiv.org/pdf/2309.00071)

## 0 RoPE Review
Found another good [video](https://www.youtube.com/watch?v=SMBkImDWOyQ) on RoPE and shows the key idea of rotate original embedding vector based on the **absolute** position in the sentence( ONly based on preceeding words)
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/rope1.png)
The advantage is that the **relative** position of the words are preserved no matter other context.
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/rope2.png)
For higher dimentions, we break it down to 2-dim pairs and define different $\theta$ to capture high and low frequence features
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/rope3.png)
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/freq1.png)
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/freq2.png)

## 1 Position Interpolation
Meta published [PI](https://arxiv.org/pdf/2306.15595) to extent the context window length beyond training. The key idea is to interpolate RoPE directly.It's simple but insufficient at high freq.
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/pi.png)
Let's rewrite RoPE in complex number form
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/pi1.png)
and the PI is formulated as following
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/pi2.png)

## 2 YaRN
[YaRN](https://arxiv.org/pdf/2309.00071) was based on **NTK(Neuron Tagent Kernel)** idea and this [video](https://www.youtube.com/watch?v=DvP8f7eWS7U) shows an early [paper](https://arxiv.org/pdf/2006.10739) to explain this idea.

Following notes are mainly from [zhihu](https://zhuanlan.zhihu.com/p/683863159)

1. NTK-aware method to deal with High-freq lost issue in PI
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/ntk-aware.png)
2. NKT-by-parts
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/ntk-parts.png)
3. NKT-Dynamic 
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/ntk-dynamic.png)
4. YaRN
![Alt text](/assets/images/2025/25-03-22-ContextExtension_files/yarn.png) 