# Find Peak Element 75 \(M\)

## Problem

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end)//2
            # if uphill
            if A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            # if downhill
            else:
                end = mid
        if A[start] > A[mid]:
            return start
        return end
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

