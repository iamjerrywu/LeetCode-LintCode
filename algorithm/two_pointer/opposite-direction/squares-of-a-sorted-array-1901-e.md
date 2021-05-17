# Squares of a Sorted Array 1901 \(E\)

## Problem

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

1. 1 &lt;= A.length &lt;= 10000
2. -10000 &lt;= A\[i\] &lt;= 10000
3. A is sorted in non-decreasing order.

Example

**Example 1**

```text
Input: 
[-4,-1,0,3,10]
Output: 
[0,1,9,16,100]
```

**Example 2**

```text
Input: 
[-7,-3,2,3,11]
Output: 
[4,9,9,49,121]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
from collections import deque
class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        # write your code here
        res = deque()
        if not A:
            return res
        i, j = 0, len(A) - 1
        while i <= j:
            if abs(A[i]) < abs(A[j]):
                res.appendleft(A[j] * A[j])
                j-=1
            else:
                res.appendleft(A[i] * A[i])
                i+=1
        return list(res)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

