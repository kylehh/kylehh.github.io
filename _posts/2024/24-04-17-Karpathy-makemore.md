---
title: Andrej Karpathy-Makemore
mathjax: true
toc: true
categories:
  - Application
tags:
  - Cloud
---

2.5 hr video of [micrgrad](https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&index=1).

## 1. Python tricks
- Counter with dict without if/else  
  ```python  
  d = {}
  d['key'] = d.get('key', 0) + 1
  ```
- Set random seed in Torch
  ```python
  # Fixed rand by manual seed
  g = torch.Generator().manual_seed(2147483647)
  p = torch.rand(3, generator=g)
  p = p / p.sum()
  p
  # sampled from the p distribution
  torch.multinomial(p, num_samples=100, replacement=True, generator=g)
  ```
- Broadcasting semantics
  ```python
  # Line up dims from the trailing dim, and check if they are either
  # - equal
  # - 1  (will be duplicated to match)
  # - none (will be changed to 1, then match)
  P = (N+1).float() # 27x27
  P /= P.sum(1, keepdims=True) #27x1
  # Following operation is wrong
  # line up the last dimention FIRST
  # (27x27)/(27) -> (27x27)/(1,27)
  P /= P.sum(1) #keepdims default=False
  ```
- Plot a square figure  
  ```python  
  plt.imshow(N, cmap='Blues')
  for i in range(dim):
      for j in range(dim):
          plt.text(j, i, 'strb', ha="center", va="bottom", color='gray')
          plt.text(j, i, 'strt', ha="center", va="top", color='gray')
  ``` 
## 2 Neural Network Setups
- Maximum Likehood Estimation

  GOAL: maximize likelihood of the data w.r.t. model parameters (statistical modeling)  
  equivalent to maximizing the log likelihood (because log is monotonic)  
  equivalent to minimizing the negative log likelihood  
  equivalent to minimizing the  average negative log likelihood  
  ```python
  for ix1:
    for ix2:
      prob = P[ix1, ix2]
      logprob = torch.log(prob)
      log_likelihood += logprob
  nll = -log_likehood
  ```  
- One hot encodeing  
  Convert `one_hot` to `float()`!  
  ![Alt text](/assets/images/2024/24-04-17-Karpathy-makemore_files/oneshot.png)

- adfadf



