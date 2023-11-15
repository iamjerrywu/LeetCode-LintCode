# Rotate String (LeetCode796) (E)

## Problem

Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` _after some number of **shifts** on_ `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

* For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

&#x20;

**Example 1:**

```
Input: s = "abcde", goal = "cdeab"
Output: true
```

**Example 2:**

```
Input: s = "abcde", goal = "abced"
Output: false
```

&#x20;

**Constraints:**

* `1 <= s.length, goal.length <= 100`
* `s` and `goal` consist of lowercase English letters.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            # approach 1
            if self.check(s, goal, i):
             
             # approach 2
             # if s[i:] + s[:i] == goal:
                return True
        return False
    
    def check(self, s, goal, mid):
        # right
        for i in range(mid, len(goal)):
            if s[i] != goal[i - mid]:
                return False
            
        # left
        for i in range(mid):
            if s[i] != goal[i + (len(goal) - mid)]:
                return False
        return True
```
{% endtab %}

{% tab title="Java" %}
```java
class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length())
            return false;
        
        for (int i = 0; i < s.length(); i++) {
            if ((s.substring(i, s.length()) + s.substring(0,i)).equals(goal)) 
                return true;
        }
        return false;
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

