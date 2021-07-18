# Maximum Number of Words You Can Type 1935 \(E\)

## Problem

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space \(no leading or trailing spaces\) and a string `brokenLetters` of all **distinct** letter keys that are broken, return _the **number of words** in_ `text` _you can fully type using this keyboard_.

**Example 1:**

```text
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
```

**Example 2:**

```text
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
```

**Example 3:**

```text
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
```

**Constraints:**

* `1 <= text.length <= 104`
* `0 <= brokenLetters.length <= 26`
* `text` consists of words separated by a single space without any leading or trailing spaces.
* Each word only consists of lowercase English letters.
* `brokenLetters` consists of **distinct** lowercase English letters.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set()
        for c in brokenLetters:
            broken.add(c)
        
        words = text.split(' ')
        res = 0
        for word in words:
            add = True
            for c in word:
                if c in broken:
                    add = False
                    break
            if add:
                res+=1
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

