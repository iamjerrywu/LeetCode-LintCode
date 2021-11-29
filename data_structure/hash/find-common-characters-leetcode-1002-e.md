# Find Common Characters (LeetCode 1002) (E)

## Problem

Given a string array `words`, return _an array of all characters that show up in all strings within the_ `words` _(including duplicates)_. You may return the answer in **any order**.

&#x20;

**Example 1:**

```
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
```

**Example 2:**

```
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
```

&#x20;

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 100`
* `words[i]` consists of lowercase English letters.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = collections.Counter(words[0])
        
        for i in range(1, len(words)):
            for c in common.keys():
                common[c] = min(common[c], words[i].count(c))
        ans = ""
        for c, cnt in common.items():
            ans+=c * cnt
        return ans
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
