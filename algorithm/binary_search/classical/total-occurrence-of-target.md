# Total Occurrence of Target 462 \(E\)

## Problem

Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.Example

Example1:

```text
Input: [1, 3, 3, 4, 5] and target = 3, Output: 2.
```

Example2:

```text
Input: [2, 2, 3, 4, 6] and target = 4, Output: 1.
```

Example3:

```text
Input: [1, 2, 3, 4, 5] and target = 6, Output: 0.
```

Challenge

Time complexity in O\(logn\)

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
        
        first, last = -1, -1
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                end = mid
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] == target:
            last = end
        elif A[first] == target:
            last = start

        if first == -1 or last == -1:
            return 0
        else:
            return last - first + 1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

