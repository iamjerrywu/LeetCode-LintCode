# Max Stack 859 \(H\)

## Problem

[https://www.lintcode.com/problem/859/](https://www.lintcode.com/problem/859/)

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push\(x\) -- Push element x onto stack.
2. pop\(\) -- Remove the element on top of the stack and return it.
3. top\(\) -- Get the element on the top.
4. peekMax\(\) -- Retrieve the maximum element in the stack.
5. popMax\(\) -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

{% hint style="info" %}
1. `-1e7 <= x <= 1e7`
2. Number of operations won't exceed `10000`.
3. The last four operations won't be called when stack is empty.
{% endhint %}

```text
Input:
push(5)
push(1)
push(5)
top()
popMax()
top()
peekMax()
pop()
top()
Output:
5
5
1
5
1
5
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.max_stack = []
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)
        if not self.max_stack or self.max_stack[-1] <= x:
            self.max_stack.append(x)
 

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return self.max_stack[-1]

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        max_val = self.peekMax()
        tmp = []
        while self.top() != max_val:
            tmp.append(self.stack.pop())
        self.stack.pop()
        self.max_stack.pop()
        while tmp:
            self.push(tmp.pop())
        return max_val
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



