# Consecutive Number Sum 1439 (H)

## Problem

Given a positive integer `N`, how many groups of continuous positive integers satisfy that the sum of all numbers is `N`?

`1 <= N <= 10 ^ 9`.Example

**Example 1:**

```
Input: 5Output: 2Explanation: 5 = 5 = 2 + 3
```

**Example 2:**

```
Input: 9Output: 3Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
```

**Example 3:**

```
Input: 15Output: 4Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
```

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param N: an integer
    @return: how many ways can we write it as a sum of consecutive positive integers
    """
    def consecutiveNumbersSum(self, N):
        # Write your code here
        res = 0
        for i in range(N + 1):
            if self.have_consecutive(N, i):
                res+=1
        
        return res
    
    def have_consecutive(self, N, num):
        for start in range(N, -1 + num, -1):
            total = 0
            for j in range(num):
                total += start - j
            if total == N:
                return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^3)**
* **Space Complexity: O(1)**

## Solution - Factorization

![](<../../.gitbook/assets/Screen Shot 2021-07-10 at 1.34.00 PM.png>)

![](<../../.gitbook/assets/Screen Shot 2021-07-10 at 1.34.51 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param N: an integer
    @return: how many ways can we write it as a sum of consecutive positive integers
    """
    def consecutiveNumbersSum(self, N):
        # Write your code here
        res = 0
        upper_bnd = int(math.sqrt(2*N + 0.25) - 0.5)
        for k in range(1, upper_bnd + 1):
            if (N - k * (k + 1) / 2) % k == 0:
                res+=1
        return res
```
{% endtab %}

{% tab title="Untitled" %}
```python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        # amount upper bound (lenght of longest consecutive positive numbers)
        # appears in case like 1,2,3,4......
        # Therefore, (1 + 1 + upper - 1) * (upper - 1) = 2n
        # upper = sqrt(2 * n - 1)
        ans = 0
        for a in range(1, int(sqrt(2 * n - 1)) + 1):
            if self.is_int(a, n):
                ans+=1
        return ans
    
        # m: i s the min value
        # a: is the total consecutive numbers
        # (m + m + a - 1) * a = 2n
        # m = (2n - a - a^2)/2*a
        # amount from range 1.......upper bound, and m (min value) must > 1
    def is_int(self, amount, n):
        min_val = (2 * n + amount - amount**2)/(2 * amount)
        if min_val == int(min_val) and min_val > 0:
            return True
        return False
    
       
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(logn)**
* **Space Complexity: O(1)**



