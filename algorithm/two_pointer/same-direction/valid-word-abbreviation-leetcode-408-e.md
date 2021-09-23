# Valid Word Abbreviation \(LeetCode 408\) \(E\)

## Problem

A string can be **abbreviated** by replacing any number of **non-adjacent** substrings with their lengths. For example, a string such as `"substitution"` could be abbreviated as \(but not limited to\):

* `"s10n"` \(`"s ubstitutio n"`\)
* `"sub4u4"` \(`"sub stit u tion"`\)
* `"12"` \(`"substitution"`\)
* `"su3i1u2on"` \(`"su bst i t u ti on"`\)
* `"substitution"` \(no substrings replaced\)
* `"s010n"` \(leading zeros in numbers are **NOT** allowed\)

Note that `"s55n"` \(`"s ubsti tutio n"`\) is not a valid abbreviation of `"substitution"` because the replaced substrings are adjacent.

Given a string `word` and an abbreviation `abbr`, return _whether the string **matches** with the given abbreviation_.

**Example 1:**

```text
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
```

**Example 2:**

```text
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
```

**Constraints:**

* `1 <= word.length <= 20`
* `word` consists of only lowercase English letters.
* `1 <= abbr.length <= 10`
* `abbr` consists of lowercase English letters and digits.
* All the integers in `abbr` will fit in a 32-bit integer.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_p, a_p = 0, 0
        
        while w_p < len(word) and a_p < len(abbr):
            if abbr[a_p].isalpha():
                if word[w_p] != abbr[a_p]:
                    return False
                else:
                    w_p+=1
                    a_p+=1
            else:
                num = 0
                while a_p < len(abbr) and abbr[a_p].isdigit():
                    if 0 <= int(abbr[a_p]) < 10:
                        #leading zeros
                        if num == 0 and int(abbr[a_p]) == 0:
                            return False
                        num = num * 10 + int(abbr[a_p])
                    a_p+=1
                while num:
                    if w_p < len(word):
                        w_p+=1
                        num-=1
                    else:
                        return False
        return w_p == len(word) and a_p == len(abbr)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O\(max\(m, n\)\)**
* **Space Complexity: O\(1\)**

