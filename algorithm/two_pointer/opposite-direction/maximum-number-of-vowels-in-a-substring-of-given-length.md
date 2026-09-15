# Maximum Number of Vowels in a Substring of Given Length

## Problem

Given a string `s` and an integer `k`, return _the maximum number of vowel letters in any substring of_ `s` _with length_ `k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

&#x20;

**Example 1:**

<pre><code><strong>Input: s = "abciiidef", k = 3
</strong><strong>Output: 3
</strong><strong>Explanation: The substring "iii" contains 3 vowel letters.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "aeiou", k = 2
</strong><strong>Output: 2
</strong><strong>Explanation: Any substring of length 2 contains 2 vowels.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: s = "leetcode", k = 3
</strong><strong>Output: 2
</strong><strong>Explanation: "lee", "eet" and "ode" contain 2 vowels.
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 10`<sup>`5`</sup>
* `s` consists of lowercase English letters.
* `1 <= k <= s.length`



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
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return (c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u');
        };
        // sliding window
        int l = 0;
        int ans = 0, cnt = 0;
        for (int r = 0; r < s.length(); r++) {
            if (isVowel(s[r])) cnt++;
            if (r >= k) {
                if (isVowel(s[l])) {
                    cnt--;
                }
                l++;
            }

            ans = max(ans, cnt);
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

