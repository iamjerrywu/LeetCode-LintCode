# First Unique Character in a String 209 \(E\)

## Problem

Given a string and find the first unique character in a given string. You can assume that there is at least one unique character in the string.Example

```text
Example 1:
	Input: "abaccdeff"
	Output:  'b'
	
	Explanation:
	There is only one 'b' and it is the first one.


Example 2:
	Input: "aabccd"
	Output:  'b'
	
	Explanation:
	'b' is the first one.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        ref = {}
        for c in str:
            ref[c] = ref.get(c, 0) + 1
        
        for k in ref:
            if ref[k] == 1:
                return k
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

