# Find Original Array From Doubled Array (LeetCode 2007) (M)

## Problem

An integer array `original` is transformed into a **doubled** array `changed` by appending **twice the value** of every element in `original`, and then randomly **shuffling** the resulting array.

Given an array `changed`, return `original`_ if _`changed`_ is a **doubled** array. If _`changed`_ is not a **doubled** array, return an empty array. The elements in_ `original` _may be returned in **any** order_.

**Example 1:**

```
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
```

**Example 2:**

```
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
```

**Example 3:**

```
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
```

**Constraints:**

* `1 <= changed.length <= 105`
* `0 <= changed[i] <= 105`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        
        n = len(changed)
        count =  collections.Counter(changed)
        changed.sort(reverse = True)       
        ori = []
        
        for i in range(len(changed)):
            double, origin = changed[i], changed[i]//2
            if count[double] != 0 and double%2 == 0:
                if double == origin and count[origin] >= 2 or double != origin and count[origin] >= 1:
                    self.update(ori, count, double, origin)
        return ori if len(ori) == n/2 else []
    def update(self, ori, count, double, origin):
        count[double]-=1
        count[origin]-=1
        ori.append(origin)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
