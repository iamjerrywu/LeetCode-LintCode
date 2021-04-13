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
        if not strs:
            return ''
        res, start = '', 0
        while start < len(strs[0]):
            ref = strs[0][start]
            for i in range(1, len(strs)):
                if start >= len(strs[i]) or ref != strs[i][start]:
                    return res
            res+=strs[0][start]
            start+=1
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
        if not strs:
            return ''
        res, start = '', 0
        while start < len(strs[0]):
            ref = strs[0][start]
            for i in range(1, len(strs)):
                if start >= len(strs[i]) or ref != strs[i][start]:
                    return res
            res+=strs[0][start]
            start+=1
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

