# Subarray Sum Equals to k II 1844 \(M\)

## Problem

Given an array of integers and an integer k, you need to find the minimum size of continuous subarrays whose sum equals to k, and return its length.

if there are no such subarray, return -1.

the integer nums\[i\] may lower than 0Example

**Example1**

```text
Input: 
nums = [1,1,1,2] and k = 3
Output: 
2
```

**Example2**

```text
Input: 
nums = [2,1,-1,4,2,-3] and k = 3
Output: 
2
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        prefix_sum = self.get_prefix_sum(nums)

        ans = float('inf')
        sum_to_index = {0: 0}
        for end in range(len(nums)):
            # if in array traversed so far, exist the value of prefix_sum(end + 1) - k
            if prefix_sum[end + 1] - k in sum_to_index:
                length = end + 1 - sum_to_index[prefix_sum[end + 1] - k]
                # might exist multiple valid start and end, pick the minimum length btw them
                ans = min(ans, length)
            sum_to_index[prefix_sum[end + 1]] = end + 1
        return ans if ans != float('inf') else -1
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
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

