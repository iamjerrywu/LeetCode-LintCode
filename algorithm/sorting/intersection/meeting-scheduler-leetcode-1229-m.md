# Meeting Scheduler (LeetCode 1229) (M)



## Problem

Given the availability time slots arrays `slots1` and `slots2` of two people and a meeting duration `duration`, return the **earliest time slot** that works for both of them and is of duration `duration`.

If there is no common time slot that satisfies the requirements, return an **empty array**.

The format of a time slot is an array of two elements `[start, end]` representing an inclusive time range from `start` to `end`.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots `[start1, end1]` and `[start2, end2]` of the same person, either `start1 > end2` or `start2 > end1`.

&#x20;

**Example 1:**

```
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
```

**Example 2:**

```
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
```

&#x20;

**Constraints:**

* `1 <= slots1.length, slots2.length <= 104`
* `slots1[i].length, slots2[i].length == 2`
* `slots1[i][0] < slots1[i][1]`
* `slots2[i][0] < slots2[i][1]`
* `0 <= slots1[i][j], slots2[i][j] <= 109`
* `1 <= duration <= 106`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        pt1 = pt2 = 0
        
        while pt1 < len(slots1) and pt2 < len(slots2):
            intersect_right = min(slots1[pt1][1], slots2[pt2][1])
            intersect_left = max(slots1[pt1][0], slots2[pt2][0])
            
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            
            if slots1[pt1][1] < slots2[pt2][1]:
                pt1+=1
            else:
                pt2+=1
        return []
                
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
