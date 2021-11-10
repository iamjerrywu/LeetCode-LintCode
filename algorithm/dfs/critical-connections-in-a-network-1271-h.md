# Critical Connections in a Network 1271 (H)

## Problem

There are `n` servers numbered from `0` to `n-1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a, b]` represents a connection between servers `a` and `b`. Any server can reach any other server directly or indirectly through the network.

A _critical connection_ is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order, but **you should guarantee that for each connections, when you return, index1 is less than index 2. For instance, if the answer is \[\[1,2],\[3,4]] you can return \[\[3,4],\[1,2]], but \[\[2,1],\[3,4]] is invaild.**

* `1 <= n <= 10^5`
* `n-1 <= connections.length <= 10^5`
* `connections[i][0] != connections[i][1]`
* There are no repeated connections.

In Java, because of low stack, when you get 57% passed and then RE, you can think that you have passed the problem.Example

```
Input:4[[0,1],[1,2],[2,0],[1,3]]Output: [[1,3]]
```

Explanation:\
![图片](https://media-test.jiuzhang.com/media/markdown/images/3/30/734d12e2-7278-11ea-9c38-0242ac1a0004.jpg)

## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-06-23 at 1.42.19 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: the number of servers
    @param connections: connections
    @return: Critical Connections in a Network
    """
    def criticalConnectionsinaNetwork(self, n, connections):
        # write your code here
        graph = self.get_graph(connections)
        ans = set(map(tuple, map(sorted, connections)))
        # equals to following code:
        # for i in range(len(connections)):
        #     connections[i] = tuple(sorted(connections[i]))
        # ans = set(connections)
        rank = [-sys.maxsize] * n
        self.dfs(0, 0, rank, graph, ans, n)
        return list(ans)
    
    def dfs(self, node, depth, rank, graph, ans, n):
        if rank[node] >= 0:
            return rank[node]
        rank[node] = depth
        min_dfs_depth = n
        for neighbor in graph[node]:
            # if equals to previous node
            if rank[neighbor] == depth - 1:
                continue
            
            dfs_depth = self.dfs(neighbor, depth + 1, rank, graph, ans, n)
            if dfs_depth <= rank[node]:
                ans.discard(tuple(sorted((node, neighbor))))
            min_dfs_depth = min(min_dfs_depth, dfs_depth)
        return min_dfs_depth
    
    def get_graph(self, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        return graph
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
