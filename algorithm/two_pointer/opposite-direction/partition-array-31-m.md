# Partition Array 31 \(M\)

## Problem

## Solution

Given an array `nums` of integers and an int `k`, partition the array \(i.e move the elements in "nums"\) such that:

* All elements &lt; _k_ are moved to the _left_
* All elements &gt;= _k_ are moved to the _right_

Return the partitioning index, i.e the first index _i_ nums\[_i_\] &gt;= _k_.

You should do really partition in array _nums_ instead of just counting the numbers of integers smaller than k.

If all elements in _nums_ are smaller than _k_, then return _nums.length_Example

**Example 1:**

Input:

```text
nums = []
k = 9
```

Output:

```text
0
```

Explanation:

Empty array, print 0.

**Example 2:**

Input:

```text
nums = [3,2,2,1]
k = 2
```

Output:

```text
1
```

Explanation:

the real array is\[1,2,2,3\].So return 1.Challenge

Can you partition the array in-place and in O\(n\)O\(n\)?

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] < k:
                left+=1
            while left < right and nums[right] >= k:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        return left
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity:**

## Appendix: Partition Array vs Quick Sort/Select

### Partition Array:

```python
while left <= right:
    while left <= right and nums[left] < k:
        left+=1
    while left <= right and nums[right] >= k:
        right-=1
    
    if left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
        
```

### Quick Select/Sort

```python
while left <= right:
    while left <= right and nums[left] < pivot:
        left+=1
    while left <= right and nums[right] > pivot:
        right-=1
    
    if left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
```

### Conclusion: 

Partition Array need to strictly set two parts that left half &lt; k, while right &gt;= k

Quick Sort/Select only need to let left parts &lt;= right part. If quick sort comparing == pivot, then in extreme case like \[1,1,1,1,1\], the time complexity would be O\(n^2\) -&gt; stack overflow

