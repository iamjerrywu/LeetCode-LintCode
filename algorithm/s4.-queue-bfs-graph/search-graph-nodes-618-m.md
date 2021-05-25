# Search Graph Nodes 618 \(M\)

## Problem

Given a `undirected graph`, a `node` and a `target`, return the nearest node to given node which value of it is target, return `NULL` if you can't find.

There is a `mapping` store the nodes' values in the given parameters.

It's guaranteed there is only one available solutionExample

Example 1:

```text
Input:{1,2,3,4#2,1,3#3,1,2#4,1,5#5,4}[3,4,5,50,50]150Output:4Explanation:2------3  5 \     |  |   \    |  |   \   |  |    \  |  |      1 --4Give a node 1, target is 50there a hash named values which is [3,4,10,50,50], represent:Value of node 1 is 3Value of node 2 is 4Value of node 3 is 10Value of node 4 is 50Value of node 5 is 50Return node 4
```

Example 2:

```text
Input:{1,2#2,1}[0,1]11Output:2
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        if len(graph) == 0 or len(values) == 0:
            return None
        
        visited = set([node])
        queue = collections.deque([node])
        
        while queue:
            cur_node = queue.popleft()
            if values[cur_node] == target:
                return cur_node
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return None
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

