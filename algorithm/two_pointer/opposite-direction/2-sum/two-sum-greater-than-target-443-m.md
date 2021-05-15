# Two Sum - Greater than target 443 \(M\)

## Problem

Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.Example

**Example 1:**

```text
Input: [2, 7, 11, 15], target = 24
Output: 1
Explanation: 11 + 15 is the only pair.
```

**Example 2:**

```text
Input: [1, 1, 1, 1], target = 1
Output: 6
```

Challenge

Do it in O\(1\) extra space and O\(nlogn\) time.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        cnt = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] <= target:
                start+=1
            else:
                cnt+=end - start
                end-=1
        return cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
  * Sort: O\(nlogn\)
  * Traverse: O\(n\)
* **Space Complexity: O\(1\)**

