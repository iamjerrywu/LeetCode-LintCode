# Clone Graph 137 (M)

## Problem



Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

You need return the node with the same label as the input node.\
How we represent an undirected graph: [http://www.lintcode.com/help/graph/](http://www.lintcode.com/help/graph/)Example

**Example1**

```
Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
```

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
        # step 1: find nodes
        nodes = self.find_nodes_by_bfs(node)
        # step 2: copy nodes
        mapping = self.copy_nodes(nodes)
        # step 3: copy edges 
        self.copy_edges(nodes, mapping)

        return mapping[node]
    
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor in visited:
                    continue
                # should add to set once neighbor is visited
                visited.add(neighbor)
                queue.append(neighbor)
        return list(visited)
    
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node. label)
        return mapping
    
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        mapping = {}
        mapping[node.val] = Node(node.val)
        queue = collections.deque([(node)])
        
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val not in mapping:
                    clone_neighbor = Node(neighbor.val)
                else:
                    clone_neighbor = mapping[neighbor.val]
                mapping[cur.val].neighbors.append(clone_neighbor)
                if neighbor.val not in mapping:
                    queue.append(neighbor)
                    # like visited, add the node here after traversing all the neighbors
                    mapping[neighbor.val] = clone_neighbor
        return mapping[node.val]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O( N + M)**
* **Space Complexity: O(n)**



## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        mapping = {}
        mapping[node.val] = Node(node.val)
        
        self.dfs(node, mapping)
        return mapping[node.val]
        
    def dfs(self, node, mapping):
        for neighbor in node.neighbors:
            if neighbor.val not in mapping:
                clone_neighbor = Node(neighbor.val)
            else:
                clone_neighbor = mapping[neighbor.val]
            mapping[node.val].neighbors.append(clone_neighbor)
            if neighbor.val not in mapping:
                mapping[neighbor.val] = clone_neighbor
                self.dfs(neighbor, mapping)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="C++" %}
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;
        map<int, Node*> mapping;
        mapping[node->val] = new Node(node->val);

        dfs(node, mapping);
        return mapping[node->val];
    }

    void dfs(Node* node, map<int, Node*>& mapping) {
        for (Node* neighbor : node->neighbors) {
            Node* clone_neighbor;
            if (!mapping.count(neighbor->val)) {
                clone_neighbor = new Node(neighbor->val);
                
            } else {
                clone_neighbor = mapping[neighbor->val];
            }
            mapping[node->val]->neighbors.push_back(clone_neighbor);
            if (!mapping.count(neighbor->val)) {
                mapping[neighbor->val] = clone_neighbor;
                dfs(neighbor, mapping);
            }
        }
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O( N + M)**
  * N: number of nodes
  * M: number of edges
* **Space Complexity:**
