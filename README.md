---
description: 175 (1N/47E/108M/19H)
---

# Lint/LeeCode notes

## Guideline 

Notes mainly comprises two parts:

### LintCode:

* Topic / category summary from "Jiuzhang Algorithm" course
* Related ladders practice and solution 

### LeetCode:

* Cover problems not in LintCode
* Weekly Challenges

## Common Algorithm in Interview

* O\(logn\):Binary Search
* O\(sqrt\(n\)\): Factorization
* O\(n\): Two Pointer, Monotone Stack, Enumeration
* O\(nlogn\): Sorting, O\(n \* logn \* process on data structure0
* O\(n^2\), O\(n^3\), Dynamic Programming
* O\(2^n\): Combination search
* O\(n!\): Permutation Search 

## Common Data Structure in Interview

![](.gitbook/assets/screen-shot-2021-04-26-at-11.00.34-pm.png)

![](.gitbook/assets/screen-shot-2021-05-02-at-11.40.34-pm.png)

![](.gitbook/assets/screen-shot-2021-05-02-at-11.41.07-pm.png)

## Time Complexity

### Polynomial vs Nondeterministic Polynomial \(NP\)

#### Polynomial: 

* O\(n\)m, O\(n^2\), O\(n^3\), O\(n + m\), O\(sqrt\(n\)\), O\(1\), O\(logn\), O\(nlogn\)

#### Nondeterministic Polynomial \(NP\)

* O\(2^n\), O\(n^n\), O\(n!\)
* Question: 
  * O\(n + m\) vs O\(max\(n, m\)\)?
    * n + m  &gt; max\(n, m\) &gt; \(n + m\) / 2 O\(n + m\) &gt; O\(max\(n, m\)\) &gt; O\(\(n + m\) / 2\) O\(max\(n, m\)\) == O\(n + m\)

### Boundary Condition:

* Normally the evaluation system can run executions up to **10^7 ~ 10^9** times
* Therefore, if input is length of 10^5, then O\(n\) approach can pass, o\(n^2\) may LTE

#### Derive Algorithm from Input range

* n = 10^4
  * O\(n\) -&gt; Two Pointer, Prefix Sum, Traverse, 1-D DP
  * O\(nlogn\) -&gt; Sort, Binary Search
* n = 10^3
  * O\(n^2\) -&gt; 2-D array, double for loop, 2-D DDo P
* n = 10 ^2
  * O\(n^3\) -&gt; Triple for loop
* n = 10
  * O\(2^n\), O\(n!\) -&gt; DFS Brute Force
* n = 10 ^9
  * Don't use extra memory \(like list, dict\) to store input, or O\(n\) appraoch
  * Might be O\(logn\), Binary Search
  * Might be O\(sqrt\(n\)\), Factorization

## Top 75 Questions

[https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)

## Unfinished Chapter

### Algo\_2021

* Chap 17 \(TSP\)

### Algo\_HF\_2021

* Chap15 \(Union Find last two problem, 40 minutes left\)
* Chap16 \(Trie vedio\)



