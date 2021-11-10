---
description: 175 (1N/47E/108M/19H)
---

# Lint/LeeCode notes

## Guideline&#x20;

Notes mainly comprises two parts:

### LintCode:

* Topic / category summary from "Jiuzhang Algorithm" course
* Related ladders practice and solution&#x20;

### LeetCode:

* Cover problems not in LintCode
* Weekly Challenges

## Common Algorithm in Interview

* O(logn):Binary Search
* O(sqrt(n)): Factorization
* O(n): Two Pointer, Monotone Stack, Enumeration
* O(nlogn): Sorting, O(n \* logn \* process on data structure0
* O(n^2), O(n^3), Dynamic Programming
* O(2^n): Combination search
* O(n!): Permutation Search&#x20;

## Common Data Structure in Interview

![](<.gitbook/assets/Screen Shot 2021-08-30 at 8.07.32 PM.png>)

![](<.gitbook/assets/Screen Shot 2021-08-30 at 8.07.42 PM.png>)

![](<.gitbook/assets/Screen Shot 2021-05-02 at 11.40.34 PM.png>)

![](<.gitbook/assets/Screen Shot 2021-05-02 at 11.41.07 PM.png>)

## Time Complexity

### Polynomial vs Nondeterministic Polynomial (NP)

#### Polynomial:&#x20;

* O(n)m, O(n^2), O(n^3), O(n + m), O(sqrt(n)), O(1), O(logn), O(nlogn)

#### Nondeterministic Polynomial (NP)

* O(2^n), O(n^n), O(n!)
* Question:&#x20;
  * O(n + m) vs O(max(n, m))?
    * n + m  > max(n, m) > (n + m) / 2\
      O(n + m) > O(max(n, m)) > O((n + m) / 2)\
      O(max(n, m)) == O(n + m)

### Boundary Condition:

* Normally the evaluation system can run executions up to **10^7 \~ 10^9** times
* Therefore, if input is length of 10^5, then O(n) approach can pass, o(n^2) may LTE

#### Derive Algorithm from Input range

* n = 10^4
  * O(n) -> Two Pointer, Prefix Sum, Traverse, 1-D DP
  * O(nlogn) -> Sort, Binary Search
* n = 10^3
  * O(n^2) -> 2-D array, double for loop, 2-D DDo P
* n = 10 ^2
  * O(n^3) -> Triple for loop
* n = 10
  * O(2^n), O(n!) -> DFS Brute Force
* n = 10 ^9
  * Don't use extra memory (like list, dict) to store input, or O(n) appraoch
  * Might be O(logn), Binary Search
  * Might be O(sqrt(n)), Factorization

## Top 75 Questions

[https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)

## Unfinished Chapter

### Algo\_2021

* Chap 17 (TSP)

### Algo\_HF\_2021

* Chap15 (Union Find last two problems, 40 minutes left)
* Chap16 (Trie vedio)
* Chap19 (Monotonic Stack last two problems, start at 1:05, around 55 mintues left)
* Chap23 (A\* algorithm, watched but not clearly get it)
* Chap 27 (spinning tree)
* Chap28 (Trie hard questions)
* Chap29 (Stack and expression)
* Chap30 (Segment Tree)

