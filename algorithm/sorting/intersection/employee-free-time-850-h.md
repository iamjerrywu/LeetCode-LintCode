# Employee Free Time 850 (H)

## Problem

We are given a list `schedule` of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

The `Intervals` is an 1d-array. Each two numbers shows an interval. For example, `[1,2,8,10]` represents that the employee works in `[1,2]` and `[8,10]`.

Also, we wouldn't include intervals like \[5, 5] in our answer, as they have zero length.

1.schedule and schedule\[i] are lists with lengths in range \[1, 100].\
2.0 <= schedule\[i].start < schedule\[i].end <= 10^8.Example

**Example 1:**

```
Input：schedule = [[1,2,5,6],[1,3],[4,10]]Output：[(3,4)]Explanation:There are a total of three employees, and all commonfree time intervals would be [-inf, 1], [3, 4], [10, inf].We discard any intervals that contain inf as they aren't finite.
```

**Example 2:**

```
Input：schedule = [[1,3,6,7],[2,4],[2,5,9,12]]Output：[(5,6),(7,9)]Explanation：There are a total of three employees, and all commonfree time intervals would be [-inf, 1], [5, 6], [7, 9],[12,inf].We discard any intervals that contain inf as they aren't finite.
```

##

## Solution - Sweep Line

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        times = []
        for worker_schedule in schedule:
            for worker_interval in worker_schedule:
                times.append([worker_interval.start, -1])
                times.append([worker_interval.end, 1])
        
        times.sort()
 
        sum_val = 0
        ans = []
        left = 0
        for time, val in times:
            sum_val+=val
            if sum_val == 0:
                left = time
            if left and sum_val == -1:
                ans.append(Interval(left, time))
                left = 0
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
  * n: len(employee)
* **Space Complexity: O(n)**



## Solution - Heap

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employeeFreeTime(self, schedule):
        # Write your code here
        heap, res = [], []
        for employee in schedule:
            for i in range(0, len(employee), 2):
                heapq.heappush(heap, (employee[i], -1))
                heapq.heappush(heap, (employee[i + 1], 1))
        
        cnt, n = 0, len(heap)
        while n > 1:
            left = heapq.heappop(heap)
            right = heap[0] # the max one
            cnt+=left[1]
            # left should be the end, and right must be the start
            if left[1] == 1 and right[1] == -1 and cnt == 0:
            
            #WARNING!, can also just write if cnt == 0, since it would automatically cover the above condition
            # if cnt == 0: 
                res.append(Interval(left[0], right[0]))  
            n-=1
        return res      
```
{% endtab %}
{% endtabs %}

## Solution - Merge&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        times = []
        for worker_schedule in schedule:
            for time_slot in worker_schedule:
                times.append(time_slot)
        
        times.sort(key = lambda t:(t.start, t.end))
        ans = []
        start = 0
        right = times[0].end
        
        for time in times:
            if right < time.start:
                start = right
            if start:
                ans.append(Interval(start, time.start))
                start = 0
            right = max(right, time.end)
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
  * n: len(employee)
* **Space Complexity: O(n)**
