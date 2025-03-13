---
title: Deepseek R1 - Training
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

Continue with Deepseek R1 from EZ Encoder. [Link](https://www.youtube.com/watch?v=JHrt8_YnmWA)

## 0 Overview
R1 overview. The great achievment of R1 is making many previous ideas really work in LLM
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/R1.png)

## 1 RL without SFT
[Teaching Large Language Models to Reason with Reinforcement Learning](https://arxiv.org/abs/2403.04642) evaluate different RL methods for reasoning model, and tried RL without Reward Model, without SFT initialization. 
The result was relatively good, but nothing compared to R1 due to model size is very small 13B. (Sparse is result-only RM, and dense is process RM)
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/meta.png)

## 2 Training paradiam 
The training paradiam is similiar to Llama 3, using Deepseek V3 as the reward model to clean reasoning data -- **Rejection Sampling**
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/llama.png)

## 3 Distillation
[LLM can self improve](https://arxiv.org/pdf/2210.11610) paper compared model distillation to a smaller model. 
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/distill.png)

## 4 R1 Training
The RW in R1 is rule based, focusing on accuracy and formatting.
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/rw.png)
There are 2 rounds of training for R1. Round 1 focusing in reasoning, 
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/round1.png)
Round 2 is adding on general capability. Use model trained in round 1 to generate reasoning data, and rejection sampling by V3. Have 800K of training data in total.
![Alt text](/assets/images/2025/25-03-11-DeepseekR1-4_files/round2.png)


