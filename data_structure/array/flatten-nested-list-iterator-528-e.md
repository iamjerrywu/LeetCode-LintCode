# Flatten Nested List Iterator 528 (M)

## Problem

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

* `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
* `int next()` Returns the next integer in the nested list.
* `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:

```
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```

If `res` matches the expected flattened list, then your code will be judged as correct.

**Example 1:**

```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```

**Example 2:**

```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```

**Constraints:**

* `1 <= nestedList.length <= 500`
* The values of the integers in the nested list is in the range `[-106, 106]`.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.integers = []
        self.process(nestedList)
        # becase it ask hasNext, so start with -1 instead of 0
        self.pos = -1
        
    def process(self, nested_list):
        print(nested_list)
        for nested_item in nested_list:
            if nested_item.isInteger():
                self.integers.append(nested_item.getInteger())
            else:
                self.process(nested_item.getList())
    
    def next(self) -> int:
        self.pos+=1
        return self.integers[self.pos]
        
    
    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.integers)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
