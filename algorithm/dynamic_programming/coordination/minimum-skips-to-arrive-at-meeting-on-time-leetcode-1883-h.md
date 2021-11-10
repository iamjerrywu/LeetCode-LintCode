# Minimum Skips to Arrive at Meeting On Time (LeetCode 1883) (H)

## Problem

You are given an integer `hoursBefore`, the number of hours you have to travel to your meeting. To arrive at your meeting, you have to travel through `n` roads. The road lengths are given as an integer array `dist` of length `n`, where `dist[i]` describes the length of the `ith` road in **kilometers**. In addition, you are given an integer `speed`, which is the speed (in **km/h**) you will travel at.

After you travel road `i`, you must rest and wait for the **next integer hour** before you can begin traveling on the next road. Note that you do not have to rest after traveling the last road because you are already at the meeting.

* For example, if traveling a road takes `1.4` hours, you must wait until the `2` hour mark before traveling the next road. If traveling a road takes exactly `2` hours, you do not need to wait.

However, you are allowed to **skip** some rests to be able to arrive on time, meaning you do not need to wait for the next integer hour. Note that this means you may finish traveling future roads at different hour marks.

* For example, suppose traveling the first road takes `1.4` hours and traveling the second road takes `0.6` hours. Skipping the rest after the first road will mean you finish traveling the second road right at the `2` hour mark, letting you start traveling the third road immediately.

Return _the **minimum number of skips required** to arrive at the meeting on time, or_ `-1`_ if it is** impossible**_.

**Example 1:**

```
Input: dist = [1,3,2], speed = 4, hoursBefore = 2
Output: 1
Explanation:
Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
```

**Example 2:**

```
Input: dist = [7,3,5,5], speed = 2, hoursBefore = 10
Output: 2
Explanation:
Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours.
You can skip the first and third rest to arrive in ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 hours.
```

**Example 3:**

```
Input: dist = [7,3,5,5], speed = 1, hoursBefore = 10
Output: -1
Explanation: It is impossible to arrive at the meeting on time even if you skip all the rests.
```

**Constraints:**

* `n == dist.length`
* `1 <= n <= 1000`
* `1 <= dist[i] <= 105`
* `1 <= speed <= 106`
* `1 <= hoursBefore <= 107`

## Solution&#x20;

dp\[i]\[j] state means:&#x20;

* The time required in to reach ith distance with j skips rests

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        # to avoid rounding issue, need to take case floating points low bits
        eps = 1e-9
        dp = [[sys.maxsize] * (n + 1) for j in range(n + 1)]
        dp[0][0] = dist[0]/speed
        
        for j in range(n + 1):
            dp[0][j] = 0
        
        # init that 0 skips is considered
        for i in range(1, n + 1):
            # when doing ceiling, it would not keep the precision, for those bits low enough would round up
            # eventually would carry extra one to the accumulation
            # therefore, should minus 1e-9 to avoid this
            dp[i][0] = ceil(dp[i - 1][0] - eps) + dist[i - 1]/speed
        
        for i in range(1, n + 1):
            for j in range(1, i):
                # skip rest: dp[i][j] = dist[i - 1]/speed + ceil(dp[i -1][j])
                # don't skip rest: dp[i][j] = dist[i - 1]/speed + min(dp[i - 1][j - 1]
                dp[i][j] = dist[i - 1]/speed + min(dp[i - 1][j - 1], ceil(dp[i -1][j] - eps))
        
        for skips in range(n):
            if dp[-1][skips] <= hoursBefore:
                return skips
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n^2)**
