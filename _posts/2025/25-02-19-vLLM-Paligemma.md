---
title: vLLM update - Paligemma
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

Notes of updating MM Processor for Paligemma model

## 0 vLLM local Install and test
The Python-only build installation is `VLLM_USE_PRECOMPILED=1 pip install --editable .`.
and all tests can be run by  
```
pip install -r requirements-dev.txt

# Linting, formatting and static type checking
pre-commit install --hook-type pre-commit --hook-type commit-msg

# You can manually run pre-commit with
pre-commit run --all-files

# Unit tests
pytest tests/
```
Or the specific VLM test can be found [here](https://docs.vllm.ai/en/latest/getting_started/examples/vision_language.html)

## 1 M
