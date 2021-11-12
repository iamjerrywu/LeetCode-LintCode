# Line Reflections (LeetCode 356) (M)

## Problem

Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

**Note** that there can be repeated points.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/23/356\_example\_1.PNG)

```
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/23/356\_example\_2.PNG)

```
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
```

&#x20;

**Constraints:**

* `n == points.length`
* `1 <= n <= 104`
* `-108 <= points[i][j] <= 108`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # need to use set, since duplicated points is neglected here
        rec = collections.defaultdict(set)
        for x, y in points:
            rec[y].add(x)
            
        mid_x = None
        for x_list in rec.values():
            # check within row
            if not self.is_valid(list(x_list)):
                return False
            # check between row
            new_mid_x = sum(x_list)/len(x_list)
            if mid_x and mid_x != new_mid_x:
                return False
            mid_x = new_mid_x
        return mid_x == new_mid_x
    
    def is_valid(self, nums):
        nums.sort()
        start, end = 0, len(nums) - 1
        prev_mid = None
        while start <= end:
            mid = (nums[end] + nums[start])/2
            if prev_mid and prev_mid != mid:
                return False
            prev_mid = mid
            start+=1
            end-=1
        return True
                    
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
