# Number of Provinces 547 \(M\)

## Problem



There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return _the total number of **provinces**_.

**Example 1:**![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:**![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```text
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

**Constraints:**

* `1 <= n <= 200`
* `n == isConnected.length`
* `n == isConnected[i].length`
* `isConnected[i][j]` is `1` or `0`.
* `isConnected[i][i] == 1`
* `isConnected[i][j] == isConnected[j][i]`

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        cnt = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                # this line can be ignored since later would not visited this city again
                visited[i] = True
                self.dfs(isConnected, visited, i)
                cnt+=1
        return cnt
    
    def dfs(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                # mark as visited, since later would visited that city
                visited[j] = True
                self.dfs(isConnected, visited, j)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
  * Call stack depth: O\(n\)
  * Loop: O\(n\), since set would avoid the next loop, each city would only be visited once 
* **Space Complexity: O\(n\)**

\*\*\*\*

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        cnt = 0
        queue = collections.deque()
        for i in range(len(isConnected)):
            if not visited[i]:
                queue.append(i)
                # in here the connected graph would all be traversed, and only count as one
                while queue:
                    city = queue.popleft()
                    visited[city] = True
                    for j in range(len(isConnected)):
                        if isConnected[city][j] == 1 and not visited[j]:
                            queue.append(j)
                cnt+=1
        return cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
  * Traverse every city: O\(n\)
    * For each city, would traverse again every possible connections O\(n\)
* **Space Complexity: O\(n\)**

