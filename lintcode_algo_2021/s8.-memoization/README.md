# S8. DP/Memoization

## Memoization

During DFS or Divide Conquer, use list to memorize the path have been traversed, so next time when traverse on same path no need to go through the entire path from head to end but directly takes the values from memorized array 

### Constraint

When n is large and dfs depth reach O\(n\)

For example, see XXX

{% hint style="danger" %}
1. When both time complexity and dfs depth reach O\(n\), then would stack overflow
   * Since when n reach big, at the same time dfs reach n, would overflow 
2. When time complexity is O\(n^2\) and dfs depth reach O\(n\), then would not overflow
   * Since when n reach big, at the same time dfs reach only sqrt\(n\), it's acceptable
{% endhint %}

## Dynamic Programming \(DP\) 

Big Scale problems depends on small scale problem's result

* Similar concept as recursion, divide and conquer

### Dynamic Programming vs Greedy Algorithm

* DP pursue the long term benefit and sacrifice the short term ones
* Greedy algorithm pursue the maximum benefit

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



