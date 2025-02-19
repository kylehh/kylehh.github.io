---
title: Structured Output
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

How can LLM follow the format defined in structured output?

One good explanation is this youtube [video](https://www.youtube.com/watch?v=xpvFinvqRCA)

## 1 OpenAI API and Outlines lib 
OAI uses Pydantic and Outlier use Regex expression. 
![Alt text](/assets/images/2025/25-02-15-StructuredOutput_files/30b.png)

A finte state machine was maintained for regular express output. You track at which state the tokens are in, and check if the following tokens are valid or not. 
![Alt text](/assets/images/2025/25-02-15-StructuredOutput_files/fsm.png)

The performance is this method are hard to scale in real case. The solution is pre-generate all possibile tokens from this step