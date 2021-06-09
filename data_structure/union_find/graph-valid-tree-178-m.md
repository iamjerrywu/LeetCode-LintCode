# Graph Valid Tree 178 \(M\)

## Problem

Given `n` nodes labeled from `0` to `n - 1` and a list of `undirected` edges \(each edge is a pair of nodes\), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.Example

**Example 1:**

```text
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]Output: true.
```

**Example 2:**

```text
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]Output: false.
```

## Solution - BFS

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

* **Time Complexity:**
* **Space Complexity:**

