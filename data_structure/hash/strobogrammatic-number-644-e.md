# Strobogrammatic Number 644 \(E\)

## Problem

A mirror number is a number that looks the same when rotated 180 degrees \(looked at upside down\).For example, the numbers "69", "88", and "818" are all mirror numbers.

Write a function to determine if a number is mirror. The number is represented as a string.Example

**Example 1:**

```text
Input : "69"
Output : true
```

**Example 2:**

```text
Input : "68"
Output : false
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        ref = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        i = 0
        j = len(num) -1
        while(i <= j):
            if num[i] not in ref or num[j] != ref[num[i]]:
                return False
            i+=1
            j-=1
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

