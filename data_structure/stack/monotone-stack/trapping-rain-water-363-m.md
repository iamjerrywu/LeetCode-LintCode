# Trapping Rain Water 363 \(M\)

## Problem

Given _n_ non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it is able to trap after raining.

![Trapping Rain Water](https://lintcode-media.oss-us-west-1.aliyuncs.com/problem/rainwatertrap.png)Example

**Example 1:**

```text
Input: [0,1,0]Output: 0
```

**Example 2:**

```text
Input: [0,1,0,2,1,0,1,3,2,1,2,1]Output: 6
```

Challenge

O\(n\) time and O\(1\) memory

O\(n\) time and O\(n\) memory is also acceptable.

## Solution - Brute Force 

Traverse every position, and that position's possible water area would be:

* min\(right_max, leftmax\)  - heights\[i\] \* 1 \(the width\)_
* Right Max: from current position looks right, the max value
* Left Max: from current position looks left, the max value

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        res = 0
        for i in range(len(heights)):
            left_max = self.find_max(heights, i, False)
            right_max = self.find_max(heights, i, True)
            res+=min(left_max, right_max) - heights[i]
        return res
    
    def find_max(self, heights, cur, right_see):
        if right_see:
            if cur < len(heights) - 1:
                return max(max(heights[cur + 1:]), heights[cur])
            else:
                return heights[cur]
        else:
            if cur > 0:
                # WARNING! should not write as [cur - 1:-1:-1]
                return max(max(heights[cur - 1::-1]), heights[cur])
            else:
                return heights[cur]
```
{% endtab %}

{% tab title="Python" %}
```python
# Cleaner Solution!
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        area = 0
        for i in range(len(heights)):
            right_max = heights[i]
            for j in range(i + 1, len(heights)):
                right_max = max(right_max, heights[j])
            left_max = heights[i]
            for j in range(i - 1, -1, -1):
                left_max = max(left_max, heights[j])
            area += min(right_max,left_max) - heights[i]
        return area
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

{% hint style="danger" %}
In this approach, actually when finding max, we redundantly traverse the elements in list
{% endhint %}

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

