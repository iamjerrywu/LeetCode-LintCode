# Maximum Number of Events That Can Be Attended (LeetCode 1353) (M)

## Problem



Given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDayi` and ends at `endDayi`.

You can attend an event `i` at any day `d` where `startTimei <= d <= endTimei`. Notice that you can only attend one event at any time `d`.

Return _the maximum number of events_ you can attend.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/02/05/e1.png)

```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
```

**Example 2:**

```
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
```

**Example 3:**

```
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
```

**Example 4:**

```
Input: events = [[1,100000]]
Output: 1
```

**Example 5:**

```
Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
```

&#x20;

**Constraints:**

* `1 <= events.length <= 105`
* `events[i].length == 2`
* `1 <= startDayi <= endDayi <= 105`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda e:(e[0], e[1]))
        
        total_days = max(event[1] for event in events)
        
        day = 0
        heap = []
        evt_id = 0
        ans = 0
        while day <= total_days:
            
            # optimized speed, if gap in events, then don't need to traverse day by day
            if evt_id < len(events) and not heap:
                day = events[evt_id][0]
            
            # add event in progress
            while evt_id < len(events) and events[evt_id][0] <= day: 
                heapq.heappush(heap, events[evt_id][1])
                evt_id+=1
            
            # discard ended events
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                ans+=1
            day+=1
        return ans
        
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
  * n: Total days
* **Space Complexity:**

****
