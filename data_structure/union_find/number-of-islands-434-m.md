# Number of Islands II 434 \(M\)

## Problem

Given a n,m which means the row and column of the 2D matrix and an array of pair A\( size k\). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A\[i\].x, A\[i\].y means that you can change the grid matrix\[A\[i\].x\]\[A\[i\].y\] from sea to island. Return how many island are there in the matrix after each operator.You need to return an array of size K.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.Example

**Example 1:**

```text
Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]Output: [1,1,2,2]Explanation:0.  00000    00000    00000    000001.  00000    01000    00000    000002.  01000    01000    00000    000003.  01000    01000    00000    000104.  01000    01000    00000    00011
```

**Example 2:**

```text
Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]Output: [1,1,2,2]
```

## Solution - Union Find

If we use BFS here \(solution for 'Number of Islands'\), then the time complexity would be huge!

The max amount of operators can be \(n \* m\)

For every BFS operation can be O\(n \* m\), so the total time complexity can be O\(n^2 \* m ^2\), if n = m, then it would be O\(n^4\), too slow!

### Code

{% tabs %}
{% tab title="python" %}
```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_set = 0
    def add(self, point):
        self.father[point] = point
        self.num_of_set+=1
    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_of_set-=1 
    def find(self, point):
        root = point
        while root != self.father[root]:
            root = self.father[root]
        # path compresion
        while root != point:
            original_father = self.father[point]
            self.father[point] = root
            point = original_father
        return root
    def get_num_of_set(self):
        return self.num_of_set

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        if not operators:
            return []
        
        uf = UnionFind()
        islands = set()
        num_of_lands = []

        for operator in operators:
            if (operator.x, operator.y) in islands:
                num_of_lands.append(uf.get_num_of_set())
                continue

            islands.add((operator.x, operator.y))
            uf.add((operator.x, operator.y))

            for delta_x, delta_y in DIRECTIONS:
                neighbor_x = operator.x + delta_x
                neighbor_y = operator.y + delta_y

                if self.is_valid(neighbor_x, neighbor_y, n, m, islands):
                    uf.merge((operator.x, operator.y), (neighbor_x, neighbor_y))
          
            num_of_lands.append(uf.get_num_of_set())

        return num_of_lands
    
    def is_valid(self, x, y, n, m, islands):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return (x, y) in islands
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

