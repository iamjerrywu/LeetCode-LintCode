# Trapping Rain Water II 364 \(H\)

## Problem

Given _n_ x _m_ non-negative integers representing an elevation map 2d where the area of each cell is _1_ x _1_, compute how much water it is able to trap after raining.

![](https://lintcode-media.oss-us-west-1.aliyuncs.com/problem/trapping-rain-water-ii.jpg)Example

**Example 1:**

```text
Given `5*4` matrix Input:[[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]Output:14
```

**Example 2:**

```text
Input:[[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]Output:0
```

## Solution - Heap



### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
import heapq
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        
        if not heights:
            return 0
        
        n, m = len(heights), len(heights[0])
        visited = set([])
        heap = []
        
        # put all the block in outermost layer into heap
        # put as tuple (height, (x, y)) into heap
        for i in range(n):
            heapq.heappush(heap, (heights[i][0], i, 0))
            heapq.heappush(heap, (heights[i][m - 1], i, m - 1))
            visited.add((i, 0))
            visited.add((i, m - 1))
        for i in range(m):
            heapq.heappush(heap, (heights[0][i], 0, i))
            heapq.heappush(heap, (heights[n - 1][i], n - 1, i))
            visited.add((0, i))
            visited.add((n - 1, i))
        
        water = 0
        while heap:
            shortest = heapq.heappop(heap)
            
            for dx, dy in  DIRECTIONS:
                x = shortest[1] + dx
                y = shortest[2] + dy

                if not self.is_valid(x, y, visited, n, m):
                    continue
                
                if shortest[0] > heights[x][y]:
                    water+=shortest[0] - heights[x][y]
                # add neighbor into heap
                height = max(shortest[0], heights[x][y])
                heapq.heappush(heap, (height, x, y))
                visited.add((x, y))
        return water
    
    def is_valid(self, x, y, visited, n, m):
        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False
        return (x, y) not in visited
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity: O\(n\)**

