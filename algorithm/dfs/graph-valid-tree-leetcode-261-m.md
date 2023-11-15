# Graph Valid Tree (LeetCode 261) (M)

## Problem

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` _if the edges of the given graph make up a valid tree, and_ `false` _otherwise_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

&#x20;

**Constraints:**

* `1 <= n <= 2000`
* `0 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai, bi < n`
* `ai != bi`
* There are no self-loops or repeated edges.



## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set([0])
        
        self.dfs(0, graph, visited)
        return len(visited) == n
    
    def dfs(self, index, graph, visited):
        for neighbor in graph[index]:    
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, graph, visited)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**



## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set([0])
        
        queue = collections.deque([0])
        cnt = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                cnt+=1
                visited.add(neighbor)
                queue.append(neighbor)
        return cnt == n - 1
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

