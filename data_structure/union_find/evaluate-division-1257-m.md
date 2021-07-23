# Evaluate Division 1257 \(M\)

## Problem

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number \(floating point number\). Given some queries, return the answers. If the answer does not exist, return -1.0.

* The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

Example

```text
Given a / b = 2.0, b / c = 3.0.queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .return [6.0, 0.5, -1.0, 1.0, -1.0 ].The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.According to the example above:equations = [ ["a", "b"], ["b", "c"] ],values = [2.0, 3.0],queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
```

## Solution - Union Find

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
from typing import (
    List,
)

class Solution:
    """
    @param equations: 
    @param values: 
    @param queries: 
    @return: return a double type array
    """
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # write your code here
        adj_list, record = self.get_adj_record(equations, values)
        ans = []
        for q in queries:
            start, end = q[0], q[1]
            if start == end and start in adj_list:
                ans.append(1.0)
                continue
            queue, res, visited = collections.deque(), -1.0, set()
            queue.append((start, 1.0))
            while queue and res == -1:
                cur_node, cur_val = queue.popleft()
                visited.add(cur_node)
                for neighbor in adj_list[cur_node]:
                    if neighbor in visited:
                        continue
                    new_val = cur_val * record[(cur_node, neighbor)]
                    if neighbor == end:
                        res = new_val
                        break
                    queue.append((neighbor, new_val))
            ans.append(res)
        return ans
    
    def get_adj_record(self, equations, values):
        adj_list, record = collections.defaultdict(set), collections.defaultdict(float)
        for i in range(len(equations)):
            u, v = equations[i][0], equations[i][1]
            adj_list[u].add(v)
            adj_list[v].add(u)
            record[(u, v)] = values[i]
            record[(v, u)] = 1 / values[i]
        return adj_list, record
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

