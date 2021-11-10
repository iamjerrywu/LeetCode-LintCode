# Second Max of Array 479 (E)

## Problem

Find the second max number in a given array.

You can assume the array contains at least two numbers.\
The second max number is the second number in a descending array.Have you met this question in a real interview?  YesProblem Correction

#### Example

Example1:

```
Input: [1,3,2,4]
Output: 3
```

Example2:

```
Input: [1,1,2,2]
Output: 2
```

## Solution - Intuition

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        if len(nums) < 2:
            return 0
        first, second = max(nums[0], nums[1]),min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return second
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**

****

## Solution - Quick Select

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        if not nums:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, 2)
    
    def quick_select(self, nums, start, end, n):
        if start == end:
            return nums[start]
        
        left = start
        right = end
        pivot = nums[start + (end - start)//2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left+=1
            while left <= right and nums[right] < pivot:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        #WARNING!
        # if k = 1th, then start == j, also k start from 1
        if start + n - 1 <= right:
            return self.quick_select(nums, start, right, n)
        if start + n - 1 >= left:
            #WARNING!
            # since left part don't care, k should reduct them
            return self.quick_select(nums, left, end, n - (left - start ))
        return nums[right + 1]class Solution:
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**
