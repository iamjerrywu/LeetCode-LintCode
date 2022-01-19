# House Robber 392 (M)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.Example

**Example 1:**

```
Input: [3, 8, 4]
Output: 8
Explanation: Just rob the second house.
```

**Example 2:**

```
Input: [5, 2, 1, 3]
Output: 8
Explanation: Rob the first and the last house.
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max money when robbing first iths houses 
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
                dp[i] = max(dp[(i - 1)], dp[(i - 2)] + nums[i])
        return dp[-1]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

## Solution - DP with Strolling Arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max money when robbing first iths houses 
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * 3
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
                dp[i%3] = max(dp[(i - 1)%3], dp[(i - 2)%3] + nums[i])
        return max(dp)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
