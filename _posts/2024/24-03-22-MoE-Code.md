---
title: MoE and Decoder-Only Transformer code
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

## 1 MoE
In the context of LLMs, MoEs make a simple modification to this architecture: we replace the feed-forward sub-layer with an MoE layer!
![Alt text](/assets/images/2024/24-03-22-MoE-Code_files/moe.png)

Two primary components:

- **Sparse** MoE Layer: replaces dense feed-forward layers in the transformer with a sparse layer of several, similarly-structured “experts”.

- Router: determines which tokens in the MoE layer are sent to which experts.

We impose sparsity by only sending a token to its top-K experts. For example, many models set k=1 or k=2, meaning that each token is processed by either one or two experts, respectively.

## 2 Mixtral-8x7B MoE
7B Mistral-7B LLM, replace each of its FFSL with MoE layer with **EIGHT** experts, where **TWO** experts are activated for each token.

In total, 47B parameters  
Inference cost, 14B parameters. 