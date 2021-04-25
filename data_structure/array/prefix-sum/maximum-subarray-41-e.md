# Maximum Subarray 41 \(E\)

## Problem

Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

Input:

```text
nums = [−2,2,−3,4,−1,2,1,−5,3]
```

Output:

```text
6
```

Explanation:

the contiguous subarray \[4,−1,2,1\] has the largest sum = 6.  
**Example 2:**

Input:

```text
nums = [1,2,3,4]
```

Output:

```text
10
```

Explanation:

the contiguous subarray \[1,2,3,4\] has the largest sum = 10.

#### Challenge

Can you do it in time complexity O\(n\)?

## Solution - Prefix Sum

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        # dp[i] means the longest contigous array sum that end with nums[ith]
        dp = [-float("inf")] * (n + 1)
        
        # init state
        dp[1] = nums[0]
        
        # function 
        for i in range(1, n + 1):
            dp[i] = nums[i - 1] + max(0, dp[i - 1])
        return max(dp)
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        # dp[i] means the longest contigous array sum that end with nums[ith]
        dp = [-float("inf")] * (n + 1)
        
        # init state
        dp[1] = nums[0]
        
        # function 
        for i in range(1, n + 1):
            dp[i] = nums[i - 1] + max(0, dp[i - 1])
        return max(dp)
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

