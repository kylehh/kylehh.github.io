---
title: 4Bit Quantization GPTQ and GGUF and 1Bit LLM
mathjax: true
toc: true
categories:
  - Study
tags:
  - Network
---

Summary from zhihu [post](https://zhuanlan.zhihu.com/p/682360619), which some picture from [here](https://www.naddod.com/blog/nvidia-ai-landscape-nvlink-infiniband-and-ethernet-technologies?srsltid=AfmBOorBszfZ4OyBlNPYvxdsYmjW3hzmLAS67ARfUMjtZmdtQKAGweuJ).  

This [blog](https://loop.houmin.site/context/ib2nvlink/) talks lot of parellesim as well.

Also this [post](https://zhuanlan.zhihu.com/p/29384865118) dives really deep into networking which is totally over my understanding. It has a good intro to NCCL at the end.

## 1 NVLink and NVSwitch
- Nvidia's properiatery tech for between GPU communicating links. (Also works between GPU and CPU).
- NVswitch is on the node
- After merging Mellanox, NVLink can work cross nodes with NVLink Switch(off nodes), composing a NVLink Network.  
- NVlink 4.0 supports up to 32 nodes (256 GPUs)

## 2 InfiniBand
- InfiniBand introduced RDMA, bypassing the CPU for memory access
- Introduced in 90s to replace PCI. But deplayed by internet bubble burst. Then Intel goes for PCIe
- Target for AI Factory
- Quantum + Connect-X NIC product from NV
![Alt text](/assets/images/2025/25-05-13-networks_files/infiniband.png)
## 3 RoCE
- RDMA over Converged Ethertnet
- Implementatng RDMA with existing Ethernet, low cost
- v1 is called IBoE. v2 is the main stream now.
- Based on UDP/IP
- iWARP(Internet Wide Area RDMA Protocol) is another RDMA implementation over TCP/IP
## 4 Ethernet
- Target for AI Cloud
- One of the solutions with Inifiband
- Spectrum-X + BlueField DPU product from NV
![Alt text](/assets/images/2025/25-05-13-networks_files/ethernet.png)