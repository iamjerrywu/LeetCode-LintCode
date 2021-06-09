# Connecting Graph 590 II \(M\)

## Problem

Given `n` nodes in a graph labeled from `1` to `n`. There is no edges in the graph at beginning.

You need to support the following method:

1. `connect(a, b)`, an edge to connect node a and node b
2. `query(a)`, Returns the number of connected component nodes which include node `a`.

Example

Example 1:

```text
Input:ConnectingGraph2(5)query(1)connect(1, 2)query(1)connect(2, 4)query(1)connect(1, 4)query(1)Output:[1,2,3,3]
```

Example 2:

```text
Input:ConnectingGraph2(6)query(1)query(2)query(1)query(5)query(1)Output:[1,1,1,1,1]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {i : i for i in range(1, n + 1)}
        self.size_of_set = {i : 1 for i in range(1, n + 1)}

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
    
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size_of_set[root_b] += self.size_of_set[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.size_of_set[self.find(a)]

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

