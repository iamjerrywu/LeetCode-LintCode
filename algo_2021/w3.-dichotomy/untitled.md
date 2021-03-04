# 1807. Fibonacci \(E\)

## Problem

[https://www.lintcode.com/problem/415](https://www.lintcode.com/problem/415)

#### Description

Find the _N_th number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

* The first two numbers are 0 and 1.
* The _i_ th number is the sum of _i_-1 th number and _i_-2 th number.

The first ten numbers in Fibonacci sequence is:

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...`

{% hint style="info" %}
The _N_th fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.
{% endhint %}

### Example

```text
Example 1:
	Input:  1
	Output: 0
	
	Explanation: 
	return the first number in  Fibonacci sequence .

Example 2:
	Input:  2
	Output: 1
	
	Explanation: 
	return the second number in  Fibonacci sequence .
```

## Approach: Pure Recursive

### Intuition:

Recursively thinking

### Algorithm: 

Since _i_ th number is the sum of _i_-1 th number and _i_-2 th number, apply recursive algorithm exception the first 2 elements

#### Step by step: 

* For n&lt;=2, answer = n - 1
* Rest of res = sum of i-1th number and i-2th number

### Code

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        return self.fibonacci(n - 2) + self.fibonacci(n - 1)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** **O\(2^n\)**
  * The slowest way because it takes exponential time. The amount of operations needed for each level of recursion, grows exponentially as depth approaches N. 
* **Space Complexity: O\(N\)**
  * We need space proportionate to `N` to account for the max size of the stack, in memory. This stack keeps track of the function calls to `fib(N)`. This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a `StackOverflowError`

## Approach: Memoization

### Intuition:

Improve recursion by using iteration, still solving for all sub-problems and returning answer for N, using already computed Fibonacci values. 

### Algorithm: 

Using data structure \(hashmap, or array\) to store the memorized fibonacci number, then use iteration to find the Nth value

#### Step by step: 

* For n&lt;=2, answer = n - 1
* Otherwise, iterate through N, and storing each computed answer in dictionary along the way
* Use this array as reference to 2 previous numbers to calculate the current fibonacci number
* Eventually reach last number and return 

### Code

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        return self.memoize(n)
        
    def memoize(self, n):
        # init memory
        cache = {1:0, 2:1}
        for i in range(3, n + 1):
            # implement memory 
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** **O\(n\)**
  * Each number, starting at 2 up to and including `N`, is visited, computed and then stored for O\(1\)O\(1\) access later on.
* **Space Complexity: O\(N\)**
  * The size of the data structure is proportionate to `N`

## Approach: Iterative Top-Down Approach 

### Intuition:

Iteratively thinking 

### Algorithm: 

Since _i_ th number is the sum of _i_-1 th number and _i_-2 th number, apply iteration except for the first 2 elements

#### Step by step: 

* For n&lt;=2, answer = n - 1
* Rest of the numbers \(loop from 3 ~ n-1\): cur = \(cur-2\)th + \(cur-1\)th

### Code

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        
        pre_2, pre_1, cur = 0, 1, 1
        
        for i in range(3, n + 1):
            cur = pre_2 + pre_1
            pre_2 = pre_1
            pre_1 = cur
        return cur
```
{% endtab %}

{% tab title="Python \(optimized\)" %}
```python
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** **O\(n\)**
  * Each value from `2 to N` will be visited at least once. The time it takes to do this is directly proportionate to `N` where `N` is the `Fibonacci Number` we are looking to compute.
* **Space Complexity: O\(1\)**
  * Constant space complexity





