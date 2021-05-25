# Connected Component in Undirected Graph 431 \(M\)

## Problem

Find connected component in undirected graph.

Each node in the graph contains a label and a list of its neighbors.

\(A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.\)

You need return a list of label set.

Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order. [Learn more about representation of graphs](http://www.lintcode.com/help/graph)Example

**Example 1:**

```text
Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}Output: [[1,2,4],[3,5]]Explanation:  1------2  3   \     |  |     \    |  |     \   |  |      \  |  |        4   5
```

**Example 2:**

```text
Input: {1,2#2,1}Output: [[1,2]]Explanation:  1--2
```

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if len(nodes) == 0:
            return []
        
        visited = set()
        ans = []
        for node in nodes:
            if node in visited:
                continue
            
            res = []
            queue = collections.deque([node])
            visited.add(node)
            while queue:
                cur_node = queue.popleft()
                res.append(cur_node.label)
                for neighbor in cur_node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            res.sort()
            ans.append(res)
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Union Find

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

