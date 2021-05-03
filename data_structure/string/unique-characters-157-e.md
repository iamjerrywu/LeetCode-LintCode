# Unique Characters 157 \(E\)

## Problem

Description

Implement an algorithm to determine if a string has all unique characters.Example

**Example 1:**

```text
Input: "abc_____"
Output: false
```

**Example 2:**

```text
Input:  "abc"
Output: true	
```

Challenge

What if you can not use extra space?

## Solution - Hash

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        if not str:
            return True
        
        ref = set()
        for c in str:
            if c in ref:
                return False
            ref.add(c)
        return True
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

## Solution - No Extra Memoery

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        for c in str:
            if str.count(c) != 1:
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

* **Time Complexity:**
* **Space Complexity:**

