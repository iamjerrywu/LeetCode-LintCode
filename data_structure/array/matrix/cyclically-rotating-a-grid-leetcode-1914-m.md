# Cyclically Rotating a Grid (LeetCode 1914) (M)

## Problem

You are given an `m x n` integer matrix `grid`​​​, where `m` and `n` are both **even** integers, and an integer `k`.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png)

A cyclic rotation of the matrix is done by cyclically rotating **each layer** in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the **counter-clockwise** direction. An example rotation is shown below:![](https://assets.leetcode.com/uploads/2021/06/22/explanation\_grid.jpg)

Return _the matrix after applying _`k` _cyclic rotations to it_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/06/19/rod2.png)

```
Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png) ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png) ![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png)

```
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `2 <= m, n <= 50`
* Both `m` and `n` are **even** integers.
* `1 <= grid[i][j] <= 5000`
* `1 <= k <= 109`

## Solution - Simulation

* For a given **k**, if k is greater than the number of elements in a particular layer, then we must rotate it `k%total_layer_elements` times.
* In order to rotate a layer, we use `top, bottom, left & right` pointers to do a **clockwise traversal**, while at every-step, assigning the next element to the current one.
* This will take care of all the elements except the element at index `{top+1, left}`, so before starting our current rotation, we store the current value of layer's **top left corner element** in `temp`, so as to assign it to `{top+1, left}` at the end of current layer's rotation.
* After rotating the current layer `k%total_layer_elements` times, we move on to the next inner layer by doing `top++, left++, bottom--, right--.`
* Total elements in each layer will be `2*(bottom-top+1) + 2*(right-left+1) - 4`. We subtract 4 as we're counting each corner element twice due to the multiplication part of the above expression, hence, we must subtract them once.

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        top, left = 0, 0
        bottom, right = m - 1, n - 1
        
        while top < bottom and left < right:
            layer_ele_cnt = 2 * (bottom - top + 1) + 2 * (right - left + 1) - 4
            rotation = k%layer_ele_cnt
            
            for _ in range(0, rotation):
                tmp = grid[top][left]
                
                for j in range(left, right):
                    grid[top][j] = grid[top][j + 1]
                for i in range(top, bottom):
                    grid[i][right] = grid[i + 1][right]
                for j in range(right, left, -1):
                    grid[bottom][j] = grid[bottom][j - 1]
                for i in range(bottom, top, - 1):
                    grid[i][left] = grid[i - 1][left]
                
                grid[top + 1][left] = tmp
            top+=1
            bottom-=1
            left+=1
            right-=1
        return grid
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
