---
description: Google
---

# Ambiguous Coordinates 1372 \(M\)

## Problem

We had some 2-dimensional coordinates, like `"(1, 3)"` or `"(2, 0.5)"`. Then, we removed all commas, decimal points, and spaces, and ended up with the string `S`. Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits. Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. Also note that all coordinates in the final answer have exactly one space between them \(occurring after the comma.\)

`4 <= S.length <= 12`.  
`S[0]` = "\(", `S[S.length - 1]` = "\)", and the other elements in `S` are digits.Example

**Example 1:**

```text
Input："(00011)"
Output：["(0.001, 1)", "(0, 0.011)"]
Explanation：0.0, 00, 0001 or 00.01 are not allowed.
```

**Example 2:**

```text
Input："(100)"
Output：[(10, 0)]
Explanation：1.0 is not allowed.
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param S: An string
    @return: An string
    """
    def ambiguousCoordinates(self, S):
        # write your code here
        if not S:
            return []
        S = S[1:-1]
        res = []
        for i in range(1, len(S)):
            left, right = S[:i], S[i:]
            self.get_answer(left, right, res)
        return res
    
    def get_answer(self, left, right, res):
        if len(self.form_valid(left)) > 0 and len(self.form_valid(right)) > 0:
             for left_number in self.form_valid(left):
                 for right_number in self.form_valid(right):
                    res.append('(' +  left_number + ', ' + right_number + ')')
    
    def form_valid(self, string):
        res = []
        if len(string) > 1:
            if string[0] == '0' and string[-1] != '0':  
                res.append(string[0] + '.' + string[1:])
            elif string[0] != '0':
                res.append(string)
                if string[-1] != '0':
                    for i in range(1, len(string)):
                        res.append(string[:i] + '.' + string[i:])
        else:
            res.append(string)
        return res
            
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

