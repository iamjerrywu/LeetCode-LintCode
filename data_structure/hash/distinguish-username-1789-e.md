# Distinguish Username 1789 \(E\)

## Problem

Give a group of user names. If there are duplicate user names, add a number after the user name to distinguish them, and return the modified array.Example

**Example 1:**

```text
Input：["aa", "bb", "cc", "bb", "aa", "aa", "aa"]
Output：["aa","bb","cc","bb1","aa1","aa2","aa3"]
Explanation：
The output of the second occurrence of "bb" is "bb1"
The output of the second occurrence of "aa" is "aa1"
The output of the third occurrence of "aa" is "aa2"
The output of the fourth occurrence of "aa" is "aa3"
```

**Example 2:**

```text
Input：[aa, bb, cc, aa]
Output：[aa, bb, cc, aa1]
Explanation：The output of the second occurrence of "aa" is "aa1"
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param names: a string array
    @return: the string array
    """
    def DistinguishUsername(self, names):
        # Write your code here
        ref = {}
        for i in range(len(names)):
            if names[i] in ref:
                ref[names[i]] = ref.get(names[i], 0) + 1
                names[i]+=str(ref[names[i]])
            ref[names[i]] = 0
        return names
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

