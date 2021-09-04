# Flood Fill \(LeetCode 733\) \(E\)

## Problem

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `newColor`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels \(also with the same color\), and so on. Replace the color of all of the aforementioned pixels with `newColor`.

Return _the modified image after performing the flood fill_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

```text
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

**Example 2:**

```text
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
```

**Constraints:**

* `m == image.length`
* `n == image[i].length`
* `1 <= m, n <= 50`
* `0 <= image[i][j], newColor < 216`
* `0 <= sr < m`
* `0 <= sc < n`

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        
        queue = collections.deque()        
        queue.append([sr, sc])
        image[sr][sc] = newColor
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, image, start_color):
                    queue.append([new_x, new_y])
                    image[new_x][new_y] = newColor
        
        return image
    
    
    def is_valid(self, x, y, image, start_color):
        if 0 <= x < len(image) and 0 <= y < len(image[0]):
            return image[x][y] == start_color
        return False
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(n\)**
* **Space Complexity:  O\(n\)**

