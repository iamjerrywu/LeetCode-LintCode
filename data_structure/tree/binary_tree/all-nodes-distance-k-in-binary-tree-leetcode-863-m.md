# All Nodes Distance K in Binary Tree (LeetCode 863) (M)

## Problem

Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return _an array of the values of all nodes that have a distance _`k`_ from the target node._

You can return the answer in **any order**.

&#x20;

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```

**Example 2:**

```
Input: root = [1], target = 1, k = 3
Output: []
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 500]`.
* `0 <= Node.val <= 500`
* All the values `Node.val` are **unique**.
* `target` is the value of one of the nodes in the tree.
* `0 <= k <= 1000`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        # construct graph
        self.dfs(root, root, graph)
        
        tar_val = target.val
        queue = collections.deque([tar_val])
        visited  = set([tar_val])
        dist = 0
        ans = []
        while queue:
            for _ in range(len(queue)):
                cur_val = queue.popleft()
                if dist == k:
                    ans.append(cur_val)
                else:
                    for neighbor in graph[cur_val]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            dist+=1
        
        return ans
    
    def dfs(self, node, parent, graph):
        if not node:
            return 
        if node.val != parent.val:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        self.dfs(node.left, node, graph)
        self.dfs(node.right, node, graph)
```
{% endtab %}

{% tab title="Java" %}
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        int target_val = target.val;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        dfs(root, root, graph);
        System.out.println(graph);
        Set<Integer> visited = new HashSet<Integer>();
        Queue<Integer> queue = new LinkedList<>();
        
        int dist = 0;
        List<Integer> ans = new ArrayList<>();
        queue.offer(target_val);
        visited.add(target_val);
        while(!queue.isEmpty()) {
            int qSize = queue.size();
            for (int i = 0; i < qSize; i++) {
                int cur_val = queue.poll();
                if (dist != k) {
                    for(int neighbor : graph.getOrDefault(cur_val, new ArrayList<>())) {
                        if (!visited.contains(neighbor)) {
                            queue.offer(neighbor);
                            visited.add(neighbor);
                        }
                    }
                } else {
                    ans.add(cur_val);
                }
            }
            dist+=1;
        }
        return ans;
    
    }
    
    private void dfs(TreeNode node, TreeNode parent, Map<Integer, List<Integer>> graph) {
        if (node == null) 
            return;
        if (node.val != parent.val) {
            graph.putIfAbsent(node.val, new ArrayList<>());
            graph.get(node.val).add(parent.val);
            graph.putIfAbsent(parent.val, new ArrayList<>());
            graph.get(parent.val).add(node.val);
        }
        dfs(node.left, node, graph);
        dfs(node.right, node, graph);
    }
}
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(n)**
  * Worst case that tree is like a linkedlist
* **Space Complexity: O(n)**
