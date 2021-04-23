# Move Zeros 539 \(M\)

## Problem

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

1. You must do this **in-place** without making a copy of the array.
2. Minimize the total number of operations.

Example

Example 1:

```text
Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
```

Example 2:

```text
Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
```

## Solution - Two Pointer \(same direction\)

This solution is straight forward but actualy requiring more modification on values

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        cnt = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                cnt+=2
                left+=1
            right+=1
        print(cnt)
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

## Solution - Two Pointer \(Better\)

Assign all non-zero values on left side, then change those on the right side to zeros

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        cnt = 0
        while right < len(nums):
            while right < len(nums):
                if nums[right] !=0:
                    if left != right:
                       nums[left] = nums[right]
                    cnt+=1
                    left+=1
                right+=1
            
            while left < len(nums):
                if nums[left] != 0:
                    nums[left] = 0
                left+=1
        print(cnt)
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



## Solution - Partition Array \(not remained order\)

Required least modification on values, but would change the original orders

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        cnt = 0
        while left <= right:
            while left <= right and nums[left] != 0:
                left+=1
            while left <= right and nums[right] == 0:
                right-=1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                cnt+=2
                left+=1
                right-=1
        print(cnt)
        print(nums)

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

