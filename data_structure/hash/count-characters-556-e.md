# Count Characters 557 \(E\)

## Problem



Count characters in a string. Return a hash map which key is character and value is the occurrency of this character.Example

Example 1:

```text
Input:
str = "abca"

Output:
{
  "a": 2,
  "b": 1,
  "c": 1
}

```

Example 2:

```text
Input:
str = "ab"

Output:
{
  "a": 1,
  "b": 1
}
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        res = {}
        for char in str:
            if char not in res:
                res[char] = 1
            else:
                res[char]+=1
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

