# Subarray Sum 138 \(E\)

## Problem

Given an integer array, find a subarray where the sum of numbers is **zero**. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.Example

**Example 1:**

```text
Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
```

**Example 2:**

```text
Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]	
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_hash = {0:-1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in prefix_hash:
                return prefix_hash[sum] + 1, i
            prefix_hash[sum] = i
        return -1, -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

