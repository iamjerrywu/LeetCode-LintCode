# Bricks Falling When Hit

## Problem

We have a grid of `1` and `0`; the `1` in a cell represent bricks. A brick will not drop if and only if it is directly connected to the bottom of the grid, or at least one of its \(4-way\) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location \(i, j\), the brick \(if it exists\) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

1. The number of rows and columns in the grid will be in the range of \[1, 200\].
2. It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
3. An erasure may refer to a location with no brick - if it does, no bricks drop.
4. It's lower when the row index is smaller - the cell whose row index is 0 connects to the bottom of the grid.

You can imagine all the bricks are on the same plane. The bricks at the bottom of the grid are connected to a wall and remain undropped. If a brick drops, it will disappear.Example

**Example 1:**

```text
Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]Output: [2]Explanation: If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
```

**Example 2:**

```text
Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]Output: [0,0]Explanation: When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.num_of_set = 0
    
    def add(self, point):
        if point in self.father:
            return 
        self.father[point] = point
        self.size_of_set[point] = 1
        self.num_of_set+=1
    
    def find(self, point):
        root = point
        while root != self.father[root]:
            root = self.father[root]
        while root != point:
            original_father = self.father[point]
            self.father[point] = root
            point = original_father
        return root
    
    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size_of_set[root_b]+=self.size_of_set[root_a]
            self.num_of_set-=1
    
    def is_connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def get_size_of_set(self, point):
        return self.size_of_set[self.find(point)]

class Solution:
    """
    @param grid: a grid
    @param hits: some erasures order
    @return: an array representing the number of bricks that will drop after each erasure in sequence
    """
    def __init__(self):
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.WALL = (-1, -1)
    
    def initialization(self, grid, hits, uf):
        n, m = len(grid), len(grid[0])

        # erase all the bricks
        for hit in hits:
            grid[hit[0]][hit[1]]-=1
        
        # store the exised bricks into uf
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    uf.add((i, j))
        # add the wall as well
        uf.add(self.WALL)

        # merge those bricks attached to wall with the wall
        for j in range(m):
            if grid[0][j] == 1:
                uf.merge((0, j), self.WALL)
        
        # merge all bricks with their neighbors
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf, i, j, grid)

    def hitBricks(self, grid, hits):
        # Write your code here
        uf = UnionFind()
        fallen_bricks = [0] * len(hits)

        self.initialization(grid, hits, uf)

        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            grid[x][y] +=1
            # if after filled up is not 1, means it changed from -1 -> 0
            # which means originally it's actually an blank space w/o brick, so skip it
            if grid[x][y] != 1:
                continue
            
            before = uf.get_size_of_set(self.WALL)
            uf.add((x, y))
            self.merge_neighbors(uf, x, y, grid)
            # if it adds to wall, still need to merge with wall
            if x == 0:
                uf.merge((0, y), self.WALL)
            
            if uf.is_connected((x, y), self.WALL):
                after = uf.get_size_of_set(self.WALL)
                fallen_bricks[i] = max(0, after - before - 1)
            else:
                fallen_bricks[i] = 0
        return fallen_bricks
    
    def merge_neighbors(self, uf, x, y, grid):
        for dx, dy in self.DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if self.is_valid(new_x, new_y, grid):
                uf.merge((x, y), (new_x, new_y))
    
    def is_valid(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        return grid[x][y] == 1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.num_of_set = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = x
        self.size_of_set[x] = 1
        self.num_of_set += 1

    def find(self, x):
        path = []
        while x is not self.father[x]:
            path.append(x)
            x = self.father[x]
        for p in path:
            self.father[p] = x 
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x is not root_y:
            self.father[root_y] = root_x
            self.num_of_set -= 1 
            self.size_of_set[root_x] += self.size_of_set[root_y]
        
    def is_connected(self, x, y):
        return self.find(x) is self.find(x)

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]
class Solution:

    def __init__(self):
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.WALL = (-1, -1)

    def initialization(self, grid, hits, uf):
        n, m = len(grid), len(grid[0])
        
        # 敲掉所有的砖块
        for hit in hits:
            grid[hit[0]][hit[1]] -= 1 
        
        # 将存在的转块和墙加入并查集
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    uf.add((i, j))
        uf.add(self.WALL)

        #将直接贴墙的砖块合并到墙上
        for j in range(m):
            if grid[0][j] == 1:
                uf.union((0, j), self.WALL)
        
        # 将所有砖块和他们的邻居合并
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf, i, j, grid)
    def hitBricks(self, grid, hits):
        uf = UnionFind()
        fallen_bricks = [0] * len(hits)

        self.initialization(grid, hits, uf)
        # 按逆序填补砖块
        for i in range(len(hits) - 1, -1, -1):
            # 填补后是0， 说明本来就没有砖块
            x, y = hits[i][0], hits[i][1]
            grid[x][y] += 1
            if grid[x][y] != 1:
                continue
            # 填补前计算贴墙的砖块
            before = uf.get_size_of_set(self.WALL)
            uf.add((x, y))
            self.merge_neighbors(uf, x, y, grid)
            if x == 0:
                uf.union((0, y), self.WALL)
            
            if uf.is_connected((x, y), self.WALL):
                after = uf.get_size_of_set(self.WALL)
                fallen_bricks[i] = max(0, after - before - 1) 
            else:
                fallen_bricks[i] = 0 
        return fallen_bricks

    def merge_neighbors(self, uf, x, y, grid):
        for dx, dy in self.DIRECTIONS:
            x_, y_ = x + dx, y + dy 
            if not self.is_valid(x_, y_, grid):
                continue
            uf.union((x, y), (x_, y_))

    def is_valid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
```

