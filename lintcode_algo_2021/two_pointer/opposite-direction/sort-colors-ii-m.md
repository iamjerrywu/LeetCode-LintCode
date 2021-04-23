# Sort Colors II 143 \(M\)

## Problem

Given an array of _n_ objects with _k_ different colors \(numbered from 1 to k\), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

1. You are not suppose to use the library's sort function for this problem.
2. `k` &lt;= `n`

Example

**Example1**

```text
Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
```

**Example2**

```text
Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
```

Challenge

A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O\(k\) extra memory. Can you do it O\(logk\) using extra memory?

## Solution

Binary search on the colors, then do the quick select on the colors. 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sort(colors, 1, k, 0, len(colors) - 1)
    
    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
        
        color = (color_from + color_to)//2
        
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left+=1
            while left <= right and colors[right] > color:
                right-=1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left+=1
                right-=1
        
        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

