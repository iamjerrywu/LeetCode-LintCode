# Word Ladder 120 \(H\)

## Problem

Given two words \(_start_ and _end_\), and a dictionary, find the shortest transformation sequence from _start_ to _end_, output the length of the sequence.  
Transformation rule such that:

1. Only one letter can be changed at a time
2. Each intermediate word must exist in the dictionary. \(Start and end words do not need to appear in the dictionary \)

* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the dictionary.
* You may assume beginWord and endWord are non-empty and are not the same.

Example

**Example 1:**

```text
Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"
```

**Example 2:**

```text
Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"
```

## Solution - Double Direction BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1
        
        dict.add(start)
        dict.add(end)
        graph = self.construct_graph(dict)

        forward_queue = collections.deque([start])
        forward_set = set([start])
        backward_queue = collections.deque([end])
        backward_set = set([end])
        
        distance = 1
        while forward_queue and backward_queue:
            distance +=1
            if self.extend_queue(graph, forward_queue, forward_set, backward_set):
                return distance
            distance +=1
            if self.extend_queue(graph, backward_queue, backward_set, forward_set):
                return distance 
        return -1
    
    def extend_queue(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            word = queue.popleft()
            for next_word in graph[word]:
                if next_word in visited:
                    continue
                if next_word in opposite_visited:
                    return True
                queue.append(next_word)
                visited.add(next_word)
        return False

    def construct_graph(self, dict):
        graph = {}
        for word in dict:
            graph[word] = self.get_next_words(word, dict)
        return graph
    
    def get_next_words(self, word, dict):
        next_word_set = set()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    next_word_set.add(next_word)
        return next_word_set
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

