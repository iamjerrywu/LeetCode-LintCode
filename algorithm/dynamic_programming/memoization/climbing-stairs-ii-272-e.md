# Climbing Stairs II 272 (E)

## Problem

A child is running up a staircase with `n` steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

For `n=0`, we think the answer is 1.Example

**Example 1:**

```
Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
```

**Example 2:**

```
Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
```

## Solution - Memoization&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        
        if n == 0:
            return 1
        if n < 3:
            return n
        if n == 3:
            return 4
        memory = {}
        return self.search(n, memory)
    
    def search(self, n, memory):
        if n in memory:
            return memory[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        total = self.search(n - 1, memory) + self.search(n - 2, memory) + self.search(n - 3, memory) 
        memory[n] = total
        return memory[n]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        
        if n == 0:
            return 1
        if n < 3:
            return n
        if n == 3:
            return 4

        # dp[i]: the total solutions for first ith numbers
        dp = [0] * (n + 1)
        
        # init
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****

## Solution - DP with Strolling Array

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        
        if n == 0:
            return 1
        if n < 3:
            return n
        if n == 3:
            return 4

        # dp[i]: the total solutions for first ith numbers
        dp = [0] * 4
        
        # init
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i%4] = dp[(i - 1)%4] + dp[(i - 2)%4] + dp[(i - 3)%4]
        return dp[n%4]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
