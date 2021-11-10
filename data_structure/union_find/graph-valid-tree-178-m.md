# Graph Valid Tree 178 (M)

## Problem

Given `n` nodes labeled from `0` to `n - 1` and a list of `undirected` edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.Example

**Example 1:**

```
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]Output: true.
```

**Example 2:**

```
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]Output: false.
```

## Solution - BFS

If a graph is a valid tree, then it should comply following attributes:

1. N nodes with (N - 1) Edges
2. No circle in the graph&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-06-09 at 11.08.20 AM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n -1:
            return False

        # construct graph
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        # BFS
        visited = set()
        queue = collections.deque()
        queue.append(0)
        visited.add(0)
        while queue:
            cur = queue.popleft()
            for neighbor in neighbors[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return len(visited) == n
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(N + E)**
  * N: nodes amount / E: Edges amount
  * Construct Graph: O(E)
  * BFS traverse:
    * O(N + E)
* **Space Complexity: **
  * Graph: O(N + E)
  * BFS O(N):
    * The queue would have worst case of length N

## Solution - Union Find

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0 or len(edges) != n - 1:
            return False
        
        self.father = {i: None for i in range(n)}
        self.size = n
        
        for src, dst in edges:
            self.union(src, dst)
        print(self.size)
        return self.size == 1        

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.size-=1
            self.father[root_x] = root_y
    
    def find(self, node):
        root = node
        while self.father[root]:
            root = self.father[root]
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * Length of the graph (worst case as a list)
* **Space Complexity: O(n)**

## Solution - Union Find with Path Compression

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0 or len(edges) != n - 1:
            return False
        
        self.father = {i: None for i in range(n)}
        self.size = n
        
        for src, dst in edges:
            self.union(src, dst)
        print(self.size)
        return self.size == 1        

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.size-=1
            self.father[root_x] = root_y
        
    def find(self, node):
        root = node
        while self.father[root]:
            root = self.father[root]
        while node != root:
            original_father = self.father[node]
            self.father[node] = root
            node = original_father
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(log\*n)**
* **Space Complexity: O(n)**
