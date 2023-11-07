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

{% tab title="Java" %}
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            if (merged.isEmpty() || interval[0] > merged.getLast(merged.size() - 1)[1]) {
                merged.add(interval);
            } else {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
            }
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // or can simply write: 
        // sort(intervals.begin(), intervals.end())
        sort(intervals.begin(), intervals.end(), compare);
        
        vector<vector<int>> res;
    
        for (vector<int> interval : intervals) {
            if (res.size() == 0 or res.back()[1] < interval[0]) {
                res.push_back(interval);
            } else {
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }
        return res;
    }
    

private:
    static bool compare(vector<int> v1, vector<int> v2) {
        return v1[0] == v2[0] ? v1[1] < v2[1] : v1[0] < v2[0];
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**



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

{% tab title="Java" %}
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        
        ArrayList<int[]> new_arr = new ArrayList<int[]>();
        for (int[] interval : intervals) {
            new_arr.add(new int[]{interval[0], -1});
            new_arr.add(new int[]{interval[1], 1});
        }
        Collections.sort(new_arr, myComparator);
        
        int is_matched = 0;
        List<int[]> res = new ArrayList<>();
        int left = 0, right = 0;
        for (int[] arr : new_arr) {
            if (is_matched == 0) {
                left = arr[0];
            }
            is_matched+=arr[1];
            if (is_matched == 0) {
                right = arr[0];
                res.add(new int[]{left, right});
            }
        }
        return res.toArray(new int[res.size()][]);
    }
    private Comparator<int[]> myComparator = new Comparator<int[]>() {
        @Override
        public int compare(int[] a, int[] b) {
            if (a[0] == b[0]) {
                return a[1] < b[1] ? -1 : 1;
            }
            return a[0] < b[0] ? -1 : 1;
        }
    };
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
lass Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> boundaries;
        
        for (vector<int> interval : intervals) {
            boundaries.push_back(vector<int>{interval[0], -1});
            boundaries.push_back(vector<int>{interval[1], 1});
        }
        
        sort(boundaries.begin(), boundaries.end(), compare);
        
        vector<vector<int>> res;
        int is_matched = 0;
        int left = 0;
        for (vector<int> boundary : boundaries) {
            if (is_matched == 0) {
                left = boundary[0];
            }
            is_matched+=boundary[1];
            if (is_matched == 0) {
                res.push_back(vector<int>{left, boundary[0]});
            }
        }
        return res;
    }
    
private: 
    static bool compare(vector<int> v1, vector<int> v2) {
        return v1[0] == v2[0] ? v1[1] < v2[1] : v1[0] < v2[0];
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

