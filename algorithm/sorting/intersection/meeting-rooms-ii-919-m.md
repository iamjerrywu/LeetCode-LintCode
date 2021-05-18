# Meeting Rooms II 919 \(M\)

## Problem

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.Example

**Example1**

```text
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
```

**Example2**

```text
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
```

## Solution - Sweep Line

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

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        time_table = []
        for interval in intervals:
            time_table.append((interval.start, 1))
            time_table.append((interval.end, -1))
        
        time_table.sort(key = lambda n : n[0])
        cnt, max_cnt = 0, 0
        for time in time_table:
            cnt+=time[1]
            max_cnt = max(max_cnt, cnt)
        return max_cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
  * Traverse: O\(n\)
  * Sort: O\(nlogn\)
* **Space Complexity: O\(n\)**



## Solution - Prefix Sum

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(T\)**
  * T: the max end time 
* **Space Complexity: O\(n\)**

