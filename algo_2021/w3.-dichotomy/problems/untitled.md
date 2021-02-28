# 365. Fibonacci \(N\)

## Problem

[https://www.lintcode.com/problem/415](https://www.lintcode.com/problem/415)

#### Description

中文

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

\`\`

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

## Approach: Iterative Top-Down Approach 

### Intuition:

Iteratively thinking 

### Algorithm: 

Since _i_ th number is the sum of _i_-1 th number and _i_-2 th number, apply iteration except for the first 2 elements

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





