# Wiggle Sort 508 \(M\)

## Problem

Given an unsorted array `nums`, reorder it **in-place** such that

```text
nums[0] <= nums[1] >= nums[2] <= nums[3]....
```

Please sort the array in place and do not define additional arrays.Example

**Example 1:**

```text
Input: [3, 5, 2, 1, 6, 4]Output: [1, 6, 2, 5, 3, 4]Explanation: This question may have multiple answers, and [2, 6, 1, 5, 3, 4] is also ok.
```

**Example 2:**

```text
Input: [1, 2, 3, 4]Output: [1, 4, 2, 3]
```

## Solution - Not In Place

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here

        nums.sort()
        
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if left <= right:
                ans.append(nums[left])
                left+=1
            if left <= right:
                ans.append(nums[right])
                right-=1
        for i in range(len(nums)):
            nums[i] = ans[i]
        
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - In Place

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

