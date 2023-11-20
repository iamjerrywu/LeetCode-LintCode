# Minimum Height Tree (LeetCode 310) (M)

## Problem

A tree is an undirected graph in which any two vertices are connected by _exactly_ one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`)  are called **minimum height trees** (MHTs).

Return _a list of all **MHTs'** root labels_. You can return the answer in **any order**.

The **height** of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/01/e1.jpg)

<pre><code><strong>Input: n = 4, edges = [[1,0],[1,2],[1,3]]
</strong><strong>Output: [1]
</strong><strong>Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/01/e2.jpg)

<pre><code><strong>Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
</strong><strong>Output: [3,4]
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 2 * 104`
* `edges.length == n - 1`
* `0 <= ai, bi < n`
* `ai != bi`
* All the pairs `(ai, bi)` are distinct.
* The given input is **guaranteed** to be a tree and there will be **no repeated** edges.



## Solution

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (edges.size() == 0) return {0};
        map<int, vector<int>> graph;
        map<int, int> in_deg;
        for (vector<int> e : edges) {
           graph[e[0]].push_back(e[1]);
           graph[e[1]].push_back(e[0]);
           in_deg[e[0]]+=1;
           in_deg[e[1]]+=1;
        }
        deque<int> deq;
        // find first layer, the leaf nodes 
        for (auto kv : in_deg) {
            if (kv.second == 1) {
                deq.push_back(kv.first);
            }
        }
        // bfs, do topological sort, find the last ones
        return bfs(deq, graph, in_deg);
    } 

private:
    vector<int> bfs(deque<int>& deq, map<int, vector<int>>& graph, map<int, int> in_deg) {
        vector<int> ans;
        while(!deq.empty()) {
            ans.clear();
            int size = deq.size();
            for (int i = 0; i < size; i++) {
                int cur = deq.front();
                ans.push_back(cur);
                deq.pop_front();
                for (int nxt : graph[cur]) {
                    in_deg[nxt]-=1;
                    if (in_deg[nxt] == 1)
                        deq.push_back(nxt);
                }
            }
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
