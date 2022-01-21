# Palindrome Permutation (LeetCode 266) (E)

## Problem

Given a string `s`, return `true` if a permutation of the string could form a palindrome.

&#x20;

**Example 1:**

```
Input: s = "code"
Output: false
```

**Example 2:**

```
Input: s = "aab"
Output: true
```

**Example 3:**

```
Input: s = "carerac"
Output: true
```

&#x20;

**Constraints:**

* `1 <= s.length <= 5000`
* `s` consists of only lowercase English letters.



## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.Counter(s)
        
        odd_cnt = 0
        for k, v in count.items():
            if v%2:
                if odd_cnt > 0:
                    return False
                odd_cnt+=1
        return True
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Set

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        rec = set()
        odd_cnt = 0
        for c in s:
            if c in rec:
                rec.remove(c)
            else:
                rec.add(c)
        return len(rec) < 2
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
