# House Robber II 534 (M)

## Problem

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Each house holds a certain amount of money. The only constraint you face is that adjacent houses are equipped with interconnected anti-theft systems, which will automatically alarm when two adjacent houses are robbed on the same day.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Each house holds a certain amount of money. The only constraint you face is that adjacent houses are equipped with interconnected anti-theft systems, which will automatically alarm when two adjacent houses are robbed on the same day.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

This is an extension of [House Robber](http://www.lintcode.com/problem/house-robber/).It just turns a straight line into a circle.Example

This is an extension of [House Robber](http://www.lintcode.com/problem/house-robber/).It just turns a straight line into a circle.Example

**Example1**

**Example1**

```
Input: nums = [3,6,4]
Output: 6
```

```
Input: nums = [3,6,4]
Output: 6
```

**Example2**

**Example2**

```
Input: nums = [2,3,2,3]
Output: 6
```

```
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

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

## Solution - DP with Strolling Arrays

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
        dp_left = [0] * 3
        dp_right = [0] * 3

        dp_left[1] = nums[0]
        dp_right[1] = nums[1]

        for i in range(2, n):
            dp_left[i%3] = max(dp_left[(i - 1)%3], nums[i - 1] + dp_left[(i - 2)%3])
            dp_right[i%3] = max(dp_right[(i - 1)%3], nums[i] + dp_right[(i - 2)%3])
        return max(dp_left[(n - 1)%3], dp_right[(n - 1)%3])
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**





## Solution - DP **(2)**

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])

        n = len(nums)
        # house[0] ~ house[n - 2]
        dp_left = [0] * n
        dp_left[0] = nums[0]
        dp_left[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp_left[i] = max(dp_left[i - 1], dp_left[i - 2] + nums[i])
        
        # house[1] ~ house[n - 1]
        dp_right = [0] * n
        dp_right[1] = nums[1]
        dp_right[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp_right[i] = max(dp_right[i - 1], dp_right[i - 2] + nums[i])
        
        return max(dp_left[n - 2], dp_right[-1])
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
