# Number of Ships in a Rectangle (LeetCode 1274) (H)

## Problem

_(This problem is an **interactive problem**.)_

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function `Sea.hasShips(topRight, bottomLeft)` which takes two points as arguments and returns `true` If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are **at most 10 ships** in that rectangle.

Submissions making **more than 400 calls** to `hasShips` will be judged _Wrong Answer_. Also, any solutions that attempt to circumvent the judge will result in disqualification.

&#x20;

**Example :**

![](https://assets.leetcode.com/uploads/2019/07/26/1445\_example\_1.PNG)

<pre><code>Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> From [0,0] to [4,4] we can count 3 ships within the range.</code></pre>

**Example 2:**

<pre><code>Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
<strong>Output:
</strong> 3</code></pre>

&#x20;

**Constraints:**

* On the input `ships` is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given `hasShips` API, without knowing the `ships` position.
* `0 <= bottomLeft[0] <= topRight[0] <= 1000`
* `0 <= bottomLeft[1] <= topRight[1] <= 1000`
* `topRight != bottomLeft`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, x2 = bottomLeft.x, topRight.x
        y1, y2 = bottomLeft.y, topRight.y
        if x1 > x2 or y1 > y2:
            return 0
        
        x3, y3 = (x1 + x2)//2, (y1 + y2)//2
        if x1 == x2 and y1 == y2:
            return sea.hasShips(topRight, bottomLeft)
        
        # x3, y3 need to plus one
        bl_cnt, br_cnt, tl_cnt, tr_cnt = 0, 0, 0, 0
        if x3 >= x1 and y3 >= y1 and sea.hasShips(Point(x3, y3), Point(x1, y1)):
            bl_cnt = self.countShips(sea, Point(x3, y3), Point(x1, y1))
        if x2 >= x3 + 1 and y3 >= y1 and sea.hasShips(Point(x2, y3), Point(x3 + 1, y1)):    
            br_cnt = self.countShips(sea, Point(x2, y3), Point(x3 + 1, y1))
        if x3 >= x1 and y2 >= y3 + 1 and sea.hasShips(Point(x3, y2), Point(x1, y3 + 1)):    
            tl_cnt = self.countShips(sea, Point(x3, y2), Point(x1, y3 + 1))
        if x2 >= x3 + 1 and y2 >= y3 + 1 and sea.hasShips(Point(x2, y2), Point(x3 + 1, y3 + 1)):    
            tr_cnt = self.countShips(sea, Point(x2, y2), Point(x3 + 1, y3 + 1))
        return bl_cnt + br_cnt + tl_cnt + tr_cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity**
