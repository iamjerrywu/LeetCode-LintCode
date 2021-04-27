# Fizz Buzz 9 \(E\)

## Problem

Given number _n_. Print number from 1 to _n_. According to following rules:

* when number is divided by `3`, print `"fizz"`.
* when number is divided by `5`, print `"buzz"`.
* when number is divided by both `3` and `5`, print `"fizz buzz"`.
* when number can't be divided by either `3` or `5`, print the number `itself`.

Example

**Example 1:**

Input:

```text
n = 15
```

Output:

```text
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
```

Challenge

Can you do it with only one `if` statement?

## Solution - If/Else 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        str_list = []
        for num in range(1, n+1):
            if num%15==0:
                str_list.append("fizz buzz")
            elif num%3==0:
                str_list.append("fizz")
            elif num%5==0:
                str_list.append("buzz")
            else:
                str_list.append(str(num))
        return str_list
        

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

## Solution - No If 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        str_list = []
        for num in range(1, n+1):
            str_list.append((num%3==0)*"fizz" + (num%15==0)*" " + (num%5==0)*"buzz" + ((num%3!=0) & (num%5!=0)) * str(num))
        return str_list
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

