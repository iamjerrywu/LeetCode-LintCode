# Two Sum - Less than or equal to target 609 \(M\)

## Problem

Given an array of integers, find how many pairs in the array such that their sum is `less than or equal to` a specific target number. Please return the number of pairs.Example

Example 1:

```text
Input: nums = [2, 7, 11, 15], target = 24. 
Output: 5. 
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
```

Example 2:

```text
Input: nums = [1], target = 1. 
Output: 0. 
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        
        nums.sort()
        cnt = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right-= 1
            else:
                cnt+=right - left
                left+=1
        return cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

