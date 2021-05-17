# Kth Smallest Numbers in Unsorted Array 461 \(M\)

## Problem

Find the kth smallest number in an unsorted integer array.Example

**Example 1:**

```text
Input: [3, 4, 1, 2, 5], k = 3
Output: 3
```

**Example 2:**

```text
Input: [1, 1, 1], k = 2
Output: 1
```

Challenge

An O\(nlogn\) algorithm is acceptable, if you can do it in O\(n\), that would be great.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        # nums.sort(reverse = True)
        # return nums[k - 1]

        if not nums:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, k)
    
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        pivot = nums[(start + end)//2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left+=1
            while left <= right and nums[right] > pivot:
                right-=1
            
            if left <= right:
                nums[left], nums[right]= nums[right], nums[left]
                left+=1
                right-=1
        if start + k -1 <= right:
            return self.quick_select(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

