# Single Number III 84 \(M\)

## Problem

Description

Given `2*n + 2` numbers, every numbers occurs twice except two, find them.Example

**Example 1:**

Input:

```text
array = [1,2,2,3,4,4,5,3]
```

Output:

```text
[1,5]
```

Explanation:

1 and 5 only appear once.

**Example 2:**

Input:

```text
array = [1,1,2,3,4,4]
```

Output:

```text
[2,3]
```

Explanation:

2 and 3 only appear once.Challenge

O\(n\) time, O\(1\) extra space.

## Solution - XOR

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        xor_sum = 0
        for a in A:
            xor_sum^=a
        
        # if x, y are the two numbers only appeared once in A
        # the final xor_sum = all the differet bits in x, y 
        # the first diff bit btw x, y = can be xor_sum & (~xor_sum + 1)
        # (~xor_sum + 1) == -xor_sum
        diff_bit = xor_sum & (-xor_sum)
        
        # so based on the diff_bit, it can seperate A into two group
        # and x, y must in different group
        # two group might be like 2*m + x, 2*n + y
        ans = [0, 0]
        for a in A:
            if not (a&diff_bit):
                ans[0]^=a
            else:
                ans[1]^=a
        return ans
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

