# Detect Squares (LeetCode 2013) (M)

## Problem

You are given a stream of points on the X-Y plane. Design an algorithm that:

* **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
* Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

* `DetectSquares()` Initializes the object with an empty data structure.
* `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
* `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/09/01/image.png)

```
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
```

**Constraints:**

* `point.length == 2`
* `0 <= x, y <= 1000`
* At most `5000` calls **in total** will be made to `add` and `count`.

## Solution - Hash (Brute Force)

![](<../../.gitbook/assets/Screen Shot 2021-09-19 at 12.51.03 AM.png>)

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
import collections
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        
        
    def count(self, point: List[int]) -> int:
        cnt = 0
        for dx, dy in DIRECTIONS:
            x, y = point[0], point[1]
            ori_x, ori_y = x, y
            while self.is_valid(x + dx, y + dy):
                new_x, new_y = x + dx, y + dy
                if self.points[(new_x, new_y)] > 0 and self.points[(new_x, ori_y)] > 0 and self.points[(ori_x, new_y)] > 0:
                    cnt +=self.points[(new_x, new_y)] * self.points[(new_x, ori_y)] * self.points[(ori_x, new_y)] 
                x = new_x
                y = new_y
        return cnt    
    
    def is_valid(self, x, y):
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            return True
        return False
                            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**

****

## Solution - Hash (Optimized)

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
import collections
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_point = collections.defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        self.x_point[point[0]].append(point[1])
        
        
    def count(self, point: List[int]) -> int:
        cnt = 0
        x, y = point[0], point[1]
        for new_y in self.x_point[x]:
            # WARNING, if New_Y == cur_y, then bypass
            if new_y == y:
                continue
            for new_x in [x + (y - new_y), x + (new_y - y)]:
                if self.points[(new_x, new_y)] > 0 and self.points[(new_x, y)] > 0:
                    cnt +=self.points[(new_x, new_y)] * self.points[(new_x, y)]
        return cnt    

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity**
