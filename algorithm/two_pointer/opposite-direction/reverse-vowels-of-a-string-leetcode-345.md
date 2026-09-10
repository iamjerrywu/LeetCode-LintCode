# Reverse Vowels of a String (LeetCode 345)

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

&#x20;

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

&#x20;

**Constraints:**

* `1 <= s.length <= 3 * 10`<sup>`5`</sup>
* `s` consist of **printable ASCII** characters.



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
    string reverseVowels(string s) {
        
        // lambda function
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || 
                   c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
        };

        int l = 0, r = s.length() - 1;
        
        bool isLeftVowel, isRightVowel;
        while (l < r) {
            isLeftVowel = isVowel(s[l]);
            isRightVowel = isVowel(s[r]);

            if (isLeftVowel && isRightVowel) {
                // swap uses references to find the objects in memory and swaps their underlying values
                swap(s[l], s[r]);
                l++;
                r--;
            } else {
                if (!isLeftVowel) l++;
                if (!isRightVowel) r--;
            }
        }
        return s;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
