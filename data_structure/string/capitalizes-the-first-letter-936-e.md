# Capitalizes The First Letter 936 \(E\)

## Problem

Description

Given a sentence of English, update the first letter of each word to uppercase.

1. The given sentence may not be a grammatical sentence.
2. The length of the sentence does not exceed `100`.

Example

**Example1**

```text
Input: s =  "i want to get an accepted"
Output: "I Want To Get An Accepted"
```

**Example2**

```text
Input: s =  "i jidls    mdijf  i  lsidj  i p l   "
Output: "I Jidls    Mdijf  I  Lsidj  I P L   
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        sl = list(s)
        if sl[0] > 'a' and sl[0] < 'z':
            sl[0] = chr(ord(sl[0]) - 32)
        for i in range(1, len(sl)):
            if sl[i - 1] == ' ' and sl[i] != ' ':
                sl[i] = chr(ord(sl[i]) - 32)
        return ''.join(sl)

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

