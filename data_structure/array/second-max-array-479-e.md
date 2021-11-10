# Second Max Array 479 (E)

## Problem

Description

Find the second max number in a given array.

You can assume the array contains at least two numbers.\
The second max number is the second number in a descending array.Example

Example1:

```
Input: [1,3,2,4]
Output: 3
```

Example2:

```
Input: [1,1,2,2]
Output: 
```

## Solution - First, Second Comparison

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

## Solution - Brute Force Sort

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
        nums.sort()
        return nums[len(nums) - 2]
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
        return self.quick_select(nums, 0, len(nums) - 1, 2)
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        pivot = nums[(start + end)//2]
        
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left+=1
            while left <= right and nums[right] < pivot:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        if start + k - 1 <= right:
            return self.quick_select(nums, start, right, k)
        elif start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]
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
