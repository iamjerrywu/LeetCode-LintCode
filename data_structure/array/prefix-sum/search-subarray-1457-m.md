# Search Subarray 1457 \(M\)

## Problem

Given an array `arr` and a nonnegative integer `k`, you need to find a continuous array from this array so that the sum of this array is `k`. Output the length of this array. If there are multiple such substrings, return the one with the minimum ending position; if there are multiple answers, return the one with the minimum starting position. If no such subarray is found, `-1` is returned.

The length of the array does not exceed 10^610​6​​, each number in the array is less than or equal to 10^610​6​​, and `k` does not exceed 10^610​6​​.Example

**Example 1 :**

```text
Input：arr=[1,2,3,4,5] ，k=5
Output：2
Explanation:
In this array, the earliest contiguous substring is [2,3].
```

**Example 2 :**

```text
Input：arr=[3,5,7,10,2] ，k=12
Output：2
Explanation:
In this array, the earliest consecutive concatenated substrings with a sum of 12 are [5,7].
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def searchSubarray(self, arr, k):
        # Write your code here
        d = dict()
        # if k equals to first element only, then counting length would be 0 - (-1) = 1 
        d[0] = -1
        
        prefix_sum = 0
        for i in range(len(arr)):
            prefix_sum+= arr[i]
            if (prefix_sum - k) in d:
                return i - d[prefix_sum - k]
            
            if prefix_sum not in d:
                d[prefix_sum] = i
        
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

