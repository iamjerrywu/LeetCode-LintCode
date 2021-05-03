# Palindrome Data Stream 958 \(E\)

## Problem

Description

There is a data stream coming in, one lowercase letter at a time. Can the **arrangement** of the current data stream form palindrome string？

* `1 <= |s| <= 10^5`

Example

**Example 1:**

```text
input:s = ['a','a','a','a','a']
outut:[1,1,1,1,1]
Explanation:
“a” can form a palindrome
“aa” can form a palindrome
“aaa” can form a palindrome
“aaaa” can form a palindrome
“aaaaa” can form a palindrome
```

**Example 2:**

```text
input:s = ['a','b','a']
outut:[1,0,1]
Explanation:
“a” can form a palindrome
“ab” can't form a palindrome
“aba” can form a palindrome
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        # Write your code here
        # the odd number of appearance of each alphabat should <= 1
        if s is None:
            return []
            
        alphabat = [0] * 26
        #0 -> 'a', 1 -> 'b' ....25 -> 'z'
        count = 0
        answer = []
        for i in range(len(s)):
            alphabat[ord(s[i]) - ord('a')]+=1
            if alphabat[ord(s[i]) - ord('a')] %2 == 1:
                count += 1
            else:
                count -= 1
            if count > 1:
                answer.append(0)
            else:
                answer.append(1)
        return answer
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

