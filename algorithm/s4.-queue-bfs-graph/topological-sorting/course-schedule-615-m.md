# Course Schedule 615 (M)

## Problem

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Before taking some courses, you need to take other courses. For example, to learn course 0, you need to learn course 1 first, which is expressed as \[0,1].

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?Example

Example 1:

```
Input: n = 2, prerequisites = [[1,0]] 
Output: true
```

Example 2:

```
Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses

        # construct graph
        # [0, 1], 0 <- 1 (0: node_in / 1: node_out)
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in]+=1

        num_choose = 0
        queue = collections.deque()

        # those don't have pre-requiste course, can be the beginning 
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            now_pos = queue.popleft()
            num_choose+=1
            for next_pos in graph[now_pos]:
                in_degree[next_pos]-=1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        
        return num_choose == numCourses
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int inDegrees[numCourses];
        unordered_map<int, vector<int>> nxts;
        
        // init data structure
        for (int i = 0; i < numCourses; i++) inDegrees[i] = 0;
        for (vector<int> pr : prerequisites) {
            inDegrees[pr[0]]+=1;
            nxts[pr[1]].push_back(pr[0]);
        }
        
        queue<int> queue;
        // if indegree is 0, means it can be started courses
        for (int i = 0; i < numCourses; i++) {
            if (inDegrees[i] == 0) {
                queue.push(i);
            }
        }
        int taken = 0;
        while (!queue.empty()) {
            int curCourse = queue.front();
            taken+=1;
            queue.pop();
            for (int nxtCourse : nxts[curCourse]) {
                inDegrees[nxtCourse]-=1;
                if (inDegrees[nxtCourse] == 0) {
                    queue.push(nxtCourse);
                } 
            }
        }
        return taken == numCourses;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(E + V)**
  * E: Number of dependencies
  * V: Number of Courses
* **Space Complexity:**&#x20;
  * **O(E + V)**
    * E: Number of dependencies
    * V: Number of Courses
