# Longest Path On The Tree 1469 (M)

## Problem

Given a tree consisting of `n` nodes, `n-1` edges. Output the distance between the two nodes with the furthest distance on this tree.\
Given three arrays of size `n-1`, `starts`, `ends`, and `lens`, indicating that the `i`-th edge is from `starts[i]` to `ends[i]` and the length is `lens[i]`.

Return the farthest distance between any two nodes on the tree, not the depth of the tree. Note that the given edges are undirected edge.\
It is guaranteed that the given edges are able to constitute a tree.

* 1 \leq n \leq 1\* 10^51≤n≤1∗10​5​​
* 1 \leq lens\[i] \leq 1\* 10^31≤lens\[i]≤1∗10​3​​

Example

**Example 1:**

```
Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[1,2,5,6]
Output：11
Explanation:
(3→2→4)the length of this path is `11`,as well as(4→2→3)。
```

**Example 2:**

```
Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[5,2,5,6]
Output：13
Explanation:
(1→0→2→4)the length of this path is`13`,as well as(4→2→0→1)。
```

## Solution - DFS

{% hint style="danger" %}
Maximum Recursion Depth Exceeded&#x20;
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        # Write your code here
        
        # construct graph
        neighbors = {}
        for i in range(n - 1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]

            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []
            
            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))
        
        # return maximum_chain, maximum_path
        chain, path = self.dfs(0, -1, neighbors)
        return path
    
    def dfs(self, root, parent, neighbors):
        # would not have 'not root'
        # since the all nodes construct in graph are existed
        
        max_chain = 0
        max_path = 0

        child_max_chain = 0
        child_second_max_chain = 0

        for neighbor, dist in neighbors[root]:
            if neighbor == parent:
                continue
            
            child_chain, child_path = self.dfs(neighbor, root, neighbors)
            child_chain += dist

            max_path = max(child_path, max_path)
            max_chain = max(child_chain, max_chain)

            _, child_second_max_chain, child_max_chain = sorted([child_max_chain, child_second_max_chain, child_chain])
        
        max_path = max(child_max_chain + child_second_max_chain, max_path)

        return [max_chain, max_path]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution -BFS

1. 1st BFS:&#x20;
   1. Find the start point that the farthest to the root
2. 2nd BFS:
   1. From the start, find the end that is farthest to the start

#### Follow-up:&#x20;

Find the 2nd longest path

* Longest Path: Start -> End
* 2nd Longest Path: Start - > End' or Start' -> End (must be same in one of the ends)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        # Write your code here
        
        # construct graph
        neighbors = {}
        for i in range(n - 1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]

            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []
            
            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))
        
        # return: the farthest point to root, and the distance
        # first time to find the farthest point, as start for next round
        start, _ = self.bfs(0, neighbors)
        # second time to find the distance
        end, answer = self.bfs(start, neighbors)
        return answer 
    
    def bfs(self, root, neighbors):
        queue = collections.deque()
        distance_to_root = {}

        queue.append(root)
        distance_to_root[root] = 0

        max_distance, max_node = 0, -1
        while queue:
            now = queue.popleft()

            if max_distance < distance_to_root[now]:
                max_distance = distance_to_root[now]
                max_node = now

            for neighbor, edge_length in neighbors[now]:
                if neighbor in distance_to_root:
                    continue
                queue.append(neighbor)
                distance_to_root[neighbor] = distance_to_root[now] + edge_length
        return max_node, max_distance
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
