# Search in Rotated Sorted Array II 63 \(M\)

## Description

Follow up for [Search in Rotated Sorted Array](http://www.lintcode.com/problem/search-in-rotated-sorted-array/):

What if **duplicates** are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.Example

**Example 1:**

Input:

```text
A = []target = 1
```

Output:

```text
false
```

Explanation:

Array is empty, 1 is not in array. **Example 2:**

Input:

```text
A = [3,4,4,5,7,0,1,2]target = 4
```

Output:

```text
true
```

Explanation:

4 is in the array



## Problem

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        if not A:
             return False
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] == target:
                return True
            if A[mid] > A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[start]:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                start+=1
        
        if A[start] == target:
            return True
        if A[end] == target:
            return True
        return False

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

