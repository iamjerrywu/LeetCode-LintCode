# Connecting Graph 589 \(M\)

## Problem

Given `n` nodes in a graph labeled from `1` to `n`. There is no edges in the graph at beginning.

You need to support the following method:

1. `connect(a, b)`, add an edge to connect node `a` and node b\`.
2. `query(a, b)`, check if two nodes are connected

Example

Example 1:

```text
Input:ConnectingGraph(5)query(1, 2)connect(1, 2)query(1, 3) connect(2, 4)query(1, 4) Output:[false,false,true]
```

Example 2:

```text
Input:ConnectingGraph(6)query(1, 2)query(2, 3)query(1, 3)query(5, 6)query(1, 4)Output:[false,false,false,false,false]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {i : i for i in range(1, n + 1)}

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    
    def find(self, node):
        root = node
        while self.father[root] != root:
            root = self.father[root]
        
        # path compression
        while root != node:
            original_father = self.father[node]
            self.father[node] = root
            node = original_father
        return root
    
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
  * Connect: O\(1\)
  * Query: O\(1\)
* **Space Complexity: O\(n\)**

