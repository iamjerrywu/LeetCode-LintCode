# Name Deduplication 487 \(E\)

## Problem

Given a list of names, remove the duplicate names. Two name will be treated as the same name if they are equal ignore the case.

Return a list of names without duplication, all names should be in lowercase, and keep the order in the original list.

You can assume that the name contains only uppercase and lowercase letters and spaces.Example

Example 1:

```text
Input:["James", "james", "Bill Gates", "bill Gates", "Hello World", "HELLO WORLD", "Helloworld"]


Output:["james", "bill gates", "hello world", "helloworld"]
```

Example 2:

```text
Input:["cmy","Cmy"]

Output:["cmy"]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        
        d = {}
        res = []
        for name in names:
            name = name.lower()
            if name not in d:
                d[name] = 1
                res.append(name)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

