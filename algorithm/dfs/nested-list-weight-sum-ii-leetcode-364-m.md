# Nested List Weight Sum II \(LeetCode 364\) \(M\)

## Problem

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The **depth** of an integer is the number of lists that it is inside of. For example, the nested list `[1,[2,2],[[3],2],1]` has each integer's value set to its **depth**. Let `maxDepth` be the **maximum depth** of any integer.

The **weight** of an integer is `maxDepth - (the depth of the integer) + 1`.

Return _the sum of each integer in_ `nestedList` _multiplied by its **weight**_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex1.png)

```text
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex2.png)

```text
Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
```

**Constraints:**

* `1 <= nestedList.length <= 50`
* The values of the integers in the nested list is in the range `[-100, 100]`.
* The maximum **depth** of any integer is less than or equal to `50`.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.max_level = 1
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.recursion1(nestedList, 1)
        res = self.recursion2(nestedList, 1, self.max_level)
        return res
        
    def recursion1(self, nestedList, level):
        for ele in nestedList:
            if ele.isInteger():
                self.max_level = max(self.max_level, level)
            else:
                self.recursion1(ele.getList(), level + 1)
    def recursion2(self, nestedList, level, max_level):
        res = 0
        for ele in nestedList:
            if ele.isInteger():
                res += (max_level - level + 1) * ele.getInteger()
            else:
                res+=self.recursion2(ele.getList(), level + 1, max_level)
        return res
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

