# Rectangle Overlap 626 (E)

## Problem

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is **positive**. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true`_ if they overlap, otherwise return _`false`.

**Example 1:**

```
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
```

**Example 2:**

```
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
```

**Example 3:**

```
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
```

**Constraints:**

* `rect1.length == 4`
* `rect2.length == 4`
* `-109 <= rec1[i], rec2[i] <= 109`
* `rec1` and `rec2` represent a valid rectangle with a non-zero area.

## Solution - Check Points

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec_x = [[rec1[0], rec1[2]], [rec2[0], rec2[2]]]
        rec_y = [[rec1[1], rec1[3]], [rec2[1], rec2[3]]]
        rec_x.sort()
        rec_y.sort()
        
        if rec_x[0][1] > rec_x[1][0] and rec_y[0][1] > rec_y[1][0]:
            return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: **
* **Space Complexity: **
