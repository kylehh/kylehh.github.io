---
title: Create Workshop by Hugo Part 1
mathjax: true
toc: true
categories:
  - Application
tags:
  - Frontend
---
Workshop instructions by Hugo is a great tool. Easy to create, goodlooking template and look professional. I am so regretful that my early workshops in AWS were not creat in this format and got lost. AWS later have an internal workshop tool called Workshop something, bascially it's a host for Hugo website.

Here is a quick intro to how to start creating workshop instructions by Hugo. Part one focuses on how to create the local website, and later part two will use S3 to host the static website.

## Step 1, Hugo installation
This is straightforward. Simply run `brew install hugo` to get the job done.

## Step 2, Get a template and start work from there.
This is the [tempalte](https://github.com/kylehh/workshop-template) I created. Git clone it and start working on Markdowns!

## Step 3, local test
Run `hugo server` and then go to the local link, which usually is http://localhost:1313  
![Alt text](/assets/images/2023/23-07-03-hugo-workshop-template_files/hugoserver.png)  

Now you can see the workshop page. Edit file and the changes will be present in real time.   
![Alt text](/assets/images/2023/23-07-03-hugo-workshop-template_files/hugo.png)  