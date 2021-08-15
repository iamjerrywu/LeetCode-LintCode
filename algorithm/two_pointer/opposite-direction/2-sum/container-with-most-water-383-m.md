# Container With Most Water 383 \(M\)

## Problem

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

**Example 1:**![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```text
Input: height = [1,1]
Output: 1
```

**Example 3:**

```text
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:**

```text
Input: height = [1,2,1]
Output: 2
```

**Constraints:**

* `n == height.length`
* `2 <= n <= 105`
* `0 <= height[i] <= 104`

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(len(height)):
                ans = max(ans, min(height[i], height[j]) * (i - j))
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

## Solution - Two Pointers

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

