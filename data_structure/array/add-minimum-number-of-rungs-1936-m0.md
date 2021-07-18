# Add Minimum Number of Rungs 1936 \(M0

## Problem

You are given a **strictly increasing** integer array `rungs` that represents the **height** of rungs on a ladder. You are currently on the **floor** at height `0`, and you want to reach the last rung.

You are also given an integer `dist`. You can only climb to the next highest rung if the distance between where you are currently at \(the floor or on a rung\) and the next rung is **at most** `dist`. You are able to insert rungs at any positive **integer** height if a rung is not already there.

Return _the **minimum** number of rungs that must be added to the ladder in order for you to climb to the last rung._

**Example 1:**

```text
Input: rungs = [1,3,5,10], dist = 2
Output: 2
Explanation:
You currently cannot reach the last rung.
Add rungs at heights 7 and 8 to climb this ladder. 
The ladder will now have rungs at [1,3,5,7,8,10].
```

**Example 2:**

```text
Input: rungs = [3,6,8,10], dist = 3
Output: 0
Explanation:
This ladder can be climbed without adding additional rungs.
```

**Example 3:**

```text
Input: rungs = [3,4,6,7], dist = 2
Output: 1
Explanation:
You currently cannot reach the first rung from the ground.
Add a rung at height 1 to climb this ladder.
The ladder will now have rungs at [1,3,4,6,7].
```

**Example 4:**

```text
Input: rungs = [5], dist = 10
Output: 0
Explanation:
This ladder can be climbed without adding additional rungs.
```

**Constraints:**

* `1 <= rungs.length <= 105`
* `1 <= rungs[i] <= 109`
* `1 <= dist <= 109`
* `rungs` is **strictly increasing**.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs = [0] + rungs
        res = 0
        for i in range(1, len(rungs)):
            if rungs[i] - rungs[i - 1] <= dist:
                continue
            else:
                if (rungs[i] - rungs[i - 1])%dist == 0:
                    res+= int((rungs[i] - rungs[i - 1])/dist - 1)
                else:
                    res+= (rungs[i] - rungs[i - 1])//dist
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

