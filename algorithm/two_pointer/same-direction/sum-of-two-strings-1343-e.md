# Sum of Two Strings 1343 \(E\)

## Problem

Description

Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.

* A and B are strings which are composed of numbers

Example

```text
Example1:
Input:
A = "99"
B = "111"
Output: "11010"
Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
```

```text
Example2:
Input:
A = "2"
B = "321"
Output: "323"
Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        if not A and not B:
            return ''
        if not A:
            return B
        if not B:
            return A
        
        sum_list = []
        ptr_A, ptr_B = len(A) - 1, len(B) - 1
        while ptr_A >= 0 and ptr_B >= 0:
            sum_list.append(str(int(A[ptr_A]) + int(B[ptr_B])))
            ptr_A-=1
            ptr_B-=1
        while ptr_A >= 0:
            sum_list.append(str(int(A[ptr_A])))
            ptr_A-=1
        while ptr_B >= 0:
            sum_list.append(str(int(B[ptr_B])))
            ptr_B-=1
        # need to reversed tmp
        return ''.join(str for str in reversed(sum_list))
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

