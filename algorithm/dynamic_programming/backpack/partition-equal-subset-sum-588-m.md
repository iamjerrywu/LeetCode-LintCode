# Partition Equal Subset Sum 588 \(M\)

## Problem

Given a `non-empty` array containing `only positive integers`, find if the array can be partitioned into `two` subsets such that the sum of elements in both subsets is equal.

Each of the array element will not exceed 100.  
The array size will not exceed 200.Have you met this question in a real interview?  YesProblem Correction

#### Example

Example 1:

```text
Input: nums = [1, 5, 11, 5], 
Output: true
Explanation:
two subsets: [1, 5, 5], [11]
```

Example 2:

```text
Input: nums = [1, 2, 3, 9], 
Output: false
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        if not nums:
            return False
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total//2
        n = len(nums)

        # dp[i][j] state means first ith items can form sum of j
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j] 
        
        return dp[n][target]
        
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
