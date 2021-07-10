# The Skyline Problem 131 \(H\)

## Problem

A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return _the **skyline** formed by these buildings collectively_.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [lefti, righti, heighti]`:

* `lefti` is the x coordinate of the left edge of the `ith` building.
* `righti` is the x coordinate of the right edge of the `ith` building.
* `heighti` is the height of the `ith` building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`.

The **skyline** should be represented as a list of "key points" **sorted by their x-coordinate** in the form `[[x1,y1],[x2,y2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate `0` and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

**Note:** There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...,[2 3],[4 5],[12 7],...]`

**Example 1:**![](https://assets.leetcode.com/uploads/2020/12/01/merged.jpg)

```text
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
```

**Example 2:**

```text
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
```

**Constraints:**

* `1 <= buildings.length <= 104`
* `0 <= lefti < righti <= 231 - 1`
* `1 <= heighti <= 231 - 1`
* `buildings` is sorted by `lefti` in non-decreasing order.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class BuildingType:
    start = 1
    end = 0
    
class Solution:
    def getSkyline(self, buildings):
        points = []
        for left, right, height in buildings:
            # mark the height in start point as -height
            # since when sorting, for same left position, make the higher building in the front
            # when same left, right position, also make the higher building in the front (since if the higher one need to popped, should pop first)
            points.append((left, -height, BuildingType.start))
            points.append((right, height, BuildingType.end))
        # sort based on position
        points.sort()
        min_heap, max_height = [0], 0
        res = []
        for pos, height, status in points:
            if status == BuildingType.start: # start point
                if -height > max_height:
                    max_height = -height
                    res.append([pos, -height])
                heapq.heappush(min_heap, height)
            else: # end point
                self.heap_remove(min_heap, -height)
                heap_max = -min_heap[0]
                if heap_max < max_height:
                    max_height = heap_max
                    res.append([pos, max_height])
        return res
    
    def heap_remove(self, heap, height):
        for val in heap:
            if val == height:
                heap.remove(height)
                break
        heapq.heapify(heap)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
  * Traverse: O\(n\)
  * Heap manipulation: 
    * Push: O\(logn\)
    * Remove: O\(n\)
* **Space Complexity: O\(n\)**

\*\*\*\*

## Solution - Heap with Lazy Delete

{% tabs %}
{% tab title="Python" %}
```python
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minheap = []
        self.deleted_set = set()
    #O(logk)
    def push(self, val, index):
        heappush(self.minheap, (val, index))
    
    #O(logk)
    def _lazy_delete(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)
    
    #O(logk)
    def top(self):
        self._lazy_delete()
        return self.minheap[0][0]
    #O(logk)
    def pop(self):
        self._lazy_delete()
        heappop(self.minheap)
    
    # O(1)
    def delete(self, index):
        self.deleted_set.add(index)
    
    #O(1)
    def is_empty(self):
        return not bool(self.minheap)


class BuildingType:
    start = 1
    end = 0
    
class Solution:
    def getSkyline(self, buildings):
        points = []
        index = 0
        for left, right, height in buildings:
            # mark the height in start point as -height
            # since when sorting, for same left position, make the higher building in the front
            # when same left, right position, also make the higher building in the front (since if the higher one need to popped, should pop first)
            points.append((left, -height, BuildingType.start, index))
            points.append((right, height, BuildingType.end, index))
            index+=1
        # sort based on position
        points.sort()
        # print(points)
        min_heap, max_height = Heap(), 0
        min_heap.push(0, -1)
        res = []
        for pos, height, status, index in points:
            if status == BuildingType.start: # start point
                if -height > max_height:
                    max_height = -height
                    res.append([pos, -height])
                min_heap.push(height, index)
            else: # end point
                min_heap.delete(index)
                heap_max = -min_heap.top()
                if heap_max < max_height:
                    max_height = heap_max
                    res.append([pos, max_height])
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

