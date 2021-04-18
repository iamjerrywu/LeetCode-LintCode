# Longest Common Prefix 78 \(M\)

## Problem

[https://www.lintcode.com/problem/78/](https://www.lintcode.com/problem/78/)

Given k strings, find the longest common prefix \(_LCP_\).Example

```text
Example 1:
	Input:  "ABCD", "ABEF", "ACEF"
	Output:  "A"
	

Example 2:
	Input: "ABCDEFG", "ABCEFG" and "ABCEFA"
	Output:  "ABC"
```

## Solution - Vertical Scan

Scan each word from start to end

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        res = ''
        if not strs:
            return res
        ref = strs[0]
        for start in range(len(ref)):
            for i in range(1, len(strs)):
                if start >= len(strs[i]) or ref[start] != strs[i][start]:
                    return res
            res+=ref[start]
        return res 
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(s\)**
  * s = length of total strs
* **Space Complexity: O\(1\)**

\*\*\*\*

## Solution - Horizontal Scan

Scan each word in full length comparing to first one, then scan the next word

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        # write your code here
        res = ''
        if not strs:
            return res
        res = strs[0]
        for i in range(1, len(strs)):
            for j in range(0, len(res)):
                if j >= len(strs[i]) or res[j] != strs[i][j]:
                    res = res[:j]
                    break
            # early break if res is already none
            if not res:
                return res
        return res         
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(s\)**
  * s = length of total strs
* **Space Complexity: O\(1\)**

\*\*\*\*

