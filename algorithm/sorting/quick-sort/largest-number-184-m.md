# Largest Number 184 (M)

## Problem

## Solution - Lambda Sorting

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        
        """first, in order to use cmp_to_key() in sorted(), we need to import 
        functools module and its cmp_to_key() function"""
        
        from functools import cmp_to_key
        
        # check the corner cases 
        if not nums:
            return  ""
        
        # sort nums basing on lambda conditional statement
        nums = sorted(nums, key = cmp_to_key(lambda x, y: \
        -1 if str(x) + str(y) > str(y) + str(x) else 1))
        
        # make a new string
        res = int("".join([str(n) for n in nums]))
        
        return str(res)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity:**

****

## Solution - Quick Sort

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        self.quick_sort(nums, 0, len(nums) - 1)
        return ''.join([str(n) for n in nums]) if max(nums)!=0 else '0'
    
    def quick_sort(self, nums, start, end):
        if start >= end:
            return 
        left, right = start, end
        mid = (left + right)//2
        pivot = nums[mid]
        while left <= right:
            while left <= right and self.compare_highest_digit(nums[left], pivot) == 1:
                left+=1
            while left <= right and self.compare_highest_digit(nums[right], pivot) == 2:
                right-=1
            # exchange value
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end )
    
    def compare_highest_digit(self, num, pivot):
        if str(num) + str(pivot) > str(pivot) + str(num):
            return 1
        elif str(num) + str(pivot) < str(pivot) + str(num):
            return 2
        else:
            return -1

```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**&#x20;
* **Space Complexity:**
