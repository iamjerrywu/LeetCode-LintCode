# Valid Anagram 158 (E)

## Problem

Given two strings `s` and `t`, return `true` _if_ `t` _is an anagram of_ `s`_, and_ `false` _otherwise_.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

**Constraints:**

* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution - Sorting

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(nlogn)**
* **Space Complexity: O(n)**

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = collections.Counter(s)
        
        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c]-=1
        
        for num in counter.values():
            if num != 0:
                return False
        return True
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
