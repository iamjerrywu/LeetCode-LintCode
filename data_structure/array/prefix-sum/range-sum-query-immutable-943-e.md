# Range Sum Query - Immutable 943 (E)

## Problem

Given an integer array nums, find the sum of the elements between indices `i` and `j` `(i ≤ j)`, inclusive.The elements corresponding to `i` and `j` are also included.

1. You may assume that the array does not change.
2. There are many calls to `sumRange` function.

Example

**Example1**

```
Input: nums = [-2, 0, 3, -5, 2, -1]sumRange(0, 2)sumRange(2, 5)sumRange(0, 5)Output:1-1-3Explanation: sumRange(0, 2) -> (-2) + 0 + 3 = 1sumRange(2, 5) -> 3 + (-5) + 2 + (-1) = -1sumRange(0, 5) -> (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

**Example2**

```
Input: nums = [-4, -5]sumRange(0, 0)sumRange(1, 1)sumRange(0, 1)sumRange(1, 1)sumRange(0, 0)Output: -4-5-9-5-4Explanation: sumRange(0, 0) -> -4sumRange(1, 1) -> -5sumRange(0, 1) -> (-4) + (-5) = -9sumRange(1, 1) -> -5sumRange(0, 0) -> -4
```

## Solution - Array Sum

{% tabs %}
{% tab title="Python" %}
```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * n: j - i
* **Space Complexity: O(1)**

****

## Solution - Prefix Sum

{% tabs %}
{% tab title="Python" %}
```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(1)**
* **Space Complexity: O(n)**
