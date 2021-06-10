# Connecting Graph III 591 \(M\)

## Problem

Given `n` nodes in a graph labeled from `1` to `n`. There is no edges in the graph at beginning.

You need to support the following method:

1. `connect(a, b)`, an edge to connect node a and node b
2. `query()`, Returns the number of connected component in the graph

Example

Example 1:

```text
Input:ConnectingGraph3(5)query()connect(1, 2)query()connect(2, 4)query()connect(1, 4)query()Output:[5,4,3,3]
```

Example 2:

```text
Input:ConnectingGraph3(6)query()query()query()query()query()Output:[6,6,6,6,6]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        # initialize your data structure here.
        self.father = {i : i for i in range(1, n + 1)}
        self.num_of_set = n
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
            self.num_of_set-=1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.num_of_set
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

