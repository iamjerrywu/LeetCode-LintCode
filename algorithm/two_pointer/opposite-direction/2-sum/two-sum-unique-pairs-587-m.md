# Two Sum - Unique Pairs 587 \(M\)

## Problem

Given an array of integers, find how many `unique pairs` in the array such that their sum is equal to a specific target number. Please return the number of pairs.Example

**Example 1:**

```text
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

```

**Example 2:**

```text
Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        cnt = 0
        while left < right:
            sum_val = nums[left] + nums[right]
            if sum_val > target:
                right-=1
            elif sum_val < target:
                left+=1
            else:
                cnt+=1
                left+=1
                right-=1
            # bypass the duplicated ones
            while left <= right and left > 0 and nums[left] == nums[left - 1]:
                left+=1
            # bypass the duplicated ones
            while left <= right and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right-=1
        return cnt
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
  * Sort: O\(nlogn0
  * Two pointer scan: O\(n\)
* **Space Complexity:**

