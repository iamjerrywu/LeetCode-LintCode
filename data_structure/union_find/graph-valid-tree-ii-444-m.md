# Graph Valid Tree II 444 \(M\)

## Problem



Please design a data structure which can do the following operations:

* `void addEdge(int a, int b)`:add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
* `bool isValidTree()`: Check whether these edges make up a valid tree.

Example

**Example 1**

```text
Input:addEdge(1, 2)isValidTree()addEdge(1, 3)isValidTree()addEdge(1, 5)isValidTree()addEdge(3, 5)isValidTree()Output: ["true","true","true","false"]
```

## Solution 

If this problem is solved using BFS, then the time complexity would be too large.

* If called `isValidTree()` m times, then time complexity would be O\(m \* \(N + E\)\)

Therefore, should use UnionFind in this case

### Code - Union Find

{% tabs %}
{% tab title="python" %}
```python
class UnionFind:
    def __init__(self):
        # father pointer
        self.father = {}
    def add(self, x):
        # if node alreay exist
        if x in self.father:
            return 
        self.father[x] = None
    def find(self, x):
        # root point to x
        # and recursively traverse back to find it's father 
        root = x
        while self.father[root]:
            root = self.father[root]
        return root
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        
        # if they are not in the same component, let root_x point to root_y
        if root_x != root_y:
            self.father[x] = root_y
    # is_connected can check on following condition
    # 1. two nodes in same set?
    # 2. two nodes belongs to same component?
    # 3. two nodes are connected?
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    """
    @param a: the node a
    @param b: the node b
    @return: nothing
    """
    def __init__(self):
        self.uf = UnionFind()
        self.has_cycle = False
        self.edges = 0
    
    def addEdge(self, a, b):
        # write your code here
        self.uf.add(a)
        self.uf.add(b)
        self.edges+=1
        if self.uf.is_connected(a, b):
            self.has_cycle = True
        #because it's adding edge, a, b should connected
        self.uf.merge(a, b) 

    """
    @return: check whether these edges make up a valid tree
    """
    def isValidTree(self):
        # write your code here
        if len(self.uf.father) != self.edges + 1:
            return False
        return not self.has_cycle
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * addEdge\(\): O\(n\)
    * In worst case, the nodes act as list with length n
  * isValidTree: O\(1\)
* **Space Complexity:**

## Solution 

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

