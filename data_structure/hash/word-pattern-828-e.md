---
description: Uber
---

# Word Pattern 828 \(E\)

## Problem

Given a `pattern` and a string `str`, find if `str` follows the same pattern.  
Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.

You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters separated by a single space.Example

**Example1**

```text
Input:  pattern = "abba" and str = "dog cat cat dog"
Output: true
Explanation:
The pattern of str is abba
```

**Example2**

```text
Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc
```

**Example3**

```text
Input:  pattern = "aaaa" and str = "dog cat cat dog"
Output: false
Explanation:
The pattern of str is abba
```

**Example4**

```text
Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc
```

## Solution - HashMap + HashSet

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        test_strings = teststr.split(" ")
        if len(pattern) != len(test_strings):
            return False

        ref, appeared = {}, set()
        for i in range(len(pattern)):
            if pattern[i] not in ref:
                if test_strings[i] not in appeared:
                    appeared.add(test_strings[i])
                else:
                    return False
                ref[pattern[i]] = test_strings[i]
            elif ref[pattern[i]] != test_strings[i]:
                return False
        return True
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

