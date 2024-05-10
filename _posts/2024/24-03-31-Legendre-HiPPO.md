---
title: Legendre polynomials and HiPPO
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
  - Math
---

## 0 References
[HiPPO](https://arxiv.org/abs/2008.07669) paper by Albert Gu, Tri Dao, 2008

[Structured State Space for Sequence Modeliing S4](https://arxiv.org/abs/2111.00396) paper by Albert Gu, 2021

[Hungry Hungry HiPPO](https://arxiv.org/abs/2212.14052) paper by Dan Fu, Tri Dao, 2022

The next one will discuss about 
[Mamba](https://arxiv.org/abs/2312.00752) paper by Albert Gu, Tri Dao, 2023

## 1 Legendre Polynomials
Legendre Polynomial is a set of  orthogonal polynomials. They are solutions to Legendre DE
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/legendre.png)  
and can be rewrtie as following
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/liouville.png)    

- They are orthogonal on the interval [-1, 1] with respect to the uniform measure on that interval.
-  Let $P_n$ be the nth Legendre polynomial. Then, for all n, $P_n(1)=1$ and $P_n(-1)=(-1)^n$ 

## 2 Exponential Moving Average
Simply Moving Average is unweighted mean of the previous K data point in finance, or take equal number of data on either side of a central value in engineer and science. 

Exponential Moving Average is weighted mean with a parameter $\alpha$. For new value $p_t$ at time $t$, we have     
$$EMA_t = \alpha * p_t + (1-\alpha)*EMA_{t-1}$$  

Plug in $EMA_{t-1}$ and so on, you will get  
$$EMA_t = \alpha * (p_t + (1-\alpha)*p_{t-1}+(1-\alpha)^2p_{t-2}+(1-\alpha)^3p_{t-3}+...)$$ 

Here is the figure of EMA weights
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/ema.png)  

## 3 HiPPO
The problem HiPPO trying to solve is the long term memory issue and need to be updated in a constant time. 
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/motivation.png)

The solution is to use a polynomial to match the signal up to time $t$
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/coeff.png)  

The difference of fitted polynomial and original singnal can be measured in different ways, like EMA.  

The coefficient X is actually 64 dim, and only showes 4 in the figure below. The latest X value represents the whole red curve which matches well in near and degrade in the past, which is exactly the EMA measure. 
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/emameasure.png)  

You can also have uniform measure
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/uniformmeasure.png) 
or time-varying measure
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/tv1measure.png)  
![Alt text](/assets/images/2024/24-03-31-Legendre-HiPPO_files/tv2measure.png)   