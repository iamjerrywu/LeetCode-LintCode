# Course Schedule 615 \(M\)

## Problem

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Before taking some courses, you need to take other courses. For example, to learn course 0, you need to learn course 1 first, which is expressed as \[0,1\].

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?Example

Example 1:

```text
Input: n = 2, prerequisites = [[1,0]] 
Output: true
```

Example 2:

```text
Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false
```

## Solution 

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
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

