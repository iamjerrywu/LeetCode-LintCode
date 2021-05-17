# Implement Stack 495 \(E\)

## Problem

Description

Implement a stack. You can use any data structure inside a stack except stack itself to implement it.Example

Example 1:

```text
Input:
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
```

Example 2:

```text
Input:
isEmpty()
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.list = []
    def push(self, x):
        # write your code here
        self.list.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.list.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.list[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not len(self.list)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

