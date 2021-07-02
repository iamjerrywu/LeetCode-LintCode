# String Partition 328 \(M\)

## Problem

Given a string with all characters in uppercase, please divide the string into as many parts as possible so that each letter appears in only one part. Return an array containing the length of each part.

S.length \leq 1000S.length≤1000Example

**Example 1:**

```text
Input:"MPMPCPMCMDEFEGDEHINHKLIN"Output:[9,7,8]Explanation:"MPMPCPMCM""DEFEGDE""HINHKLIN"
```

## Solution - Two Pointer

```python
class Solution:
    """
    @param s: a string
    @return:  an array containing the length of each part
    """
    def splitString(self, s):
        # write your code here.
        last_pos = {}
        # find the last position for every s[i]
        for i in range(len(s)):
            last_pos[s[i]] = i
        
        i, j, res = 0, 0, []
        while i < len(s):
            start = i
            j = last_pos[s[i]]
            while j < len(s) and i < j:
                # since last pos[s[i]] might M j, should check
                j = max(j, last_pos[s[i]])
                i+=1
            res.append(j - start + 1)
            i+=1
        return res
```

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(m\)**
  * m: the instinct alphabets, max as 26



