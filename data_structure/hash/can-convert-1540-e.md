# Can Convert 1540 \(E\)

## Problem

Given two string `S` and `T`, determine if `S` can be changed to `T` by deleting some letters \(including 0 letter\)Example

**Example1**

```text
Input: S = "lintcode" and T = "lint"
Output: true
```

**Example2**

```text
Input: S = "lintcode" and T = "ide"
Output: true
```

**Example3**

```text
Input: S = "adda" and T = "aad"
Output: false
Explanation: You can not change "adda" to "aad" by deleting one 'd'.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        i = 0
        for c in s:
            if c == t[i]:
                i+=1
            if i == len(t):
                return True
        return False

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

