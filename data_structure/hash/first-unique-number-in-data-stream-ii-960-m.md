# First Unique Number in Data Stream II 960 \(M\)

## Problem

We need to implement a data structure named `DataStream`. There are `two` methods required to be implemented:

1. `void add(number)` // add a new number
2. `int firstUnique()` // return first unique number

You can assume that there must be at least one unique number in the stream when calling the firstUnique.Example

Example 1:

```text
Input:
add(1)
add(2)
firstUnique()
add(1)
firstUnique()
Output:
[1,2]
```

Example 2:

```text
Input:
add(1)
add(2)
add(3)
add(4)
add(5)
firstUnique()
add(1)
firstUnique()
add(2)
firstUnique()
add(3)
firstUnique()
add(4)
firstUnique()
add(5)
add(6)
firstUnique()
Output:
[1,2,3,4,5,6]
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self.duplicates:
            return 
        if num not in self.num_to_prev:
            self.push_back(num)
            return 
        
        # find duplicate, remove it forom hash/linked list
        self.duplicates.add(num)
        self.remove(num)
    
    def remove(self, num):
        prev = self.num_to_prev.get(num)
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if remove the tail node, then prev will be the new tail
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        if not self.dummy.next:
            return None
        return self.dummy.next.val
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

