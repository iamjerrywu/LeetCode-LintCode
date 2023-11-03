# Ransom Note (LeetCode 383)

## Problem

Given two strings `ransomNote` and `magazine`, return `true` _if_ `ransomNote` _can be constructed by using the letters from_ `magazine` _and_ `false` _otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

&#x20;

**Example 1:**

<pre><code><strong>Input: ransomNote = "a", magazine = "b"
</strong><strong>Output: false
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: ransomNote = "aa", magazine = "ab"
</strong><strong>Output: false
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: ransomNote = "aa", magazine = "aab"
</strong><strong>Output: true
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= ransomNote.length, magazine.length <= 105`
* `ransomNote` and `magazine` consist of lowercase English letters.



## Solution

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> appears;
        for (char c : magazine) {
            appears[c]+=1;
        }

        for (char c : ransomNote) {
            if (appears.count(c)) {
                appears[c]-=1;
                if (appears[c] == 0) {
                    appears.erase(c);
                }
            } else {
                return false;
            }
        }
        return true;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

