# Climbing Stairs 111 \(E\)

## Problem

You are climbing a stair case. It takes **n** steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?Example

```text
Example 1:
	Input:  n = 3
	Output: 3
	
	Explanation:
	1) 1, 1, 1
	2) 1, 2
	3) 2, 1
	total 3.


Example 2:
	Input:  n = 1
	Output: 1
	
	Explanation:  
	only 1 way.
```

## Solution - Top Down Search 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        memory = {}
        res = self.search(n, memory)
        return res
    def search(self, n, memory):
        if n in memory:
            return memory[n]
        if n < 3:
            return n
        res = self.search(n - 1, memory) + self.search(n - 2, memory)
        memory[n] = res
        return res
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

\*\*\*\*

## Solution - Top Down Search with Memoization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        # memoization
        memory = {}
        res = self.search(n, memory)
        return res
    def search(self, n, memory):
        if n in memory:
            return memory[n]
        if n < 3:
            return n
        res = self.search(n - 1, memory) + self.search(n - 2, memory)
        memory[n] = res
        return res
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

\*\*\*\*

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n < 3:
            return n
        
        # dp[i]: the total solutions num for first ith number
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
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

\*\*\*\*

## Solution - DP with Strolling Arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n < 3:
            return n
        # dp solution (strolling array optimization)
        # dp[i]: the total solutions num for first ith number
        dp = [0] * (3)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i%3] = dp[(i - 1)%3] + dp[(i - 2)%3]
        return dp[n%3]
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

\*\*\*\*

## Solution - Top Down Search 

### Code

{% tabs %}
{% tab title="python" %}
```python

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

