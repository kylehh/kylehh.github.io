---
title: From LLM to Agents
mathjax: true
toc: true
categories:
  - study
tags:
  - LLM
---

Yao Shunyu, the original author of ReAct paper, talk about LLM and Agents.
![Alt text](/assets/images/23-09-19-LLM2Agents_files/overview.png)

## 1, ReAct
Reasoning Only: like CoT  
Acting Only: like WebGPT (search only)  
Need to combine both achive human-like results
![Alt text](/assets/images/23-09-19-LLM2Agents_files/react_overview.png)

Comparing action space with RL, RL is external only but ReAct is acting with both internal and external.  
How can we achieve long-term mem? check next point!
![Alt text](/assets/images/23-09-19-LLM2Agents_files/react_summary.png)



## 2 Reflexion
Noah Shinn, a undergraduate from northeastern is the first author of this paper. 

- Use language feedback instead of scalar feedback,0/1. A feedback would be like runtime error msgs, unit test cases and results. 
- Use language update, instead of parameter update like PPO, A3C, DQN.... A update would be like "be sure to handel this corner case"

So this "Verbal" RL would be called Reflexion.
How can we achieve long-term mem? check next point!
![Alt text](/assets/images/23-09-19-LLM2Agents_files/reflex_verbalRL.png)
