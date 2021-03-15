# 109. Triangle

## Problem

[https://www.lintcode.com/problem/128](https://www.lintcode.com/problem/128)

### Description 

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

{% hint style="info" %}
Bonus point if you are able to do this using only O\(n\) extra space, where n is the total number of rows in the triangle.
{% endhint %}

### Example

Example 1:

```text
Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
```

Example 2:

```text
Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
```

## Overview

### Triangle vs BST

#### Triangle:

* Total nodes amount: O\(n^2\)

BST:

* Total nodes amount: O\(2^n\)

## Approach

### Intuition 

Traverse all the path and calculate the sum using DFS \(recursion\)

### Algorithm

Traverse all the path and collect the minimum value

#### Step by step

* Start from top point and traverse to button
  * Recursively doing DFS
    * Next Level: X + 1
      * Have left, right path: Y / Y + 1
    * If reach the button, than update the minimum value
* Return minimum value

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        self.minimum = float('inf')
        self.traverse(triangle, 0, 0, 0)
        return self.minimum
    
    def traverse(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.minimum = min(path_sum, self.minimum)
            return 
        self.traverse(triangle, x + 1, y, path_sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1, path_sum + triangle[x][y])

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(2 ^ n\)**
  * Since this way of traverse is similar to BST traverse
    * For each layer, the total run time = 1 + 2 + 4 + 8 + ......
      * Therefore it's O\(2^n\)
* **Space Complexity: O\(A\)**
  * **A** is the length of Array





