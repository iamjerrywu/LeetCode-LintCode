# Smallest Subset 761 \(M\)

## Problem

Given an array of `non-negative` integers. Our task is to find minimum number of elements such that their sum should be greater than the sum of rest of the elements of the array. At least one positive integer is in the array.Example

Example 1:

```text
Input: nums = [3, 1, 7, 1], 
Output: 1
```

Example 2:

```text
Input: nums = [2, 1, 2], 
Output: 2
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        # write your code here
        half_sum = 0
        for num in arr:
            half_sum+=num
        half_sum = half_sum//2
        arr.sort(reverse = True)
        
        cur_sum, res = 0, 0
        for i in range(len(arr)):
            cur_sum+=arr[i]
            res+=1
            if cur_sum > half_sum:
                return res
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

