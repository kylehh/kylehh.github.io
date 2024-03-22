---
title: MoE and Decoder-Only Transformer code
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---



## 1 Enable CORS in API Gateway
This is the most obvious step to do, and just follow instructions on the console and use default options.An `OPTION` method will be added as `MOCK` integration type  
![Alt text](/assets/images/24-03-22-MoE-Code_files/console.png)

## 2 Add modify the API resources
Now you need to modify `Integration reqeust` and `Integration response` for the `OPTION` method. I believe this is the key step to make CORS work. Some posts say you also need to modify `Header mappings`, and I also did, but Im not sure if it's necessary.  
![Alt text](/assets/images/23-09-15-CORS_files/integration.png)

Even though Im not fully understand the 4 steps here, especially the differences between Method vs Integration, the `Mapping templates` need to be filled with proper json responses. 
- for `Integration reqeust` , add `{"statusCode" : 200}`
- for `Integration response` , add `{"statusCode" : 200, "message": "Go ahead without me"}`  

![Alt text](/assets/images/23-09-15-CORS_files/mappingtemplates.png)
## 3 Test CORS
[https://test-cors.org](https://test-cors.org/) is a simple website to test out your CORS setups. Using `POST` method and you are espected to see status 200.