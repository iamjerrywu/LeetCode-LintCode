# Group the People Given the Group Size They Belong To (LeetCode 1282) (M)

## Problem

&#x20;

There are `n` people that are split into some unknown number of groups. Each person is labeled with a **unique ID** from `0` to `n - 1`.

You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the group that person `i` is in. For example, if `groupSizes[1] = 3`, then person `1` must be in a group of size `3`.

Return _a list of groups such that each person `i` is in a group of size `groupSizes[i]`_.

Each person should appear in **exactly one group**, and every person must be in a group. If there are multiple answers, **return any of them**. It is **guaranteed** that there will be **at least one** valid solution for the given input.

&#x20;

**Example 1:**

```
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
```

**Example 2:**

```
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```

&#x20;

**Constraints:**

* `groupSizes.length == n`
* `1 <= n <= 500`
* `1 <= groupSizes[i] <= n`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
        
        ans = []
        
        for k, v_list in groups.items():
            if len(v_list) > k:
                while v_list:
                    ans.append(list(v_list[:k]))
                    v_list = v_list[k:]
            else:
                ans.append(v_list)
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
