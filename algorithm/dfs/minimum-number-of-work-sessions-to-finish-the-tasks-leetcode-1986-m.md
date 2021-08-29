# Minimum Number of Work Sessions to Finish the Tasks \(LeetCode 1986\) \(M\)

## Problem



There are `n` tasks assigned to you. The task times are represented as an integer array `tasks` of length `n`, where the `ith` task takes `tasks[i]` hours to finish. A **work session** is when you work for **at most** `sessionTime` consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

* If you start a task in a work session, you must complete it in the **same** work session.
* You can start a new task **immediately** after finishing the previous one.
* You may complete the tasks in **any order**.

Given `tasks` and `sessionTime`, return _the **minimum** number of **work sessions** needed to finish all the tasks following the conditions above._

The tests are generated such that `sessionTime` is **greater** than or **equal** to the **maximum** element in `tasks[i]`.

**Example 1:**

```text
Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
```

**Example 2:**

```text
Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
```

**Example 3:**

```text
Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.
```

**Constraints:**

* `n == tasks.length`
* `1 <= n <= 14`
* `1 <= tasks[i] <= 10`
* `max(tasks[i]) <= sessionTime <= 15`

## Solution - Greedy + DFS

The greedy thinking for this problem would be

1. First try to find .the perfect fit to remaining time \(sessionTime\) with search algorithm
2. If no perfect fit can be found, then start from biggest to the lowest

Need to use a list to store task, and a set to record the task in case they are run out 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        counter = collections.Counter(tasks)
        task_list = [[k, v] for k, v in counter.items()]
        task_list.sort(reverse = True)
        task_set = set(tasks)
        ans = 0
        time = sessionTime
        while True:
            # first try to find perfect match of tasks
            if self.pick_perfect_task(time, task_list, task_set):
                ans+=1
                time = sessionTime
                if len(task_set) == 0:
                    return ans
            # then try to find starting from the biggest task in the remainings
            cost = self.pick_task(time, task_list, task_set)
            if cost == -1:
                ans+=1
                time = sessionTime
                if len(task_set) == 0:
                    return ans
            else:
                time-=cost

    def pick_perfect_task(self, time, task_list, task_set):
        task_sum = 0
        take_tasks = []
        task_whole = []
        for task in task_list:
            task_amount = task[1]
            while task_amount > 0:
                task_whole.append(task[0])
                task_amount-=1
        
        if self.dfs(time, task_sum, task_whole, set(), take_tasks):
            self.update(take_tasks, task_list, task_set)
            return True
        return False
    
    def dfs(self, time, task_sum, task_whole, visited, take_tasks):
        if task_sum > time:
            return False
        if task_sum == time:
            return True
        for i in range(len(task_whole)):
            if i not in visited:
                visited.add(i)
                take_tasks.append(task_whole[i])
                if self.dfs(time, task_sum + task_whole[i], task_whole, visited, take_tasks):
                    return True
                take_tasks.pop()
                visited.remove(i)
    
    # update the tasks sets
    def update(self, take_tasks, task_list, task_set):
        for take_task in take_tasks:
            for task in task_list:
                if task[0] == take_task:
                    task[1]-=1
                    if task[1] == 0:
                        task_set.remove(task[0])
    
    def pick_task(self, time, task_list, task_set):
        for task in task_list:
            if task[1] != 0 and task[0] <= time:
                task[1]-=1
                if task[1] == 0:
                    task_set.remove(task[0])
                return task[0]
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

