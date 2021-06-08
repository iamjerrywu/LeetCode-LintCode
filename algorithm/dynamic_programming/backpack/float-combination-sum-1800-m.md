# Float Combination Sum 1800 \(M\)

## Problem

Given an array of `A`, a non-negative integer `target`. Each decimal in `A` needs to be operated by ceil or floor, and finally an integer array is obtained, requiring the sum of all integers that are in the array to be equal to `target`, and requiring adjustments sum of the decimal array is minimum.  
Such as ceil\(1.2\),adjustment is 0.8,floor\(1.2\),adjustment is 0.2. return the integer array.

1.`1<=A.length<=300`

2.`0<=target<=15000`

3.`0.0<=A[i]<=100.0`

4.Datas guarantees the existence of answers.  
There are still something wrong in the c++ and python. We will fix it as soon as possible.Example

**Example 1:**

```text
Input：A=[1.2,1.3,2.3,4.2],target=9Output：[1,1,3,4]Explanation：1.2->1,1.3->1,2.3->3,4.2->4.
```

**Example 2:**

```text
Input：A=[2.5,2.5],target=5Output：[2,3]Explanation：2.5->2,2.5->3.
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: A float array
    @param target: A non-negative integer
    @return: Return an integer array which sum equals target
    """
    def getArray(self, A, target):
        # write your code here
        n = len(A)

        # state: st[i][j] means the cost for first ith number that adjust to be sum of j
        # prev[i][j] record when dp[i][j] is optimized
        # for A[i - 1], record 1 (ceil), record 0 (floor)

        dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
        prev = [[-1] * (target + 1) for _ in range(n + 1)]

        # init 
        dp[0][0] = 0

        # function: dp[i][j] = min(
        #      dp[i - 1][j - ceil] + ceil - A[i - 1],
        #      dp[i - 1][j - floor] + A[i - 1] - floor)
        # record whether do ceil / floor at the same time
        for i in range(1, n + 1):
            ceil = int(math.ceil(A[i - 1]))
            floor = int(math.floor(A[i - 1]))
            for j in range(target + 1):
                if j >= ceil and dp[i - 1][j - ceil] + ceil - A[i - 1] < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - ceil] + ceil - A[i - 1]
                    prev[i][j] = 1
                if j >= floor and dp[i - 1][j - floor] + A[i - 1] - floor < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - floor] + A[i - 1] - floor
                    prev[i][j] = 0
        
        # backtrack the answer
        ans = list(A)
        for i in range(n, 0, -1):
            if prev[i][target] == 1:
                ans[i - 1] = int(math.ceil(A[i - 1]))
            else:
                ans[i - 1] = int(math.floor(A[i - 1]))
            target-=ans[i - 1]
        
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* target\)**
* **Space Complexity: O\(n \* target\)**

{% hint style="warning" %}
Can't use strolling array to optimize the space complextiy, please in this question the answer is asked to provide the details of solution, rather that just the amount. In this case, the `prev`array cannot be optimized. Even dp arr is optimized to length of target, however prev array remain the same, so space complexity is still O\(n\*target\)
{% endhint %}

