# Robot Bounded In Circle \(LeetCode1041\) \(M\)

## Problem

On an infinite plane, a robot initially stands at `(0, 0)` and faces north. The robot can receive one of three instructions:

* `"G"`: go straight 1 unit;
* `"L"`: turn 90 degrees to the left;
* `"R"`: turn 90 degrees to the right.

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.

**Example 1:**

```text
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
```

**Example 2:**

```text
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
```

**Example 3:**

```text
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
```

**Constraints:**

* `1 <= instructions.length <= 100`
* `instructions[i]` is `'G'`, `'L'` or, `'R'`.

## Solution 

```python
MOVE = {0:[0, 1], 1:[1,0], 2:[0, -1], 3:[-1, 0]}

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0
        for instruction in instructions:
            if instruction == 'L':
                direction = (direction + 3)%len(MOVE)
            elif instruction == 'R':
                direction = (direction + 1)%len(MOVE)
            else:
                x+=MOVE[direction][0]
                y+=MOVE[direction][1]
        # after the sequnce of instruction, if follinwg condition match, means have cycle
        # 1. if it ended in origin
        # 2. it it ended in direction other than north 
        # (if ended north and not in origin, would have diff distance after every round
        return (x == 0 and y == 0) or direction != 0
```

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

