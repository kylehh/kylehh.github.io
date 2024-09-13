---
title: Git Merges
mathjax: true
toc: true
categories:
  - Study
tags:
  - Git
---

## Merge vs Rebase
Great explanation from this [tutorial](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

## 1 Merge
`git merge main`is a **non-destructive** operation. The existing branches are not changed in any way, and *feature* branch will have an extraneous **merge commit** every time you need to incorporate upstream changes.   
![Alt text](/assets/images/2024/24-09-13-Git-ff-rebase_files/merge.png)  

## 2 Fast-Forward Merge
When there is **no new commit** in the main branch, mering a feature branch would lead to fast-forward merge.
`git merge feature`
![Alt text](/assets/images/2024/24-09-13-Git-ff-rebase_files/ff.png)  

## 2 Rebase 
**git rebase main** moves the entire *feature* branch to begin on the tip of the *main* branch, effectively incorporating all of the new commits in main. It **re-writes** the project history.  
![Alt text](/assets/images/2024/24-09-13-Git-ff-rebase_files/rebase.png)  

Now you can fast-forwrd the feature branch in main. 

## 3 The golden rule of rebasing
**Never** use it on public branch.
It will force *main* to get all commit from you, while others don't need. 
![Alt text](/assets/images/2024/24-09-13-Git-ff-rebase_files/rebase_feature.png)



