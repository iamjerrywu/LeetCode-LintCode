# Interleaving Positive and Negative Numbers 144 \(M\)

## Problem

Description

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

You are not necessary to keep the original order of positive integers or negative integers.Example

_**Example 1**_

```text
Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
```

Challenge

Do it in-place and without extra memory.

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        left, right = 0, len(A) - 1
        # quick sort with pivot 0
        while left <= right:
            while left <= right and A[left] < 0:
                left+=1
            while left <= right and A[right] > 0:
                right-=1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left+=1
                right-=1
        # if neg_nums = pos_nums + 1
        if left > len(A) - right - 1:
            i, j = 1, len(A) - 1
        # if neg_nums + 1 = pos_nums
        elif left < len(A) - right - 1:
            i, j = 0, len(A) - 2
        # if neg_num == pos_nums
        else:
            i, j = 0, len(A) - 1
        # swap neg/pos num by 2 interval
        while i <= j:
            A[i], A[j] = A[j], A[i]
            i+=2
            j-=2
        

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

