# Lake Escape 1828 \(H\)

## Problem

Albert is stranded on a frozen lake. He is currently on a snowbank that gives him some traction. but once he steps the ice, he will slide in the same direction until he hits another snowbank. There are also treacherous holes in the ice that he must avoid.

As a cruel twist of fate, Albert's young pup, Kuna, is also stranded, but on a different snowbank. Can Albert reach his pup AND make it to shore?

Albert can only move horizontally and vertically. He makes it to shore by leaving the lake grid.

The input contains these parameters:

* side\_length: the length of a side of the lake \(it's a square\)
* lake\_grid: a 2D matrix representing the lake 0 = ice, 1 = snowbank, -1 = hole
* albert\_row: row of Alber'ts snowbank
* albert\_column: column of Albert's snowbank
* kuna\_row: row of Kuna's snowbank
* kuna\_column: column of Kuna's snowbank

It is guaranteed \|albert\\_row-kuna\\_row\|+\|albert\\_column- kuna\\_column\|&gt;0∣albert\_row−kuna\_row∣+∣albert\_column−kuna\_column∣&gt;0。Example

**Example 1:**

```text
Input:7[[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,1,-1,0,-1,0],[-1,0,1,0,0,0,0],[0,1,1,0,0,1,0],[-1,0,-1,0,-1,0,0],[0,0,0,0,0,0,0]]4132Output: trueExplanation:As it seen in the picture. Yellow ceil is Albert's location and red ceil is Kuna's location. Albert can turn right to (4,2) and up to (3,2) then turn right to leave the lake grid.
```

![&#x56FE;&#x7247;](https://media.jiuzhang.com/media/markdown/images/2/20/c06db360-53ec-11ea-ab9e-0242c0a8d005.jpg)

Challenge

Albert can't go to the shore and then find Kuna.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
class LakeType:
    ICE = 0
    SNOWBANK = 1
    HOLE = -1
class Solution:
    """
    @param side_length: the length of a side of the lake (it's a square)
    @param lake_grid: a 2D matrix representing the lake 0= ice, 1= snowbank, -1= hole 
    @param albert_row: row of Albert's snowbank
    @param albert_column: column of Albert's snowbank 
    @param kuna_row: row of Kuna's snowbank 
    @param kuna_column: column of Kuna's snowbank
    @return: a bool - whether Albert can escape
    """
    def lakeEscape(self, side_length, lake_grid, albert_row, albert_column, kuna_row, kuna_column):
        # write your code here
        n = side_length
        queue = collections.deque()
        visited = set()

        queue.append((albert_row, albert_column))
        visited.add((albert_row, albert_column))

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                # if cannot go, return (-1, -1)
                nxt_x, nxt_y = self.get_nxt_pos(x, y, dx, dy, lake_grid)

                if(nxt_x, nxt_y) == (-1, -1):
                    continue
                if (nxt_x, nxt_y) in visited:
                    continue
                # can only move when you are on snowbank
                if lake_grid[nxt_x][nxt_y] == LakeType.SNOWBANK:
                    queue.append((nxt_x, nxt_y))
                visited.add((nxt_x, nxt_y))
            
        if not self.can_escape(visited, lake_grid):
            return False
        
        if (kuna_row, kuna_column) in visited:
            return True
        return False
    
    def get_nxt_pos(self, x, y, dx, dy, lake_grid):
        n = len(lake_grid)
        while 0 <= x + dx < n and 0 <= y + dy < n:
            x+=dx
            y+=dy
            if lake_grid[x][y] == LakeType.ICE:
                continue
            if lake_grid[x][y] == LakeType.HOLE:
                return (-1, -1)
            
            break
        return (x, y)
    
    def can_escape(self, visited, lake_grid):
        n = len(lake_grid)
        for i in range(n):
            if (0, i) or (i, 0) in visited:
                return True
        return False      
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

