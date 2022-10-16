# Concatenated Words (LeetCode 472) (H)

## Problem

****

Given an array of strings `words` (**without duplicates**), return _all the **concatenated words** in the given list of_ `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words in the given array.

&#x20;

**Example 1:**

<pre><code>Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
<strong>Output:
</strong> ["catsdogcats","dogcatsdog","ratcatdogcat"]
<strong>Explanation:
</strong> "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".</code></pre>

**Example 2:**

<pre><code>Input: words = ["cat","dog","catdog"]
<strong>Output:
</strong> ["catdog"]</code></pre>

&#x20;

**Constraints:**

* `1 <= words.length <= 104`
* `1 <= words[i].length <= 30`
* `words[i]` consists of only lowercase English letters.
* All the strings of `words` are **unique**.
* `1 <= sum(words[i].length) <= 105`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        ans = []
        for word in words:
            memo = dict()
            if self.dfs(0, 0, word, word_set, memo):
                ans.append(word)
        return ans
    
    def dfs(self, idx, cnt, word, word_set, memo):
        if idx in memo:
            return memo[idx]
        if idx == len(word) and cnt > 1:
            return True
        
        for i in range(idx, len(word) + 1):
            sub_str = word[idx:i]
            if sub_str in word_set:
                if self.dfs(i, cnt + 1, word, word_set, memo):
                    return True
        memo[idx] = False
        return False
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
