# K Closests Points 612 \(M\)

## Problem

Given some `points` and an `origin` in two-dimensional space,Find `k` `points` from points which are closest to `origin` Euclidean.Return to the answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.Example

Example 1:

```text
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
```

Example 2:

```text
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
```

Challenge

O\(nlogn\) is OK, but can you think of a solution to O\(nlogk\)？

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

* **Time Complexity: O\(n + klogk\)**
* **Space Complexity:**

## Solution - Max Heap

### Code

{% tabs %}
{% tab title="python" %}
```python

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

\*\*\*\*

## Solution - Min Heap

### Code

{% tabs %}
{% tab title="python" %}
```python

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

