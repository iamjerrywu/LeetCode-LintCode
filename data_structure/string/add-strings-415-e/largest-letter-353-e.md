# Largest letter 353 \(E\)

## Problem

Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S. The uppercase character should be returned. If there is no such character, return "NO".

* 1&lt;=len\(s\)&lt;=10^61&lt;=len\(s\)&lt;=106

Example

```text
Input: S = "admeDCAB"Output: "D"Input: S = "adme"Output: "NO"
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        # write your code here
        upp_low_diff = ord('a') - ord('A')
        ref = set()
        for c in s:
            ref.add(c)
        max_chr_val, max_chr = 0, ''
        for key in ref:
            key_val = ord(key)
            if chr(key_val + upp_low_diff) in ref and key_val > max_chr_val:
                max_chr_val = key_val
                max_chr = key
        return max_chr if max_chr != '' else 'NO'
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

