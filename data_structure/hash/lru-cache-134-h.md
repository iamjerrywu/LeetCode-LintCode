# LRU Cache 134 (H)

## Problem

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `set`.

* `get(key)` Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
* `set(key, value)` Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Finally, you need to return the data from each get.Example

**Example1**

```
Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
```

**Example 2:**

```
Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
```

## Solution

Using singly-linkedlist and hashmap to record the previous node

* Since linked list access O(1) (with hashmap), and if out of size, linkedlist can do in O(1) deleting node as well
  * Even array can do O(1) access, but deleting first node require O(n) adjusting values in rest positions
* With hashmap don't need to implement doubly linkedlist

![](<../../.gitbook/assets/Screen Shot 2021-04-25 at 11.57.55 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class LinkedNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    # change "prev->node->next->...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return 
        # remove cur node from linked-list
        prev.next = node.next
        # update previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        prev = self.key_to_prev[key]
        cur = prev.next

        self.kick(prev)
        return cur.value
    
    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.tail.value = value
            return
        
        self.push_back(LinkedNode(key, value))
        # the size of hashmap equals to linkedlist length
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()

```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(1)**
* **Space Complexity: O(1)**



### Code - Doubly LinkedList

{% tabs %}
{% tab title="python" %}
```python
class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.nodes = {}
        self.start = None
        self.end = None

    def get(self, key):
        # Get node for key if it exists
        node = self.nodes.get(key)
        if not node:
            return -1

    # Move this node to front of list
        self.move_to_front(node)

        return node.val

    def put(self, key, val):
        node = self.nodes.get(key)

        if node:
          # Update existing node and move to front
            node.val = val
            self.move_to_front(node)
            return

        if self.count == self.n:
          # No space, so remove last item
          if self.end:
            del self.nodes[self.end.key]
            self.remove(self.end)
        else:
            self.count += 1

        # Finally create and insert the new node
        node = Node(key, val)
        self.insert(node)
        self.nodes[key] = node

  # Private helpers
    def insert(self, node):
        if not self.end:
              self.end = node
        if self.start:
                node.next = self.start
                self.start.prev = node
        self.start = node

    def remove(self, node):
        if node.prev:
             node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.start == node:
             self.start = node.next
        if self.end == node:
            self.end = node.prev

    def move_to_front(self, node):
        # Remove node and re-insert at head
        self.remove(node)
        self.insert(node)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(1)**
* **Space Complexity: O(1)**

## Solution **- Unorderd\_Map**

{% tabs %}
{% tab title="Python" %}
```python
# Here using ordered dict

import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.rec = collections.OrderedDict()
        self.max_cap = capacity
        
    def get(self, key: int) -> int:
        if key in self.rec:
            self.rec.move_to_end(key)
            return self.rec[key]
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        self.rec[key] = value
        self.rec.move_to_end(key)
        
        if len(self.rec) > self.max_cap:
            self.rec.popitem(last = False)
        
            
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class LRUCache {
public:
    LRUCache(int capacity) {
        maxSize = capacity;
    }
    
    int get(int key) {
        if (hashMap.find(key) != hashMap.end()) {
            int value = hashMap[key]->second;
            updateCache(key, value);
            return value;
        }     
        return -1;
    }
    
    void put(int key, int value) {
        if (hashMap.find(key) != hashMap.end()) {
            updateCache(key, value);
        } else {
            cache.push_front(pair(key, value));
            hashMap[key] = cache.begin();
        }
        
        if (hashMap.size() > maxSize) {
            hashMap.erase(cache.back().first);
            cache.pop_back();
        }
    }

private:
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>> :: iterator> hashMap;
    int maxSize;
    
    void updateCache(int key, int value) {
        cache.erase(hashMap[key]);
        cache.push_front(pair(key, value));
        hashMap[key] = cache.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
