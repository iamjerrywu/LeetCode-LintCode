# Two Sum II - Input array is sorted 608 \(M\)

## Problem

#### Description

Given an array of integers that is already _sorted in ascending order_, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers \(both index1 and index2\) are not zero-based.

You may assume that each input would have exactly one solution.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```text
Input: nums = [2, 7, 11, 15], target = 9 
Output: [1, 2]
```

**Example 2:**

```text
Input: nums = [2,3], target = 5
Output: [1, 2]
```

## Solution - Two Pointers

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] < target:
                start+=1
            elif nums[start] + nums[end] > target:
                end-=1
            else:
                return [start + 1, end + 1]
        return [-1, -1]
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

\*\*\*\*

## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        for i in range(len(nums)):
            idx = self.binary_search(nums, i + 1, len(nums) - 1, target - nums[i])
            if idx != -1:
                return [i + 1, idx + 1]
        
    
    def binary_search(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end)// 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
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



