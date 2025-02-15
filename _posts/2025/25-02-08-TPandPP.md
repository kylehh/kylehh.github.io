---
title: Tensor Parallelism and Pipeline Parallelism
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

There are multiple parallelism strategies

## 1 Data Parallelism
While MLPs have fixed activation functions on nodes (“neurons”), KANs have learnable
activation functions on edges (“weights”). KANs have NO linear weights AT ALL – every
weight parameter is replaced by a univariate function parametrized as a spline. 
![Alt text](/assets/images/2025/25-02-08-TPandPP_files/)

