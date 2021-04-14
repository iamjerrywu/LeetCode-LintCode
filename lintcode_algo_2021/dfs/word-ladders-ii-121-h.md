# Word Ladders II 121 \(H\)

## Problem

Given two words \(_start_ and _end_\), and a dictionary, find all shortest transformation sequence\(s\) from _start_ to _end_.  
Transformation rule such that:

1. Only one letter can be changed at a time
2. Each intermediate word must exist in the dictionary

* All words have the same length.
* All words contain only lowercase alphabetic characters.
* At least one solution exists.

Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```text
Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：[["a","c"]]
Explanation：
"a"->"c"
```

**Example 2:**

```text
Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation：
1."hit"->"hot"->"dot"->"dog"->"cog"
2."hit"->"hot"->"lot"->"log"->"cog"
```

## Solution

This problem cannot be done by either BFS or DFS individually, since both would have too large time complexity. 

Need to combine BFS and DFS together. First construct the all valid graph from BFS, then do the DFS in these graph to find out the valid path that would reach target word

### Code

{% tabs %}
{% tab title="python" %}
```python
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        distance = {}

        self.bfs(end, distance, dict)

        results = []
        self.dfs(start, end, distance, dict, [start], results)

        return results
    
    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                # must be the word that haven't visited
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                # since next word might be current word, should eliminate, and should also in the dictionary
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
    
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            # need to hard copy the path answer (since might be mulitple possible answers)
            results.append(list(path))
            return 
        
        for word in self.get_next_words(curt, dict):
            # if the word is not curt next word
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()

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

