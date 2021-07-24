# Describe the Painting 1943 \(M\)

## Problem

There is a long and thin painting that can be represented by a number line. The painting was painted with multiple overlapping segments where each segment was painted with a **unique** color. You are given a 2D integer array `segments`, where `segments[i] = [starti, endi, colori]` represents the **half-closed segment** `[starti, endi)` with `colori` as the color.

The colors in the overlapping segments of the painting were **mixed** when it was painted. When two or more colors mix, they form a new color that can be represented as a **set** of mixed colors.

* For example, if colors `2`, `4`, and `6` are mixed, then the resulting mixed color is `{2,4,6}`.

For the sake of simplicity, you should only output the **sum** of the elements in the set rather than the full set.

You want to **describe** the painting with the **minimum** number of non-overlapping **half-closed segments** of these mixed colors. These segments can be represented by the 2D array `painting` where `painting[j] = [leftj, rightj, mixj]` describes a **half-closed segment** `[leftj, rightj)` with the mixed color **sum** of `mixj`.

* For example, the painting created with `segments = [[1,4,5],[1,7,7]]` can be described by `painting = [[1,4,12],[4,7,7]]` because:
  * `[1,4)` is colored `{5,7}` \(with a sum of `12`\) from both the first and second segments.
  * `[4,7)` is colored `{7}` from only the second segment.

Return _the 2D array_ `painting` _describing the finished painting \(excluding any parts that are **not** painted\). You may return the segments in **any order**_.

A **half-closed segment** `[a, b)` is the section of the number line between points `a` and `b` **including** point `a` and **not including** point `b`.

## Solution - Sweep Line

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        color_mapping = []
        for segment in segments:
            color_mapping.append((segment[0], segment[2], True))
            color_mapping.append((segment[1], segment[2], False))
        color_mapping.sort(key = lambda c : (c[0], c[2]))
        
        mapping = {}
        sum_val = 0
        for index, variance, add in color_mapping:
            if add:
                sum_val+=variance
            else:
                sum_val-=variance
            mapping[index] = sum_val
        res_tmp = [(k, v) for k, v in mapping.items()]
        res = []
        for i in range(len(res_tmp) - 1):
            if res_tmp[i][1] != 0:
                res.append([res_tmp[i][0], res_tmp[i + 1][0], res_tmp[i][1]])
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

