---
title: Deepseek R1 - CoT
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

Continue with Deepseek R1 from EZ Encoder. [Link](https://www.youtube.com/watch?v=JHrt8_YnmWA)

## 0 System 0 vs System 1

## 1 Chain of Thoughts
"CoT Prompting Elicits Reasoning
in Large Language Models" [paper](https://arxiv.org/pdf/2201.11903) was published by Jason Wei from Google in 2022. Initial method is adding in context prompting.  
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot1.png)

and "Large Language Models are Zero-Shot Reasoners" [paper]() firstly introduced **Let's think step by step** prompt.
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot2.png)

Combining these two methods,"Challenging BIG-Bench tasks and
whether chain-of-thought can solve them"[paper](https://arxiv.org/pdf/2210.09261) tested on **Big Bench-Challenage** dataset.
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot3.png)

"SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT
REASONING IN LANGUAGE MODELS" [paper]() uses LLM generate multiple answers, and use **majority voting** to get the correct answer.
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot4.png)

"LARGE LANGUAGE MODELS CAN SELF-IMPROVE" [paper](https://arxiv.org/pdf/2210.11610) introduces training model in **SFT** step to get better CoT results. and model distillation for reasoning model can get good results as well. 
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot5.png)

Next step, is training in RL step from [paper](https://arxiv.org/pdf/2412.14135)
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/cot6.png)

## 2 Outcome Reward Model vs Process Reward Model
ORM was outcome driven and PRM would check the reasoning step by step
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/orwprw.png)
Reward model used in RL, can also be call **verifier** in the post-training. There are multiple methods to get results from verifier
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/verifier.png)

Three contribution to OAI's [paper](https://arxiv.org/pdf/2110.14168) on using CoT for math problems.
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/3con.png)
- GSM8K (Grade School Math) are element school level test datasets with human annotated CoT.
- Verifier training
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/verifiertrain.png)
- Test Time Compute
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/ttc.png)

The quality goes down after verifier test more than 400 results, but we can combine majority voting to further boost the performance ( voting amount 10 results)
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/400.png)
Training the verifier can be at **token level**(use all token prediction) or **solution level**(Only use the last token). Token level can surpass solution level in the long run. Token level is similar to value functions, needs to tell the final results at early tokens. It has better results than solution level so widely used in OAI.
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/tokensolution.png)

The last technical [paper](https://arxiv.org/pdf/2305.20050) from OAI, use PRM8000 trained a PRW model. 
![Alt text](/assets/images/2025/25-03-01-DeepseekR1-3_files/last.png)

