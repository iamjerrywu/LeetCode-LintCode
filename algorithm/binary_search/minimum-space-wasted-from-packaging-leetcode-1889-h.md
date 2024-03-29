# Minimum Space Wasted From Packaging (LeetCode 1889) (H)

## Problem

You have `n` packages that you are trying to place in boxes, **one package in each box**. There are `m` suppliers that each produce boxes of **different sizes** (with infinite supply). A package can be placed in a box if the size of the package is **less than or equal to** the size of the box.

The package sizes are given as an integer array `packages`, where `packages[i]` is the **size** of the `ith` package. The suppliers are given as a 2D integer array `boxes`, where `boxes[j]` is an array of **box sizes** that the `jth` supplier produces.

You want to choose a **single supplier** and use boxes from them such that the **total wasted space** is **minimized**. For each package in a box, we define the space **wasted** to be `size of the box - size of the package`. The **total wasted space** is the sum of the space wasted in **all** the boxes.

* For example, if you have to fit packages with sizes `[2,3,5]` and the supplier offers boxes of sizes `[4,8]`, you can fit the packages of size-`2` and size-`3` into two boxes of size-`4` and the package with size-`5` into a box of size-`8`. This would result in a waste of `(4-2) + (4-3) + (8-5) = 6`.

Return _the **minimum total wasted space** by choosing the box supplier **optimally**, or_ `-1` if it is **impossible** to fit all the packages inside boxes. Since the answer may be **large**, return it **modulo** `109 + 7`.

**Example 1:**

```
Input: packages = [2,3,5], boxes = [[4,8],[2,8]]
Output: 6
Explanation: It is optimal to choose the first supplier, using two size-4 boxes and one size-8 box.
The total waste is (4-2) + (4-3) + (8-5) = 6.
```

**Example 2:**

```
Input: packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
Output: -1
Explanation: There is no box that the package of size 5 can fit in.
```

**Example 3:**

```
Input: packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
Output: 9
Explanation: It is optimal to choose the third supplier, using two size-5 boxes, two size-10 boxes, and two size-14 boxes.
The total waste is (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9.
```

**Constraints:**

* `n == packages.length`
* `m == boxes.length`
* `1 <= n <= 105`
* `1 <= m <= 105`
* `1 <= packages[i] <= 105`
* `1 <= boxes[j].length <= 105`
* `1 <= boxes[j][k] <= 105`
* `sum(boxes[j].length) <= 105`
* The elements in `boxes[j]` are **distinct**.

## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        packages_space = sum(packages)
        box_space = float('inf')
        wasted_space = float('inf')
        
        for box_list in boxes:
            box_list.sort()
            # if biggest box cannot hold largest package, then continue
            if box_list[-1] < packages[-1]:
                continue
            
            pre_id, cur_id, box_space = 0, 0, 0
            
            for box in box_list:
                # if box too small for even the smallest package
                if box < packages[0]:
                    continue
                # find the id that located in the package list 
                # those left to cur_id's package can be contained in the box
                cur_id = bisect.bisect_right(packages, box)
                box_space+=(cur_id - pre_id) * box
                if cur_id >= len(packages):
                    break
                pre_id = cur_id
            wasted_space = min(wasted_space, box_space - packages_space)
        
        return wasted_space % (10 ** 9 + 7) if wasted_space != float('inf') else -
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn + mlogk)**
  * n: length of packages
  * m: length of box\_list in boxes
  * k: length of box\_list
* **Space Complexity:**
  * O(n + m)
    * Timsort()
