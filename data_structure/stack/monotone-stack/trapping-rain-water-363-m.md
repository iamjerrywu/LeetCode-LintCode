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

## Solution 

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
                return max(max(heights[cur - 1::-1]), heights[cur])
            else:
                return heights[cur]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

