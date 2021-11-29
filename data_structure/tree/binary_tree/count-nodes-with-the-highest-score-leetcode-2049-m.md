# Count Nodes With the Highest Score (LeetCode 2049) (M)

## Problem



There is a **binary** tree rooted at `0` consisting of `n` nodes. The nodes are labeled from `0` to `n - 1`. You are given a **0-indexed** integer array `parents` representing the tree, where `parents[i]` is the parent of node `i`. Since node `0` is the root, `parents[0] == -1`.

Each node has a **score**. To find the score of a node, consider if the node and the edges connected to it were **removed**. The tree would become one or more **non-empty** subtrees. The **size** of a subtree is the number of the nodes in it. The **score** of the node is the **product of the sizes** of all those subtrees.

Return _the **number** of nodes that have the **highest score**_.

&#x20;

**Example 1:**

![example-1](https://assets.leetcode.com/uploads/2021/10/03/example-1.png)

```
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
```

**Example 2:**

![example-2](https://assets.leetcode.com/uploads/2021/10/03/example-2.png)

```
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
```

&#x20;

**Constraints:**

* `n == parents.length`
* `2 <= n <= 105`
* `parents[0] == -1`
* `0 <= parents[i] <= n - 1` for `i != 0`
* `parents` represents a valid binary tree.

## Solution

![](<../../../.gitbook/assets/Screen Shot 2021-10-24 at 4.25.29 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = collections.defaultdict(list)
        counter = {}
        for i in range(len(parents)):
            graph[parents[i]].append(i)
        # count nodes for every parent tree
        self.count_nodes(0, counter, graph)
        
        max_val = 0
        max_cnt = 0
        # test to remove nodes from 0 -> n - 1
        for i in range(len(parents)):
            # left_sub_tree, right_sub_tree, up_sub_tree
            val = 1
            for child in graph[i]:
                if counter[child] != 0:
                    val*=counter[child]
            if parents[i] != -1:
                val*=(counter[0] - counter[i])
            if val > max_val:
                max_val = val
                max_cnt = 1
            elif val == max_val:
                max_cnt+=1
        return max_cnt
        
    def count_nodes(self, node, counter, graph):
        cnt = 1
        for child in graph[node]:
            cnt+=self.count_nodes(child, counter, graph)
        counter[node] = cnt
        return cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
