# Maximum Number of Weeks for Which You Can Work \(LeetCode 1953\) \(E\)

## Problem

There are `n` projects numbered from `0` to `n - 1`. You are given an integer array `milestones` where each `milestones[i]` denotes the number of milestones the `ith` project has.

You can work on the projects following these two rules:

* Every week, you will finish **exactly one** milestone of **one** project. You **must** work every week.
* You **cannot** work on two milestones from the same project for two **consecutive** weeks.

Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will **stop working**. Note that you may not be able to finish every project's milestones due to these constraints.

Return _the **maximum** number of weeks you would be able to work on the projects without violating the rules mentioned above_.

**Example 1:**

```text
Input: milestones = [1,2,3]
Output: 6
Explanation: One possible scenario is:
​​​​- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 2.
- During the 3rd week, you will work on a milestone of project 1.
- During the 4th week, you will work on a milestone of project 2.
- During the 5th week, you will work on a milestone of project 1.
- During the 6th week, you will work on a milestone of project 2.
The total number of weeks is 6.
```

**Example 2:**

```text
Input: milestones = [5,2,1]
Output: 7
Explanation: One possible scenario is:
- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 1.
- During the 3rd week, you will work on a milestone of project 0.
- During the 4th week, you will work on a milestone of project 1.
- During the 5th week, you will work on a milestone of project 0.
- During the 6th week, you will work on a milestone of project 2.
- During the 7th week, you will work on a milestone of project 0.
The total number of weeks is 7.
Note that you cannot work on the last milestone of project 0 on 8th week because it would violate the rules.
Thus, one milestone in project 0 will remain unfinished.
```

**Constraints:**

* `n == milestones.length`
* `1 <= n <= 105`
* `1 <= milestones[i] <= 109`

## Solution - Heap \(LTE\)

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ms_queue = []
        for i in range(len(milestones)):
            ms_queue.append(-milestones[i])
        heapq.heapify(ms_queue)
        
        cur_ms = -heapq.heappop(ms_queue)
        cnt = 0
        
        while True:
            cur_ms-=1
            cnt+=1
            if len(ms_queue) == 0:
                return cnt
            
            prev_ms = cur_ms
            cur_ms = -heapq.heappop(ms_queue)
            if prev_ms != 0:
                heapq.heappush(ms_queue, -prev_ms)    
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(sum\(milestones\)\)**
* **Space Complexity:**

## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        n = len(milestones)
        if n == 1:
            return 1
        cnt = sum(milestones[:-1])
        cnt = cnt * 2 + 1
        return cnt if cnt < sum(milestones) else sum(milestones)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
  * n: len\(milestones\)
* **Space Complexity: O\(1\)**

