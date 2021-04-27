# Topological Sorting 127 \(M\)

## Problem

Given an directed graph, a topological order of the graph nodes is defined as follow:

* For each directed edge `A -> B` in graph, A must before B in the order list.
* The first node in the order can be any node in the graph with no nodes direct to it.

Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.Have you met this question in a real interview?  YesProblem Correction

#### Clarification

[Learn more about representation of graphs](http://www.lintcode.com/help/graph)

#### Example

For graph as follow:

![&#x56FE;&#x7247;](https://media-cdn.jiuzhang.com/markdown/images/8/6/91cf07d2-b7ea-11e9-bb77-0242ac110002.jpg)

The topological order can be:

```text
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
```

#### Challenge

Can you do it in both BFS and DFS?

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_to_indegree = self.get_indegree(graph)
        
        # bfs
        order = []
        # for those nodes degree = 0
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
    
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor]+=1
        return node_to_indegree
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

