# Interval List Intersections (LeetCode 986) (M)

## Problem

* `0 <= firstList.length, secondList.length <= 1000`
* `firstList.length + secondList.length >= 1`
* `0 <= starti < endi <= 109`
* `endi < starti+1`
* `0 <= startj < endj <= 109`
* `endj < startj+1`

**Constraints:**

```
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
```

**Example 4:**

```
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
```

**Example 3:**

```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

**Example 2:**

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

![](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)

**Example 1:**

&#x20;

The **intersection** of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

A **closed interval** `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

Return _the intersection of these two interval lists_.

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise **disjoint** and in **sorted order**.

&#x20;

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        
        pt1, pt2 = 0, 0
        ans = []
        while pt1 < len(firstList) and pt2 < len(secondList):
            intersect_right = min(firstList[pt1][1], secondList[pt2][1])
            intersect_left = max(firstList[pt1][0], secondList[pt2][0])
            
            if intersect_left <= intersect_right:
                ans.append([intersect_left, intersect_right])
            
            if firstList[pt1][1] > secondList[pt2][1]:
                pt2+=1
            else:
                pt1+=1
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
