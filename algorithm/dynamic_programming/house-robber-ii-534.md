# House Robber II 534 \(M\)

## Problem

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Each house holds a certain amount of money. The only constraint you face is that adjacent houses are equipped with interconnected anti-theft systems, which will automatically alarm when two adjacent houses are robbed on the same day.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

This is an extension of [House Robber](http://www.lintcode.com/problem/house-robber/).It just turns a straight line into a circle.Example

**Example1**

```text
Input: nums = [3,6,4]
Output: 6
```

**Example2**

```text
Input: nums = [2,3,2,3]
Output: 6
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here

        if not nums:
            return 0 
        
        if len(nums) < 2:
            return nums[0]

        n = len(nums)
        dp_left = [0] * n
        dp_right = [0] * n

        dp_left[1] = nums[0]
        dp_right[1] = nums[1]

        for i in range(2, n):
            dp_left[i] = max(dp_left[i - 1], nums[i - 1] + dp_left[i - 2])
            dp_right[i] = max(dp_right[i - 1], nums[i] + dp_right[i - 2])
        return max(dp_left[n - 1], dp_right[n - 1])
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution - DP with Strolling Arrays

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

