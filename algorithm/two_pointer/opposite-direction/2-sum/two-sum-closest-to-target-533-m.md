# Two Sum - Closest to Target 533 \(M\)

## Problem

Given an array `nums` of _n_ integers, find two integers in _nums_ such that the sum is closest to a given number, _target_.

Return the absolute value of difference between the sum of the two numbers and the target.Example

**Example1**

```text
Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
```

**Example2**

```text
Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
```

Challenge

Do it in O\(nlogn\) time complexity.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        start, end = 0, len(nums) - 1
        diff, prev_diff = float('inf'), float('inf')

        while start < end:
            sum_val = nums[start] + nums[end]
            if sum_val > target:
                diff = min(diff, sum_val - target)
                end-=1
            elif sum_val < target:
                diff = min(diff, target - sum_val)
                start+=1
            else:
                return 0
            # early break
            if prev_diff < diff:
                break
        prev_diff = diff
        return diff
                

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity: O\(1\)**

