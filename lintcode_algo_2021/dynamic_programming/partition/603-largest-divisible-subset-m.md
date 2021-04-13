---
description: Partition DP
---

# 603 · Largest Divisible Subset \(M\)

## Problem

Given a set of `distinct positive` integers, find the largest subset which has the most elements, and every pair of two elements `(Si, Sj)` in this subset satisfies: `Si % Sj = 0` or `Sj % Si = 0`.

If there are multiple solutions, return any subset is fine.  
1 \leq len\(nums\) \leq 500001≤len\(nums\)≤50000Example

Example 1:

```text
Input: nums =  [1,2,3], 
Output: [1,2] or [1,3]
```

Example 2:

```text
Input: nums = [1,2,4,8], 
Output: [1,2,4,8]
```

## Approach - DP \(Brute Force\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        last_index = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    # need to record the prev index because later if we want to trace back the set values
                    prev[i] = j
            if dp[i] > dp[last_index]:
                last_index = i
        
        subset = []
        while last_index != -1:
            subset.append(nums[last_index])
            last_index = prev[last_index]

        return subset[::-1]
```
{% endtab %}

{% tab title="java" %}
```java

```
{% endtab %}
{% endtabs %}

## Approach - DP with Hashset Optimization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return 0
        
        nums= sorted(nums)
        n = len(nums)
        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1
        
        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in dp:
                    continue
                if dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
            if dp[num] > dp[last_num]:
                last_num = num
        return self.get_path(prev, last_num)
    
    def get_path(self, prev, last_num):
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]
    
    # no need to find 1 and num itself
    def get_factors(self, num):
        if num == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= num:
            if num%factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num//factor)
            factor+=1
        return factors

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

