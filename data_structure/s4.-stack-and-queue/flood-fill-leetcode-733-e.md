# Flood Fill (LeetCode 733) (E)

## Problem

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `newColor`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `newColor`.

Return _the modified image after performing the flood fill_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

**Example 2:**

```
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

{% tab title="C++" %}
<pre class="language-cpp"><code class="lang-cpp"><strong>class Solution {
</strong>public:
    vector&#x3C;int> dx = {0, 1, 0, -1};
    vector&#x3C;int> dy = {1, 0, -1, 0};
    vector&#x3C;vector&#x3C;int>> floodFill(vector&#x3C;vector&#x3C;int>>&#x26; image, int sr, int sc, int color) {
        int start_color = image[sr][sc];
        if (start_color == color)
            return image;
        image[sr][sc] = color;
        deque&#x3C;pair&#x3C;int, int>> deq;
        deq.push_back(pair(sr, sc));
        bfs(deq, image, start_color, color);
        return image;
    }

private:
    void bfs(deque&#x3C;pair&#x3C;int, int>> deq, vector&#x3C;vector&#x3C;int>> &#x26;image, int start_color, int color) {
        while(!deq.empty()) {
            pair&#x3C;int, int> cur = deq.front();
            deq.pop_front();
            for (int i = 0; i &#x3C; dx.size(); i++) {
                int new_x = cur.first + dx[i];
                int new_y = cur.second + dy[i];
                if (is_valid(new_x, new_y, image, start_color)) {
                    image[new_x][new_y] = color;
                    deq.push_back(pair(new_x, new_y));
                    bfs(deq, image, start_color, color);
                }
            }
        }
    }

    bool is_valid(int x, int y, vector&#x3C;vector&#x3C;int>> &#x26;image, int start_color) {
        if (0 &#x3C;= x and x &#x3C; image.size() and 0 &#x3C;= y and y &#x3C; image[0].size()) {
            return image[x][y] == start_color;
        }
        return false;
    }
};
</code></pre>
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O(n)**
* **Space Complexity:  O(n)**



## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        image[sr][sc] = newColor
        self.dfs(sr, sc, start_color, newColor, image)
        return image
    
    def dfs(self, x, y, start_color, new_color, image):
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y, image, start_color):
                image[new_x][new_y] = new_color
                self.dfs(new_x, new_y, start_color, new_color, image)

    def is_valid(self, x, y, image, start_color):
        if 0 <= x < len(image) and 0 <= y < len(image[0]):
            return image[x][y] == start_color
        return False
```
{% endtab %}

{% tab title="C++" %}
````cpp
class Solution {
public:
    vector<int> dx = {0, 1, 0, -1};
    vector<int> dy = {1, 0, -1, 0};
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int start_color = image[sr][sc];
        if (start_color == color)
            return image;
        image[sr][sc] = color;
        dfs(sr, sc, image, start_color, color);
        return image;
    }

private:
    void dfs(int x, int y, vector<vector<int>> &image, int start_color, int color) {
        for (int i = 0; i < dx.size(); i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (is_valid(new_x, new_y, image, start_color)) {
                image[new_x][new_y] = color;
                dfs(new_x, new_y, image, start_color, color);
            }
        }
    }

    bool is_valid(int x, int y, vector<vector<int>> &image, int start_color) {
        if (0 <= x and x < image.size() and 0 <= y and y < image[0].size()) {
            return image[x][y] == start_color;
        }
        return false;
    }
};
```
````
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O(n)**
* **Space Complexity:  O(n)**
