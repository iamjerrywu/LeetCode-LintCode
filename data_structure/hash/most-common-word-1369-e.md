# Most Common Word 1369 \(E\)

## Problem

Given a string `paragraph` and a string array of the banned words `banned`, return _the most frequent word that is not banned_. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is **unique**.

The words in `paragraph` are **case-insensitive** and the answer should be returned in **lowercase**.

**Example 1:**

```text
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```

**Example 2:**

```text
Input: paragraph = "a.", banned = []
Output: "a"
```

**Constraints:**

* `1 <= paragraph.length <= 1000`
* paragraph consists of English letters, space `' '`, or one of the symbols: `"!?',;."`.
* `0 <= banned.length <= 100`
* `1 <= banned[i].length <= 10`
* `banned[i]` consists of only lowercase English letters.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
SKIP = {"!", "'", "?", ",", ";", ".", " "}
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # need to transfer to lower case
        banned_set = set([word.lower() for word in banned])
        
        words = {}
        ans = [0, '']
        tmp_str = ''
        for c in paragraph:
            if c not in SKIP:
                # need to transfer to lower case 
                tmp_str+=c.lower()
            else:
                if tmp_str:
                    ans = self.process(tmp_str, words, ans, banned_set)
                    tmp_str = ''
        # need to remember process the last string
        if tmp_str:
            ans = self.process(tmp_str, words, ans, banned_set)
        
        return ans[1]
    
    def process(self, string, words, ans, banned):
        words[string] = words.get(string, 0) + 1
        if string not in banned and words.get(string) > ans[0]:
            return [words.get(string), string]
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

