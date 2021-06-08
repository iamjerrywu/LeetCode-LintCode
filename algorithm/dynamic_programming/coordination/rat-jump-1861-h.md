# Rat Jump 1861 \(H\)

## Problem

There is a mouse jumping from the top of a staircase with height `n`. This mouse can jump 1, 3 or 4 steps in an even number of jumps and 1, 2, or 4 steps in an odd number of times. Some steps have glue,if the mouse jump those steps,it will be directly stuck and cannot continue to jump.You need to solve how many ways the mouse can reach the ground \( level 0 \) from the top of this staircase.It also can be reached if it exceeds the ground. For example, jumping from 1 to -1 is another plan for jumping from 1 to 0.The state of the stairs with or without glue is input from high to low, that is, `arr[0]` is the top of the stairs.  
`arr[i] == 0` represents that there is no glue on the i-th position, `arr[i] == 1` represents that there is glue on the i-th position.

2&lt;=n&lt;=50000  
arr\[i\]=1 means there is glue on the step, 0 means there is no glue  
The input guarantees the highest steps and the lowest is 0  
The answer needs to be modulo by 1e9 + 7Example

**Example1:**

```text
Input:[0,0,0]Output:5Explanation:There are 3 steps.The step 2  is the starting point without glue.Step 1, no glue.Step 0, no glue.The mouse jump plans is:2--odd(1)-->1--even(1)-->02--odd(1)-->1--even(3)-->-22--odd(1)-->1--even(4)-->-32--odd(2)-->02--odd(4)-->-2
```

**Example2:**

```text
Input:[0,0,1,0]Output:3Explanation:There are 4 steps.The step 3  is the starting point without glue.Step 2, no glue.Step 1, have glue.Step 0, no glue.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
MOD = 10**9 + 7
class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    def ratJump(self, arr):
        # Write your code here.
        
        n = len(arr)
        
        # dp state: dp[i][0]: total solutions that from 0 jump even steps to reach ith position
        #           dp[i][1]: total solutions taht from 0 jump odd steps to reach ith position
        dp = [[0, 0] for _ in range(n)]

        # init: begin at position 0, and jump 0 steps (even)

        dp[0][0] = 1

        even_jumps = [1, 3, 4]
        odd_jumps = [1,2,4]

        # function: dp[i][0] = dp[i - 1][1] + dp[i - 3][1] + dp[i - 4][1]
        #           dp[i][1] = dp[i - 1][0] + dp[i - 2][0] + dp[i - 4][0]
        for i in range(1, n - 1):
            # can't jump
            if arr[i] == 1:
                continue
            for jump in even_jumps:
                if i - jump >= 0:
                    dp[i][0] = (dp[i][0] + dp[i - jump][1]) % MOD
            for jump in odd_jumps:
                if i - jump >= 0:
                    dp[i][1] = (dp[i][1] + dp[i - jump][0]) % MOD
        
        # ans:
        # accumulate the solutions
        # notice that since destination exceed n - 1 can also be count as solution
        # example: if last jump = 3
        # the valid range of previous jump would be (n-1-jump  ~  n-1-1
        ans = 0
        for jump in even_jumps:
            for i in range(max(0, n - jump - 1), n - 1):
                ans = (ans + dp[i][1]) % MOD
        for jump in odd_jumps:
            for i in range(max(0, n - jump - 1), n - 1):
                ans = (ans + dp[i][0]) % MOD
        
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

