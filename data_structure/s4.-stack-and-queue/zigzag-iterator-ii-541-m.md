# Zigzag Iterator II 541 \(M\)

## Problem

Follow up [Zigzag Iterator](http://www.lintcode.com/en/problem/zigzag-iterator/): What if you are given `k` 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for `k > 2` cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".Example

**Example1**

```text
Input: k = 3
vecs = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
]
Output: [1,4,8,2,5,9,3,6,7]
```

**Example2**

```text
Input: k = 3
vecs = [
    [1,1,1]
    [2,2,2]
    [3,3,3]
]
Output: [1,2,3,1,2,3,1,2,3]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        
        self.queue = collections.deque()
        #traverse all vecs
        for vec in vecs:
            #for a list, pop(): O(1), pop(0), O(n)
            if vec:
                self.queue.appendleft(vec[::-1])

    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        
        #first element in queue (right)
        vec = self.queue.pop()
        # last elemnet in list
        value = vec.pop()
        #list might empty
        if vec:
            # not empty 
            self.queue.appendleft(vec)
        
        return value

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.queue) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

