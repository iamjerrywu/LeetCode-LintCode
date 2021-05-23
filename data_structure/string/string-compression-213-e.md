# String Compression 213 \(E\)

## Problem

mplement a method to perform basic string compression using the counts of repeated characters. For example, the string `aabcccccaaa` would become `a2b1c5a3`.

If the "compressed" string would not become smaller than the original string, your method should return the original string.

You can assume the string has only upper and lower case letters \(a-z\).Example

**Example 1:**

```text
Input: str = "aabcccccaaa"Output: "a2b1c5a3"
```

**Example 2:**

```text
Input: str = "aabbcc"Output: "aabbcc"

```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if not originalString:
            return originalString
        compress_str = ''
        cnt,  cur_char = 0, originalString[0]
        for i in range(len(originalString)):
            if i == 0 or originalString[i - 1] == originalString[i]:
                cnt+=1
            else:
                compress_str+=cur_char + str(cnt)
                cur_char = originalString[i]
                cnt = 1
        # for the last one, have to concatenate as well
        compress_str+=cur_char + str(cnt)
        
        return compress_str if len(compress_str) < len(originalString) else originalString
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(m\)**
  * m: the amount of inorder group of characters
  * Stack: string use m times
  * Heap: no heap used

