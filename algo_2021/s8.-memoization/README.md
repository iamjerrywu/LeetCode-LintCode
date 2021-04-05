# S8. DP/Memoization

## Dynamic Programming \(DP\) 

### Coordination:

### Backpack: 

#### dsd

#### Backpack DP vs DFS

**Time complexity:** 

* Backpack DP: O\(n \* m\)
  * n = total items, m = key value
* DFS: O\(n\*2^n\)
  * n = total items

**Which is better?**

* Ans: It depends!
* Normally DP is faster, however consider of following conditions:
  * \[1,2,4,8, 16\], m = 31, O\(n \* m\) = O\(n \* 2^n\)
  * \[1, 1000, 1000000\], m = 1001001, m &gt;&gt; 2^n, then DFS is faster 
* Concluded that if m is super large, then DFS is possibly faster
* The reason DP is normally faster:
  * \[1,2,3,4,5,5,6,7,8,9,10000\], m = 10010
  * For the first 10 elements's sum should be 10, and there are 5 combinations
  * In DP, don't care about what values inside combinations, only care about whether first n elements can constitute or not! That's the reason it's faster than DFS



