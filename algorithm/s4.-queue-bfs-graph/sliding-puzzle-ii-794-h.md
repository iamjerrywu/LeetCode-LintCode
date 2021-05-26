# Sliding Puzzle II 794 \(H\)

## Problem

On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.

If it is impossible to move from initial state to final state, return -1.Example

**Example 1:**

```text
Input:[ [2,8,3], [1,0,4], [7,6,5]][ [1,2,3], [8,0,4], [7,6,5]]Output:4Explanation:[                 [ [2,8,3],          [2,0,3], [1,0,4],   -->    [1,8,4], [7,6,5]           [7,6,5]]                 ][                 [ [2,0,3],          [0,2,3], [1,8,4],   -->    [1,8,4], [7,6,5]           [7,6,5]]                 ][                 [ [0,2,3],          [1,2,3], [1,8,4],   -->    [0,8,4], [7,6,5]           [7,6,5]]                 ][                 [ [1,2,3],          [1,2,3], [0,8,4],   -->    [8,0,4], [7,6,5]           [7,6,5]]                 ]
```

**Example 2：**

```text
Input:[[2,3,8],[7,0,5],[1,6,4]][[1,2,3],[8,0,4],[7,6,5]]Output:-1
```

Challenge

* How to optimize the memory?
* Can you solve it with A\* algorithm?

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)

        queue = collections.deque([source])
        distance = {source: 0}

        while queue:
            curt = queue.popleft()
            if curt == target:
                return distance[curt]
            
            for next in self.get_next(curt):
                if next in distance:
                    continue

                queue.append(next)
                distance[next] = distance[curt] + 1
        return -1
    
    def matrix_to_string(self, state):
        str_list = []
        for i in range(3):
            for j in range(3):
                str_list.append(str(state[i][j]))
        return "".join(str_list)

    def get_next(self, state):
        states = []
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
        
        zero_index = state.find('0')
        x, y = zero_index//3, zero_index%3

        for i in range(4):
            x_, y_ = x + direction[i][0], y + direction[i][1]
            # should within range
            if 0 <= x_ < 3 and 0 <= y_ < 3:
                next_state = list(state)
                next_state[x * 3 + y] = next_state[x_ * 3 + y_]
                next_state[x_ * 3 + y_] = '0'
                states.append("".join(next_state))
        
        return states
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

