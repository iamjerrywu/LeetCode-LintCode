# Largest Rectangle in Histogram 122 (H)

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return _the area of the largest rectangle in the histogram_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
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

* **Time Complexity: O(n^3)**
* **Space Complexity: O(1)**

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

* **Time Complexity: O(n^2)**
* **Space Complexity: O(1)**

## Solution - Monotonic Stack

Characteristic for monotonic stack is that the first value smaller than cur value in left/right.

Since we try to enumerate the max height, which means the max retangle can be find at height\[i]. Therefore, toward left, and toward right, we need to find the first element that's smaller than it.

Example of illustrating L list / R list&#x20;

![](<../../../.gitbook/assets/Screen Shot 2021-06-17 at 10.56.21 AM.png>)

Example here:

![](<../../../.gitbook/assets/Screen Shot 2021-06-17 at 11.24.10 AM.png>)

![](<../../../.gitbook/assets/Screen Shot 2021-06-17 at 11.24.51 AM.png>)

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
        
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n + 1):
            # set speical value -1, for heights[n]
            value = -1 if i == n else heights[i]
            # should be ascending
            while stack and heights[stack[-1]] > value:
                top = stack.pop(-1)

                left = stack[-1] if stack else -1
                # i would be the first one smaller than cur on the right side
                width = i - left - 1
                max_area = max(max_area, width * heights[top])
            stack.append(i)
        return max_area
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****

## Solution&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-10-12 at 12.24.29 AM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        up_stack = []
        ans = 0
        ans = 0
        for i, height in enumerate(heights + [0]):
            while up_stack and heights[up_stack[-1]] > height:
                prev_height = heights[up_stack.pop()]
                
                # if no stack, means the prev height is the lowest one among all the heigh traversed so far
                if not up_stack:
                    width = i
                else:
                    width = i - up_stack[-1] - 1
                ans = max(ans, prev_height * width)
            up_stack.append(i)
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
