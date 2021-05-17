# Search Insert Position 60 \(E\)

## Problem

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume **NO** duplicates in the array.Example

**Example 1:**

Input:

```text
array = [1,3,5,6]
target = 5
```

Output:

```text
2
```

Explanation:

5 is indexed to 2 in the array.

**Example 2:**

Input:

```text
array = [1,3,5,6]
target = 2
```

Output:

```text
1
```

Explanation:

2 should be inserted into the position with index 1.

**Example 3:**

Input:

```text
array = [1,3,5,6]
target = 7
```

Output:

```text
4
```

Explanation:

7 should be inserted into the position with index 4.

**Example 4:**

Input:

```text
array = [1,3,5,6]
target = 0
```

Output:

```text
0
```

Explanation:

0 should be inserted into the position with index 0.Challenge

O\(log\(n\)\) time

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

