# Minimum Garden Perimeter to Collect Enough Apples \(LeetCode 1954\) \(M\)

## Problem

In a garden represented as an infinite 2D grid, there is an apple tree planted at **every** integer coordinate. The apple tree planted at an integer coordinate `(i, j)` has `|i| + |j|` apples growing on it.

You will buy an axis-aligned **square plot** of land that is centered at `(0, 0)`.

Given an integer `neededApples`, return _the **minimum perimeter** of a plot such that **at least**_ ****`neededApples` _apples are **inside or on** the perimeter of that plot_.

The value of `|x|` is defined as:

* `x` if `x >= 0`
* `-x` if `x < 0`

**Example 1:**![](https://assets.leetcode.com/uploads/2019/08/30/1527_example_1_2.png)

```text
Input: neededApples = 1
Output: 8
Explanation: A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.
```

**Example 2:**

```text
Input: neededApples = 13
Output: 16
```

**Example 3:**

```text
Input: neededApples = 1000000000
Output: 5040
```

**Constraints:**

* `1 <= neededApples <= 1015`

## Solution - BFS Level 

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Math

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        apples = 0
        length = 0
        start = 0
        while apples < neededApples:
            length+=2
            start+=1
            apples+=self.cal_apples(start, length)
        return length * 4
    
    def cal_apples(self, start, length):
        cnt = 0
        cnt += ((start + length)/2 * (length - start + 1))
        if length - start > 1:
            cnt += (((start + 1) + (length - 1))/2 * (length - start - 2 + 1))
        return cnt * 4
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

