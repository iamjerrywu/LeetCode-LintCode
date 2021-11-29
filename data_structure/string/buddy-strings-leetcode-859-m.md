# Buddy Strings (LeetCode 859) (M)

## Problem

****

Given two strings `s` and `goal`, return `true` _if you can swap two letters in_ `s` _so the result is equal to_ `goal`_, otherwise, return_ `false`_._

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

* For example, swapping at indices `0` and `2` in `"abcd"` results in `"cbad"`.

&#x20;

**Example 1:**

```
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
```

**Example 2:**

```
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
```

**Example 3:**

```
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
```

**Example 4:**

```
Input: s = "aaaaaaabc", goal = "aaaaaaacb"
Output: true
```

&#x20;

**Constraints:**

* `1 <= s.length, goal.length <= 2 * 104`
* `s` and `goal` consist of lowercase letters.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            seen = set()
            for c in s:
                if c in seen:
                    return True
                seen.add(c)
            return False
        
        pairs = []
        
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                pairs.append((c1, c2))
            if len(pairs) >= 3:
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
                
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
