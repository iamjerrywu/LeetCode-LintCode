# Longest String Chains 257 \(M\)

## Problem



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

* **Time Complexity:** 
* **Space Complexity:**

\*\*\*\*

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

* **Time Complexity:** 
* **Space Complexity:**

