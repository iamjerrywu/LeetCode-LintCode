# Reverse ASCII Encoded Strings 1781 \(E\)

## Problem

Given a string which encode by ascii \(For example, "ABC" can encode to "656667"\),You need to write a function that take an encoded string as input and returns reversed decoded string.

You can assume there is only **uppercase** letters in answer string.Example

**Example1**

```text
Input: "7976766972"
Output: "HELLO"
```

**Example2**

```text
Input: "656667"
Output: "CBA"
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param encodeString: an encode string
    @return: a reversed decoded string
    """
    def reverseAsciiEncodedString(self, encodeString):
        # Write your code here
        
        ans = ""
        for i in range(len(encodeString) -1, 0, -2):
            ascii_num = int(encodeString[i-1:i+1])
            ans+=chr(ascii_num)
        return ans
```
{% endtab %}

{% tab title="java" %}
```java
public class Solution {
    /**
     * @param encodeString: an encode string
     * @return: a reversed decoded string
     */
    public String reverseAsciiEncodedString(String encodeString) {
        // Write your code here
        StringBuilder ans = new StringBuilder();
        for ( int i = encodeString.length() - 1 ; i >=0 ; i = i -2) {
            String sub_str = encodeString.substring(i - 1, i + 1);
            int num = Integer.valueOf(sub_str);
            ans.append((char)num);
        }
        return ans.toString();
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

