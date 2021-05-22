# Search for a Range 61 \(M\)

## Problem

Given a sorted array of `n` integers, find the starting and ending position of a given `target` value.

If the target is not found in the array, return `[-1, -1]`.Example

**Example 1:**

Input:

```text
array = []target = 9
```

Output:

```text
[-1,-1]
```

Explanation:

9 is not in the array.

**Example 2:**

Input:

```text
array = [5, 7, 7, 8, 8, 10]target = 8
```

Output:

```text
[3,4]
```

Explanation:

The \[3,4\] subinterval of the array 1 has the value 8.Challenge

O\(log _n_\) time.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        
        res = []
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] < target:
                start = mid
            else:
                # since want to find first position, end = mid when A[mid] == target
                end = mid
        
        if A[start] == target:
            res.append(start)
        elif A[end] == target:
            res.append(end)

        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] > target:
                end = mid
            else:
                # since want to find last position, start = mid when A[mid] == target
                start = mid
        
        if A[end] == target:
            res.append(end)
        elif A[start] == target:
            res.append(start)
        
        if not res:
            return [-1, -1]
        return res

        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(**
* **Space Complexity:**

