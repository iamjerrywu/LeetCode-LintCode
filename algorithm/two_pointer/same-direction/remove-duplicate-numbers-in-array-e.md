# Remove Duplicate Numbers in Array 521 (E)

## Problem

[https://www.lintcode.com/problem/521/](https://www.lintcode.com/problem/521/)

Given an array of integers, remove the duplicate numbers in it.

You should:

1. Do it in place in the array.
2. Put the element after removing the repetition at the beginning of the array.
3. Return the number of elements after removing duplicate elements.

You don't need to keep the original order of the integers.Example

Example 1:

```
Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
```

Explanation:

1. Move duplicate integers to the tail of _nums_ => _nums_ = `[1,3,4,2,?,?]`.
2. Return the number of unique integers in _nums_ => `4`.\
   Actually we don't care about what you place in `?`, we only care about the part which has no duplicate integers.

Example 2:

```
Input:
nums = [1,2,3]
Output:
[1,2,3]
3
```

Challenge

1. Do it in O(n) time complexity.
2. Do it in O(nlogn) time without extra space.

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        i, j = 0, 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] == nums[i]:
                j+=1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]
        return i + 1
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
