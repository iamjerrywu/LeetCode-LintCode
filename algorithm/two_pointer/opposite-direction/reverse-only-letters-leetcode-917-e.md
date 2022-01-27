# Reverse Only Letters (LeetCode 917) (E)

## Problem



Given a string `s`, reverse the string according to the following rules:

* All the characters that are not English letters remain in the same position.
* All the English letters (lowercase or uppercase) should be reversed.

Return `s` _after reversing it_.

&#x20;

**Example 1:**

```
Input: s = "ab-cd"
Output: "dc-ba"
```

**Example 2:**

```
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

**Example 3:**

```
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```

&#x20;

**Constraints:**

* `1 <= s.length <= 100`
* `s` consists of characters with ASCII values in the range `[33, 122]`.
* `s` does not contain `'\"'` or `'\\'`.

## Solution - Two Pointer

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < r and not s[l].isalpha():
                l+=1
            while l < r and not s[r].isalpha():
                r-=1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
        return "".join(s)
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

## Solution - Stack

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [c for c in s if c.isalpha()]
        ans = ""
        for c in s:
            if not c.isalpha():
                ans+=c
            else:
                ans+=stack.pop()
        return ans
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
