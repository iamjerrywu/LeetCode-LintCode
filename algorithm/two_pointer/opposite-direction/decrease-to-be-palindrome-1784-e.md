# Decrease To Be Palindrome 1784 \(E\)

## Problem

Given a string `s` with a-z. We want to change `s` into a palindrome with following operations:

```text
1. change 'z' to 'y';
2. change 'y' to 'x';
3. change 'x' to 'w';
................
24. change 'c' to 'b';
25. change 'b' to 'a';
```

Returns the number of operations needed to change `s` to a palindrome at least.Example

**Example 1:**

```text
Input: "abc"
Output: 2
Explanation: 
  1. Change 'c' to 'b': "abb"
  2. Change the last 'b' to 'a': "aba"
```

**Example 2:**

```text
Input: "abcd"
Output: 4
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        if s is None:
            return 0
        minStep = 0
        left, right = 0, len(s)-1
        while left < right:
            # 'a' 'c'
            minStep+= abs(ord(s[left]) - ord(s[right]))
            left+=1
            right-=1
        return minStep
```
{% endtab %}

{% tab title="java" %}
```java
public class Solution {
    /**
     * @param s: the string s
     * @return: the number of operations at least
     */
    public int numberOfOperations(String s) {
        // Write your code here
        if (s == null) {
            return 0;
        }
        
        int minStep = 0;
        int left = 0;
        int right = s.length() -1;
        
        while(left < right) {
            minStep+= Math.abs((int)s.charAt(left) - (int)s.charAt(right));
            left++;
            right--;
        }
        return minStep;
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

