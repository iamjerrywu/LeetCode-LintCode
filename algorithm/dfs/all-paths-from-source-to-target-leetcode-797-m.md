# All Paths From Source to Target (LeetCode 797) (M)

## Problem

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/28/all\_1.jpg)

<pre><code>Input: graph = [[1,2],[3],[3],[]]
<strong>Output:
</strong> [[0,1,3],[0,2,3]]
<strong>Explanation:
</strong> There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/28/all\_2.jpg)

<pre><code>Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>Output:
</strong> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]</code></pre>

&#x20;

**Constraints:**

* `n == graph.length`
* `2 <= n <= 15`
* `0 <= graph[i][j] < n`
* `graph[i][j] != i` (i.e., there will be no self-loops).
* All the elements of `graph[i]` are **unique**.
* The input graph is **guaranteed** to be a **DAG**.



## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        n = len(graph) - 1
        visited = set([0])
        self.dfs(0, graph, [0], ans, n, visited)
        return ans
    
    def dfs(self, node, graph, tmp, ans, n, visited):
        if node == n:
            ans.append(list(tmp))
            return 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                tmp.append(neighbor)
                self.dfs(neighbor, graph, tmp, ans, n, visited)
                tmp.pop()
                visited.remove(neighbor)
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
