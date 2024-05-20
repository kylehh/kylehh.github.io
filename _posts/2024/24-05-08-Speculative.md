---
title: Speculative Decoding
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

A discussion around tokenizers in slack leads to following comment:   
Would be the natural progression after you arrive at the fact taking three steps to get `sm` `art` `er` may be inefficient when there is a high proba it’s going to be `smarter`

That's a good explanation of the intuition behind speculative decoding.
## 1  Speculative Sampling and Speculative Decoding

[DeepMind](https://arxiv.org/pdf/2302.01318) and [Google](https://proceedings.mlr.press/v202/leviathan23a/leviathan23a.pdf) published two paper around the same time regarding this algorithm. 

Define notations as follow:  
$M_p$ = draft model (llama-7b)  
$M_q$ = target model (llama-70b)  
$pf$ = prefix, $K$ = 5  
Do following two steps in parallel. 
1. Run draft model for K steps to generate K tokens 
2. Run target model once to get distributions of K+1 tokens (No sampling here)
![Alt text](/assets/images/2024/24-05-08-Speculative_files/drafttarget.png) 
The key algorithm is **reject sampling**, accept or reject tokens based on values of p/q
![Alt text](/assets/images/2024/24-05-08-Speculative_files/rejectsampling.png)  
Even when rejected, still sample the final token from $(q(x)-p(x))_+$. This step is important to make sure we generate at least 1 token.
![Alt text](/assets/images/2024/24-05-08-Speculative_files/finaltoken.png)  
The worse case is to generate 1 token in each pass, and the best case is to generate K+1 tokens, so speedup is garanteened. 
![Alt text](/assets/images/2024/24-05-08-Speculative_files/speedup.png)  

## 2 Medusa
Tianlei Li from Princeton/Together.ai and Yuhong Li from UIUC published [Medusa](https://arxiv.org/pdf/2401.10774) paper in early 2024. 

## 3 Others
Latest [paper](https://arxiv.org/abs/2404.19737) from Meta. Similar to Medusa? 

