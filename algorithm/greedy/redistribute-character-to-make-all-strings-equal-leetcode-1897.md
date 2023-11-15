# Redistribute Character to Make All Strings Equal (LeetCode 1897)

## Problem

You are given an array of strings `words` (**0-indexed**).

In one operation, pick two **distinct** indices `i` and `j`, where `words[i]` is a non-empty string, and move **any** character from `words[i]` to **any** position in `words[j]`.

Return `true` _if you can make **every** string in_ `words` _**equal** using **any** number of operations_, _and_ `false` _otherwise_.

**Example 1:**

```
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
```

**Example 2:**

```
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
```

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 100`
* `words[i]` consists of lowercase English letters.

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ref = {}
        for word in words:
            for c in word:
                ref[c] = ref.get(c, 0) + 1
        length = len(words)
        for val in ref.values():
            if val%length != 0:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(sum(word)**
* **Space Complexity:**
