# Rotating the Box \(LeetCode 1861\) \(M\)

## Problem

You are given an `m x n` matrix of characters `box` representing a side-view of a box. Each cell of the box is one of the following:

* A stone `'#'`
* A stationary obstacle `'*'`
* Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not** affect the stones' horizontal positions.

It is **guaranteed** that each stone in `box` rests on an obstacle, another stone, or the bottom of the box.

Return _an_ `n x m` _matrix representing the box after the rotation described above_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)

```text
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)

```text
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)

```text
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

**Constraints:**

* `m == box.length`
* `n == box[i].length`
* `1 <= m, n <= 500`
* `box[i][j]` is either `'#'`, `'*'`, or `'.'`.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box:
            return box
        for row in range(len(box)):
            self.move_to_right(box[row])     
        return self.rotate_ninety_degrees(box)
    
    def move_to_right(self, box_row):
        cnt = {}
        start = 0
        for i in range(len(box_row)):
            if box_row[i] == '*':
                # only if '*' appears later than position 1, then need to relocate
                if i > 1:
                    self.relocate(start, i - 1, box_row, cnt)
                cnt.clear()
                start = i + 1
                continue
            cnt[box_row[i]] = cnt.get(box_row[i], 0) + 1
        # check on last one, since may not encounter "*"
        self.relocate(start, i, box_row, cnt)
    
    # Relocate both the "#", "." locations
    def relocate(self, start, end, box_row, cnt):
        for obj, nums in cnt.items():
            while nums > 0:
                if obj == '.':
                    box_row[start] = obj
                    start+=1
                else:
                    box_row[end] = obj
                    end-=1
                nums-=1
            
    def rotate_ninety_degrees(self, box):
        rotate_box = [[0] * len(box) for _ in range(len(box[0]))]
        for i in range(len(box)):
            for j in range(len(box[0])):
                rotate_box[j][len(box) - i - 1] = box[i][j]
        return rotate_box
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

