# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts  (LeetCode 1465) (M)

## Problem

You are given a rectangular cake of size `h x w` and two arrays of integers `horizontalCuts` and `verticalCuts` where:

* `horizontalCuts[i]` is the distance from the top of the rectangular cake to the `ith` horizontal cut and similarly, and
* `verticalCuts[j]` is the distance from the left of the rectangular cake to the `jth` vertical cut.

Return _the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays_ `horizontalCuts` _and_ `verticalCuts`. Since the answer can be a large number, return this **modulo** `109 + 7`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/05/14/leetcode\_max\_area\_2.png)

```
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/05/14/leetcode\_max\_area\_3.png)

```
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
```

**Example 3:**

```
Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
```

&#x20;

**Constraints:**

* `2 <= h, w <= 109`
* `1 <= horizontalCuts.length <= min(h - 1, 105)`
* `1 <= verticalCuts.length <= min(w - 1, 105)`
* `1 <= horizontalCuts[i] < h`
* `1 <= verticalCuts[i] < w`
* All the elements in `horizontalCuts` are distinct.
* All the elements in `verticalCuts` are distinct.



## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
MOD = 10 ** 9 + 7
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # find maximum intervals in horizontal and vertical, then multiply them
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = float('-inf')
        max_h = max(max_h, horizontalCuts[0] - 0)
        for i in range(len(horizontalCuts) - 1):
            max_h = max(max_h, horizontalCuts[i + 1] - horizontalCuts[i])
        max_h = max(max_h, h - horizontalCuts[-1])
        
        max_w = float('-inf')
        max_w = max(max_w, verticalCuts[0] - 0)
        for i in range(len(verticalCuts) - 1):
            max_w = max(max_w, verticalCuts[i + 1] - verticalCuts[i])
        max_w = max(max_w, w - verticalCuts[-1])
        return (max_h * max_w) % MOD
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

