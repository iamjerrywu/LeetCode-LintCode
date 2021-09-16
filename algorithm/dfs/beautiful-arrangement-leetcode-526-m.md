# Beautiful Arrangement \(LeetCode 526\) \(M\)

## Problem

Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` \(**1-indexed**\) is considered a **beautiful arrangement** if for every `i` \(`1 <= i <= n`\), **either** of the following is true:

* `perm[i]` is divisible by `i`.
* `i` is divisible by `perm[i]`.

Given an integer `n`, return _the **number** of the **beautiful arrangements** that you can construct_.

**Example 1:**

```text
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
```

**Example 2:**

```text
Input: n = 1
Output: 1
```

**Constraints:**

* `1 <= n <= 15`

## Solution - DFS \(Optimized\)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countArrangement(self, n: int) -> int:
        ans = self.dfs(1, 0, [], n, set())
        return ans

    def dfs(self, index, cnt, tmp, n, visited):
        ans = 0
        if cnt == n:
            return 1
        for i in range(1, n + 1):
            if i not in visited and (((cnt + 1) % i == 0) or (i % (cnt + 1) == 0)):
                visited.add(i)
                tmp.append(i)
                ans+=self.dfs(i, cnt + 1, tmp, n, visited)
                tmp.pop()
                visited.remove(i)
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O\(k\)**
  * k: the amount of valid permutations
* **Space Complexity: O\(n\)**

