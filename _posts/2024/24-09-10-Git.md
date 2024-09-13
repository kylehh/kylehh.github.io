---
title: Git Undo
mathjax: true
toc: true
categories:
  - Study
tags:
  - Git
---

More details at this [link](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

I will start with simple [cheat sheet]([2f5451f](https://www.nobledesktop.com/learn/git/undo-changes)) before diving into reset/revert/checkout

- Undo `git add`  
  `git checkout added_file`  
or `git reset added_file`
- Undo `git commit`  
  `git reset --soft HEAD~`
- Undo `git push`  
  `git revert --no-edt 2f5451f`  
  followed by `git push`

## 1 Checkout
Checkout a branch is the most common usage and what happens behind the scence is moving **HEAD** to a specific **commit**
![Alt text](/assets/images/2024/24-09-10-Git/checkout.png)

Here is the example of `git checkout hotfix` followed by `git checkout HEAD~2`
![Alt text](/assets/images/2024/24-09-10-Git/checkout-head.png)  
## 2 Reset
A reset is an operation that takes a specified commit and resets the "three trees" to match the state of the repository at that specified commit.  
`git checkout hotfix` followed by `git reset HEAD~2` will leave **orphan commits**
![Alt text](/assets/images/2024/24-09-10-Git/resethead.png)

## 3 Revert

## 4 Comparison
|Work level |Reset | Revert | Checkout|  
|---|--|---|---|
|Commit|Discard commits in a private branch|Undo commits in a public branch|Switch between branches|
|File|unstage a file|N/A|Discard changes in the working directory|

