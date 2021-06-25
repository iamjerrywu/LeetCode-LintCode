# Test Strategy 273 \(M\)

## Problem

You have an exam, which lasts **120 minutes**. There are multiple questions on the exam, and your answer order is not limited. There are three different strategies you can choose from for the question `i`:

1. Skip this question and get 0 points for no time.
2. Just do part of the problem. You would spend `p[i]` minutes and get `part[i]` points.
3. Do the whole problem. You would spend `f[i]` minutes and get `full[i]` points.

Given four arrays in turn: `p`, `part`, `f`, `full`, calculate the **maximum** number of points you can get.

The number of examination questions is no more than 200 and at least 1.  
Time spent on each question: 1 ≤ `p[i]` ≤ `f[i]` ≤ 120  
Score of each question: 1 ≤ `part[i]` ≤ `full[i]` ≤ 100  
We will run your code for 20times,. please ensure that you don't change the param in your function.Example

**Sample 1:**  
Input sample: p=\[20,50,100,5\], part=\[20,30,60,3\], f=\[100,80,110,10\], full=\[60,55,88,6\]  
Output sample: 94  
Sample explanation: Of all the choices, choosing to complete the whole question 3 and the whole question 4 has the highest score. The whole of question 3 took 110 minutes to get 88 points, and the whole of question 4 took 10 minutes to get 6 points, so it took 120 minutes to get 94 points altogether.

**Sample 2:**  
Input sample: p=\[60,60\], part=\[30,30\], f=\[100,120\], full=\[40,60\]  
Output sample: 60  
Sample explanation: You can choose doing part of the problem 1 and 2 or doing the whole of question 2. Either way you can get a maximum of 60 points in 120 minutes .

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
MAX_TIME = 120
class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        # write your 
        n = len(p) # total problem's amount
        
        # init dp state
        # dp[i][j] = the score you can get in the first ith problem spending j time
        dp = [[0] * (MAX_TIME + 1) for _ in range(n + 1)]
        

        # 1. do partial: part = dp[i - 1][j - p[i - 1]] + part[i - 1]
        # 2. do full:    full = dp[i - 1][j - f[i - 1]] + full[i - 1]
        # 3. dp[i][j] = max(part, fall, dp[i - 1][j])

        for i in range(1, n + 1):
            for j in range(1, MAX_TIME + 1):
                
                # 0. if not doing any
                dp[i][j] = dp[i - 1][j]

                # 1. if ith problem only do partial
                if (j < p[i - 1]):
                    continue
                dp[i][j] = max(dp[i][j], dp[i -1][j - p[i - 1]] + part[i - 1])

                # 2. if ith problem do full
                if (j < f[i - 1]):
                    continue
                dp[i][j] = max(dp[i][j], dp[i -1][j - f[i - 1]] + full[i - 1])
        return dp[n][MAX_TIME]




```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* max\_tim\)**
* **Space Complexity: O\(n \* max\_time\)**

## Solution - Strolling Arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
MAX_TIME = 120
class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        # write your 
        n = len(p) # total problem's amount
        
        # init dp state
        # dp[i][j] = the score you can get in the first ith problem spending j time
        dp = [[0] * (MAX_TIME + 1) for _ in range(2)]
        

        # 1. do partial: part = dp[i - 1][j - p[i - 1]] + part[i - 1]
        # 2. do full:    full = dp[i - 1][j - f[i - 1]] + full[i - 1]
        # 3. dp[i][j] = max(part, fall, dp[i - 1][j])

        for i in range(1, n + 1):
            for j in range(1, MAX_TIME + 1):
                
                # 0. if not doing any
                dp[i%2][j] = dp[(i - 1)%2][j]

                # 1. if ith problem only do partial
                if (j < p[i - 1]):
                    continue
                dp[i%2][j] = max(dp[i%2][j], dp[(i -1)%2][j - p[i - 1]] + part[i - 1])

                # 2. if ith problem do full
                if (j < f[i - 1]):
                    continue
                dp[i%2][j] = max(dp[i%2][j], dp[(i -1)%2][j - f[i - 1]] + full[i - 1])
        return dp[n%2][MAX_TIME]




```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* max\_time\)**
* **Space Complexity: O\(max\_time\)**

