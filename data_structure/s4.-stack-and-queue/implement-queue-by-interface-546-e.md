# Implement Queue by Interface 546 \(E\)

## Problem

Description

Implement queue by interface.Example

See code for more information.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class InterfaceQueue:
    def push(self, element):
        pass

    # define an interface for pop method
    # write your code here
    def pop(self):
        pass

    # define an interface for top method
    # write your code here
    def top(self):
        pass

class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.list = []
		
    # implement the push method
    # write your code here
    def push(self, val):
        self.list.append(val)
		
    # implement the pop method
    # write your code here
    def pop(self):
        if len(self.list):
            res = self.list[0]
            self.list.remove(res)
            return res
        else:
            return 0
            
	# implement the top method
    # write your code here
    def top(self):
        return self.list[0]
        
# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue
```
{% endtab %}

{% tab title="" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

