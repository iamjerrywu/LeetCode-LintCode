---
description: 4 (4M)
---

# Heap

## Introduction

Support: 

* O\(logN\) Add 
* O\(logN\) Remove
* O\(logN\) Pop
* O\(1\) Min or Max

{% hint style="warning" %}
In Python: heapq / Java: PriorityQueue, the "remove" action require O\(n\)

* Unless it's pop the top one, otherwise, need to traverse to find the specific element
{% endhint %}

Implementation in different language

* Java: `PriorityQueue`
* C++: `priority_queue`
* Python: `heapq`

## Heap - Support O\(1\) Delete Template

```python
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minheap = []
        self.deleted_set = set()
    #O(logk)
    def push(self, val, index):
        heappush(self.minheap, (val, index))
    
    #O(logk)
    def _lazy_delete(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)
    
    #O(logk)
    def top(self):
        self._lazy_delete()
        return self.minheap[0]
    #O(logk)
    def pop(self):
        self._lazy_delete()
        heappop(self.minheap)
    
    # O(1)
    def delete(self, index):
        self.deleted_set.add(index)
    
    #O(1)
    def is_empty(self):
        return not bool(self.minheap)
```

## Heap - Support O\(1\) Delete Template with size 

```python
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minheap = []
        self.num_set = {}
        self.size = 0
    
    #O(logk)
    def push(self, value, index):
        heappush(self.minheap, (value, index))
        self.num_set[index] = value
        self.size+=1   
    
    #O(logk)
    def _lazy_delete(self):
        while self.minheap and self.minheap[0][1] not in self.num_set:
            heappop(self.minheap)
    
    #O(logk)
    def top(self):
        self._lazy_delete()
        return self.minheap[0]
    
    #O(logk)
    def pop(self):
        self._lazy_delete()
        self.num_set.pop(self.top()[1])
        self.size-=1
        return heappop(self.minheap)
    
    # O(1)
    def delete(self, index):
        if index in self.num_set:
            self.num_set.pop(index)
            self.size-=1 
    #O(1)
    def is_empty(self):
        return self.size == 0
    
    #O(1)
    def get_size(self):
        return self.size
```

