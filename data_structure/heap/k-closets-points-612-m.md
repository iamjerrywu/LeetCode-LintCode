# K Closests Points 612 (M)

## Problem

Given some `points` and an `origin` in two-dimensional space,Find `k` `points` from points which are closest to `origin` Euclidean.Return to the answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.Example

Example 1:

```
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
```

Example 2:

```
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
```

Challenge

O(nlogn) is OK, but can you think of a solution to O(nlogk)？

## Solution - Quick Select

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        # tuple with (distance^2, x-position, y-position)
        vectors = [((p.x - origin.x)**2 + (p.y - origin.y)**2, p.x, p.y) for p in points]
         
        # quick select
        #O(n)
        self.quick_select(vectors, 0, len(vectors) - 1, k -1)
        # O(klogk)
        sorted_vectors = sorted(vectors[:k], key = lambda vector : (vector[0], vector[1], vector[2]))
        k_list = list(Point(x, y) for _, x, y in sorted_vectors)
        
        return k_list
    
    def quick_select(self, vectors, start, end, kth):
        if start == end:
            return
        left, right = start, end
        pivot = (vectors[left][0] + vectors[right][0])//2
        while left <= right:
            while left <= right and vectors[left][0] < pivot:
                left+=1
            while left <= right and vectors[right][0] > pivot:
                right-=1
            if left <= right:
                vectors[left], vectors[right] = vectors[right], vectors[left]
                left+=1
                right-=1
        if left <= kth:
            self.quick_select(vectors, left, end, kth)
        if right >= kth:
            self.quick_select(vectors, start, right, kth)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n + klogk)**
* **Space Complexity:**

## Solution - Max Heap (1)

Since python heapq is default a min-heap, so need to `values  *(-1)` inorder to make it act as max\_heap&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))
            
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        self.heap.sort(key = lambda item:(-item[0], -item[1], -item[2]))
        return [(-x, -y) for _, x, y in self.heap]
  
    def get_distance(self, point, origin):
        return (point.x - origin.x)**2 + (point.y - origin.y)**2
```
{% endtab %}

{% tab title="java" %}
```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // PriorityQueue<Integer> pQueue = new PriorityQueue<>();
        PriorityQueue<int[]> pQueue = new PriorityQueue<int[]>((p1, p2)-> (p2[0] * p2[0] + p2[1] * p2[1]) - (p1[0] * p1[0] + p1[1] * p1[1]));
        
        for (int i = 0; i < points.length; i++) {
            pQueue.add(points[i]);
            
            if (pQueue.size() > k) {
                pQueue.poll();
            }
        }
        
        int[][] ans = new int[k][2];
        for (int i = 0; i < k; i++) {
            ans[i] = pQueue.poll();
        }
        return ans;
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Max Heap (2)

Since python heapq is default a min-heap, so need to `values  *(-1)` inorder to make it act as max\_heap&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, point[0], point[1]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [[point_x, point_y] for dist, point_x, point_y in heap]
        return ans
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Min Heap

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        # min heap solution
        self.heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(self.heap, (dist, point.x, point.y))
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(self.heap)
            res.append(Point(x, y))
        
        return res
    def get_distance(self, point, origin):
        return (point.x - origin.x)**2 + (point.y - origin.y)**2
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogk)**
* **Space Complexity:**
