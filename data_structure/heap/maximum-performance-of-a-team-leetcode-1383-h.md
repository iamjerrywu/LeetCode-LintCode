# Maximum Performance of a Team (LeetCode 1383) (H)

## Problem

&#x20;

You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency` both of length `n`. There are `n` engineers numbered from `1` to `n`. `speed[i]` and `efficiency[i]` represent the speed and efficiency of the `ith` engineer respectively.

Choose **at most** `k` different engineers out of the `n` engineers to form a team with the maximum **performance**.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return _the maximum performance of this team_. Since the answer can be a huge number, return it **modulo** `109 + 7`.

&#x20;

**Example 1:**

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
```

**Example 2:**

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
```

**Example 3:**

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
```

&#x20;

**Constraints:**

* `1 <= k <= n <= 105`
* `speed.length == n`
* `efficiency.length == n`
* `1 <= speed[i] <= 105`
* `1 <= efficiency[i] <= 108`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
MOD = 10**9 + 7
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = sorted(zip(efficiency, speed), reverse = True)
        heap = []
        total_speed = 0
        res = 0
        for e, s in arr:
            heapq.heappush(heap, s)
            total_speed+=s
            
            if len(heap) > k:
                total_speed-=heapq.heappop(heap)
            
            # here we might calculate the wrong current val (total_speed * e)
            # i.e: we actaully pop the s/e we just add (but here we times the e, so that's wrong)
            # However, it's find since the answer we calculate will defintely smaller than previous one
            # because the efficiency is sorted reversed, 
            res = max(res, total_speed * e)
        return res%MOD
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
