# Meeting Rooms 920 \(E\)

## Problem

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

\(0,8\),\(8,10\) is not conflict at 8Example

**Example1**

```text
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
```

**Example2**

```text
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
```

## Solution 

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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        
        intervals = sorted(intervals, key = lambda interval : interval.start)
        
        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

