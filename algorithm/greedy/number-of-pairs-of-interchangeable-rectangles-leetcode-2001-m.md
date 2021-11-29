# Number of Pairs of Interchangeable Rectangles (LeetCode 2001) (M)

## Problem

You are given `n` rectangles represented by a **0-indexed** 2D integer array `rectangles`, where `rectangles[i] = [widthi, heighti]` denotes the width and height of the `ith` rectangle.

Two rectangles `i` and `j` (`i < j`) are considered **interchangeable** if they have the **same** width-to-height ratio. More formally, two rectangles are **interchangeable** if `widthi/heighti == widthj/heightj` (using decimal division, not integer division).

Return _the **number** of pairs of **interchangeable** rectangles in_ `rectangles`.

**Example 1:**

```
Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
```

**Example 2:**

```
Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.
```

**Constraints:**

* `n == rectangles.length`
* `1 <= n <= 105`
* `rectangles[i].length == 2`
* `1 <= widthi, heighti <= 105`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rec = {}
        for rectangle in rectangles:
            ratio = rectangle[0]/rectangle[1]
            rec[ratio] = rec.get(ratio, 0) + 1
        ans = 0
        for k, v in rec.items():
            ans += (1 + (v - 1)) / 2 * (v - 1)
        return int(ans)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
