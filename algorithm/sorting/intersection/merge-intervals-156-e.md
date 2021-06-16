# Merge Intervals 156 \(E\)

## Problem

Given a collection of intervals, merge all overlapping intervals.Example

**Example 1:**

```text
Input: [(1,3)]
Output: [(1,3)]
```

**Example 2:**

```text
Input:  [(1,3),(2,6),(8,10),(15,18)]
Output: [(1,6),(8,10),(15,18)]
```

Challenge

O\(_n_ log _n_\) time and O\(1\) extra space.

## Solution - Greedy \(1\)

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

## Solution - Greedy \(Concise\)

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

\*\*\*\*

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



