# Longest String Chains 257 (M)

## Problem

You are given an array of `words` where each word consists of lowercase English letters.

`wordA` is a **predecessor** of `wordB` if and only if we can insert **exactly one** letter anywhere in `wordA` **without changing the order of the other characters** to make it equal to `wordB`.

* For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain** __ is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a **predecessor** of `word2`, `word2` is a **predecessor** of `word3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return _the **length** of the **longest possible word chain** with words chosen from the given list of_ `words`.

**Example 1:**

```
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
```

**Example 2:**

```
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
```

**Example 3:**

```
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
```

**Constraints:**

* `1 <= words.length <= 1000`
* `1 <= words[i].length <= 16`
* `words[i]` only consists of lowercase English letters.

## Solution - Graph Sol 1

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda w: len(w))
        graph = defaultdict(set)
        for i in range(n):
            word = words[i]
            for j in range(len(word)):
                graph[word[:j]+word[j+1:]].add(i)
        dists = [1] * n
        ans = 1
        for u in range(n):
            for v in graph[words[u]]:
                dists[v] = max(dists[v], dists[u]+1)
                ans = max(ans, dists[v])
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

## Solution - Graph Sol 2

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        edges = collections.defaultdict(list)
        n = len(words)
        scores = [0] * n
        pos = {}
        for i in range(n):
            pos[words[i]] = i
        
        for i in range(n):
            string = words[i]
            for j in range(len(string)):
                maybe = string[0:j] + string[j + 1:]
                if maybe not in pos:
                    continue
                edges[pos[maybe]].append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, self.longest(i, edges, scores))
        return ans
            

    def longest(self, val, edges, scores):
        if scores[val] > 0:
            return scores[val]
        scores[val] = 1
        for index in edges[val]:
            scores[val] = max(scores[val], self.longest(index, edges, scores) + 1)
        return scores[val]
        
                    
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
