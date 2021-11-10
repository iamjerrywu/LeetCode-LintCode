# Reverse Words in a String 53 (E)

## Problem

Given an input string, reverse the string word by word.

* What constitutes a word?\
  A sequence of non-space characters constitutes a word and some words have punctuation at the end.
* Could the input string contain leading or trailing spaces?\
  Yes. However, your reversed string should not contain leading or trailing spaces.
* How about multiple spaces between two words?\
  Reduce them to a single space in the reversed string.

Example

**Example 1:**

Input:

```
s = "the sky is blue"
```

Output:

```
"blue is sky the"
```

Explanation:

return a reverse the string word by word.\
**Example 2:**

Input:

```
s = "hello world"
```

Output:

```
"world hello"
```

Explanation:

return a reverse the string word by word.

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if not s:
            return s

        str_list = s.split()
        ans = " "
        return ans.join(str_list[::-1])
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
