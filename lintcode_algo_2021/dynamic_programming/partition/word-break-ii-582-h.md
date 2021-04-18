# Word Break II 582 \(H\)

## Problem

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.Example

**Example 1:**

```text
Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
```

**Example 2:**

```text
Input："a"，[]
Output：[]
Explanation：dict is null.
```

## Solution - DFS + Memoization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        res = []
        if not s or not wordDict:
            return res
        max_len = max([len(word) for word in wordDict])
        self.dfs(s, 0, max_len, wordDict, {}, [], res)
        return res
 
    def dfs(self, s, index, max_len, word_set, memo, path, res):
        if index == len(s):
            res.append(" ".join(path))
            return
        #prunning
        if not self.is_possible(s, index, max_len, word_set, memo):
            return
        
        for i in range(index, len(s)):
            if i + 1 - index > max_len:
                break
            word = s[index: i + 1]
            if word not in word_set:
                continue
            path.append(word)
            self.dfs(s, index + len(word), max_len, word_set, memo, path, res)
            path.pop()
    # i.e:
    # input:aaaab
    # dict: ['a', 'aa', 'aaa', 'aaaa']
    # since last b is not in dict, no matter how the first n's a can be break, doesn't matter at all
    # therefore, need to record to avoid the same operation

    # however, in extreme case like
    # input: aaaa
    # dict: ['a', 'aa', 'aaa', 'aaaa']
    # still require 2^n times
    def is_possible(self, s, index, max_len, word_set, memo):
        if index in memo:
            return memo[index]
        if index == len(s):
            memo[index] = True
            return True
        memo[index] = False
        for i in range(index, len(s)):
            if i + 1 - index > max_len:
                break
            word = s[index : i + 1]
            if word not in word_set:
                continue
            if self.is_possible(s, i + 1, max_len, word_set, memo):
                memo[index] = True
                break
        return memo[index]

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

