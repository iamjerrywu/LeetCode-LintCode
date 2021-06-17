# Largest Rectangle in Histogram 122 \(H\)

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return _the area of the largest rectangle in the histogram_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```text
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```text
Input: heights = [2,4]
Output: 4
```

**Constraints:**

* `1 <= heights.length <= 105`
* `0 <= heights[i] <= 104`

## Solution - Enumeration Brute Force no optimization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
        
        max_area, n = 0, len(heights)
        for start in range(n):
            for end in range(start, n):
                height = float('inf')
                for i in range(start, end + 1):
                    height = min(height, heights[i])
                width = end - start + 1
                max_area = max(max_area, height * width)
        return max_area
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^3\)**
* **Space Complexity: O\(1\)**

## Solution - Enumeration Brute Force with optimization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
        
        max_area, n = 0, len(heights)
        for start in range(n):
            height = float('inf')
            for end in range(start, n):
                height = min(height, heights[end])
                width = end - start + 1
                max_area = max(max_area, height * width)
        return max_area
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

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

