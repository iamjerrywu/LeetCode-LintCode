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
        # min_sum: 0 ~ k (contigous subarray minimum sum)
        # max_sum: the max (ans, contigous subarray maximum sum))
        min_sum, max_sum = 0, -float('inf')
        prefix_sum = 0

        for num in nums:
            prefix_sum +=num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        
        return max_sum
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

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
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        ans = dp[0]
        # dp[i] state means the longest length that end with nums[i]
        for i in range(1, n):
            dp[i] = nums[i] + max(0, dp[(i - 1)])
            ans = dp[i] if dp[i] > ans else ans
        return ans
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

\*\*\*\*

## Solution - DP - Strolling Array

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
        dp = [float('inf')] * 2
        dp[0] = nums[0]
        ans = dp[0]
        # dp[i] state means the longest length that end with nums[i]
        for i in range(1, n):
            dp[i%2] = nums[i] + max(0, dp[(i - 1)%2])
            ans = dp[i%2] if dp[i%2] > ans else ans
        return ans
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

