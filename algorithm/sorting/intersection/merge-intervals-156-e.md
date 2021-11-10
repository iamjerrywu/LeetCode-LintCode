# Merge Intervals 156 (E)

## Problem

Given a collection of intervals, merge all overlapping intervals.Example

**Example 1:**

```
Input: [(1,3)]
Output: [(1,3)]
```

**Example 2:**

```
Input:  [(1,3),(2,6),(8,10),(15,18)]
Output: [(1,6),(8,10),(15,18)]
```

Challenge

O(_n_ log _n_) time and O(1) extra space.

## Solution - Greedy (1)

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key = lambda e:(e.start, e.end))
        slow, fast = 0, 1
        while fast < len(intervals):
            if intervals[slow].end >= intervals[fast].start:
                if intervals[slow].end <= intervals[fast].end:
                    intervals[slow].end = intervals[fast].end
                intervals[slow + 1] = intervals[fast]
            else:
                intervals[slow + 1] = intervals[fast]
                slow+=1
            fast+=1
        return intervals[0:slow + 1]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Greedy (Concise)

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        intervals = sorted(intervals, key = lambda x: x.start)
        res = []
        for interval in intervals:
            if len(res) == 0 or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Line Sweep

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        boundaries = []
        for interval in intervals:
            boundaries.append((interval.start, -1))
            boundaries.append((interval.end, 1))
        boundaries.sort(key = lambda n :(n[0], n[1]))
        
        # cannot write like following
        # since when sorting, we want to let the having same point
        # the 'start' one would appear prior than the 'end' one
        
        #i.e: [1,4], [4,5], the later 4 in [4,5] should be first when sorting
        '''
            boundaries.append((interval.start, 1))
            boundaries.append((interval.end, -1))
        boundaries.sort(key = lambda n :(n[0], -n[1]))
        '''
        

        res = []
        is_matched = 0
        for boundary in boundaries:
            if is_matched == 0:
                left = boundary[0]
            is_matched +=boundary[1]
            if is_matched == 0:
                right = boundary[0]
                res.append(Interval(left, right))
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

