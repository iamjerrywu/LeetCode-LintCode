# Insert Interval 30 (M)

## Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**Example 3:**

```
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
```

**Example 4:**

```
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
```

**Example 5:**

```
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
```

**Constraints:**

* `0 <= intervals.length <= 104`
* `intervals[i].length == 2`
* `0 <= starti <= endi <= 105`
* `intervals` is sorted by `starti` in **ascending** order.
* `newInterval.length == 2`
* `0 <= start <= end <= 105`

## Solution **- New Array**

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort(key = lambda s:(s[0], s[1]))
        
        boundaries = []
        for interval in intervals:
            boundaries.append([interval[0], -1])
            boundaries.append([interval[1], 1])
        
        boundaries.sort(key = lambda s:(s[0], s[1]))
        res = []
        cnt = 0
        for boundary in boundaries:
            if cnt == 0:
                start = boundary[0]
            cnt+=boundary[1]
            if cnt == 0:
                res.append([start, boundary[0]])
        intervals = list(res)
        return intervals
                    
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**

## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ret;
        int i = 0, n = intervals.size();

        while (i < n and intervals[i][1] < newInterval[0]) {
            ret.push_back(intervals[i]);
            i++;
        }
        while (i < n and newInterval[1] >= intervals[i][0]) {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        ret.push_back(newInterval);
        while(i < n) {
            ret.push_back(intervals[i]);
            i++;
        }
        return ret;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
