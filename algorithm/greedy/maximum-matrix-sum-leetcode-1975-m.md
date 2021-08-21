# Maximum Matrix Sum \(LeetCode 1975\) \(M\)

## Problem

You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:

* Choose any two **adjacent** elements of `matrix` and **multiply** each of them by `-1`.

Two elements are considered **adjacent** if and only if they share a **border**.

Your goal is to **maximize** the summation of the matrix's elements. Return _the **maximum** sum of the matrix's elements using the operation mentioned above._

**Example 1:**![](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png)

```text
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png)

```text
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
```

**Constraints:**

* `n == matrix.length == matrix[i].length`
* `2 <= n <= 250`
* `-105 <= matrix[i][j] <= 105`

## Solution - Greedy

Recognize that if there is an even amount of negative numbers, you can eliminate all the negatives signs in the following fashion:

* If there is a pair of adjacent negative numbers, just remove both negative signs
* If the remaining negative numbers are separated from each other, just **swap** their negative signs with the adjacent positive number until they are adjacent to each other, and then you can remove 2 negative signs at a time

If there is an odd amount of negative sign, there will be a negative sign in the end, and we can move that negative sign to the smallest number in the matrix \(by _swapping_ as above\)

**So, if the number of negative signs is even, the answer is the sum of the absolute value of all elements. If it is odd, we will have to minus 2 times the number with smallest absolute value \(**_**for we have to change `+` sign to `-`**_**\) to get the answer:**

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        neg_cnt = 0
        min_val = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans+=abs(matrix[i][j])
                if matrix[i][j] < 0:
                    neg_cnt+=1
                min_val = min(min_val, abs(matrix[i][j]))
        if neg_cnt%2 == 0:
            return ans
        else:
            return ans - min_val * 2
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

