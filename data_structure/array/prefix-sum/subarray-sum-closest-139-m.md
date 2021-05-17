# Subarray Sum Closest 139 \(M\)

## Problem

Given an integer array, find a subarray with sum closest to zero.  
Return the indexes of the first number and last number.

It is guaranteed that the sum of any numbers is in \[-2^{31},2^{31}-1\]\[−2​31​​,2​31​​−1\].Example

**Example1**

```text
Input: 
[-3,1,1,-3,5] 
Output: 
[0,2]
Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
```

Challenge

O\(nlogn\) time

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))

        prefix_sum.sort()

        closest, answer = float('inf'), []
        for i in range(1, len(prefix_sum)):
            if closest > prefix_sum[i][0] - prefix_sum[i - 1][0]:
                closest = prefix_sum[i][0] - prefix_sum[i - 1][0]
                left = min(prefix_sum[i - 1][1], prefix_sum[i][1]) + 1
                right = max(prefix_sum[i - 1][1], prefix_sum[i][1])
                answer = [left, right]
        return answer
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

