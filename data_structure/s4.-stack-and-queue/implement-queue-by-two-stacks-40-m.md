# Implement Queue by Two Stacks 40 (M)

## Problem

As the title described, you should only use two stacks to implement a queue's actions.

The queue should support `push(element)`, `pop()` and `top()` where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Suppose the queue is not empty when the pop() function is called.Example

**Example 1:**

Input:

```
Queue Operations = 
    push(1)
    pop()    
    push(2)
    push(3)
    top()    
    pop()  
```

Output:

```
1
2
2
```

Explanation:

Both pop and top methods should return the value of the first element.

**Example 2:**

Input:

```
Queue Operations = 
    push(1)
    push(2)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(1)
```

Output:

```
[]
```

Explanation:

There is no output.Challenge

implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by _AVERAGE_.

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
```
{% endtab %}

{% tab title="C++" %}
<pre class="language-cpp"><code class="lang-cpp"><strong>class MyQueue {
</strong>public:
    stack&#x3C;int> stack1, stack2;
    MyQueue() {
    }
    void push(int x) {
        stack1.push(x);
    }
    
    int pop() {
        int ret = peek();
        if (ret) {
            stack2.pop();
        }
        return ret;
    }
    
    int peek() {
        if (stack2.empty()) {
            while(!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        if (!stack2.empty()){
            int ret = stack2.top();
            return ret;
        }
        return 0;
    }
    
    bool empty() {
        return stack1.empty() and stack2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
</code></pre>
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
