# Single Number II 83 \(M\)

## Problem

Given `3*n + 1` non-negative integer, every numbers occurs triple times except one, find it.Example

**Example 1:**

Input:

```text
A = [1,1,2,3,3,3,2,2,4,1]
```

Output:

```text
4
```

Explanation:

Only 4 appears once  
**Example 2:**

Input:

```text
A = [2,1,2,2]
```

Output:

```text
1
```

Explanation:

Only 1 appears onceChallenge

One-pass, constant extra space.

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        
        # ones: the total sum of bits that only appear onces 
        # twos: the total sum of bits that appear twice
        ones, twos = 0, 0
        
        for a in A:
            # would record appeard once only
            # when twice "xor" would eliminate, when three times since &(~twos)
            ones = (ones ^ a) & (~twos)
            # would record only twice 
            # when appear first times, would eliminate by &(~ones)
            # when twice, appear
            # when third times, due two 'xor', would eliminate 
            twos = (twos ^ a) & (~ones)
        return ones 

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

