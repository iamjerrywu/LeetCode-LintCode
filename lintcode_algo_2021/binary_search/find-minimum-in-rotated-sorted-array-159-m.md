# Find Minimum in Rotated Sorted Array 159 \(M\)

## Problem

Given a mountain sequence of `n` integers which increase firstly and then decrease, find the mountain top\(Maximum\).

Arrays are strictly incremented, strictly decreasingExample

Example 1:

```text
Input: nums = [1, 2, 4, 8, 6, 3] 
Output: 8
```

Example 2:

```text
Input: nums = [10, 9, 8, 7], 
Output: 10
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # left parts
            if nums[mid] > nums[0] and nums[mid] > nums[-1]:
                start = mid
            # right parts
            else:
                end = mid
        return min(nums[start], nums[end])

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(logn\)**
* **Space Complexity: O\(1\)**

