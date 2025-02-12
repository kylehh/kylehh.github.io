---
title: Deepseek V3
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

Let's summarize the learning of [deepseek](https://arxiv.org/abs/2412.19437) from recent weeks

## 0 Testing datasets
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro): Univ of Waterloo's Multi-Task Language Understanding Benchmark, enhaunced and released in 2024.12,000 Qs
- [GPQA](https://huggingface.co/datasets/Idavidrein/gpqa)Graduate-Level Google-Proof Q&A Benchmark. 448 Qs
- [Math-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) OpenAI's Math test sets.
- [CodeForces](https://codeforces.com/) Coding competition website
- [SWE-Bench](https://www.swebench.com/) OpenAI's coding datasets from Github issues

## 1 Multi-Head Latent Attention
MLA was introduced in Deepseek V2 [paper](https://arxiv.org/pdf/2405.04434), and it's **Low Rank Decomposition** for KV cache.