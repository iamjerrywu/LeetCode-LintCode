# Minimum Area Rectangle (LeetCode 939) (M)

## Problem

You are given an array of points in the **X-Y** plane `points` where `points[i] = [xi, yi]`.

Return _the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes_. If there is not any such rectangle, return `0`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

&#x20;

**Constraints:**

* `1 <= points.length <= 500`
* `points[i].length == 2`
* `0 <= xi, yi <= 4 * 104`
* All the given points are **unique**.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, abs(x2 - x1) * abs(y2 - y1))
            seen.add((x1, y1))
        return ans if ans != float('inf') else 0
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
* **Space Complexity:**

