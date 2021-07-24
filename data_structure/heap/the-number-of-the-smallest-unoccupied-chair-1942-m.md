# The Number of the Smallest Unoccupied Chair 1942 \(M\)

## Problem

There is a party where `n` friends numbered from `0` to `n - 1` are attending. There is an **infinite** number of chairs in this party that are numbered from `0` to `infinity`. When a friend arrives at the party, they sit on the unoccupied chair with the **smallest number**.

* For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a **0-indexed** 2D integer array `times` where `times[i] = [arrivali, leavingi]`, indicating the arrival and leaving times of the `ith` friend respectively, and an integer `targetFriend`. All arrival times are **distinct**.

Return _the **chair number** that the friend numbered_ `targetFriend` _will sit on_.

**Example 1:**

```text
Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
```

**Example 2:**

```text
Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
```

**Constraints:**

* `n == times.length`
* `2 <= n <= 104`
* `times[i].length == 2`
* `1 <= arrivali < leavingi <= 105`
* `0 <= targetFriend <= n - 1`
* Each `arrivali` time is **distinct**.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        records = []
        for i in range(n):
            records.append((i, times[i][0], True))
            records.append((i, times[i][1], False))
        records.sort(key = lambda r : (r[1], r[2]))
        
        empty_chairs = []
        friend_to_chairs = {}
        for i in range(n):
            empty_chairs.append(i)
        heapq.heapify(empty_chairs)
        
        # do simulation
        for friend_id, time, sit in records:
            if friend_id == targetFriend:
                return heapq.heappop(empty_chairs)
            
            if sit == True:
                occupy_id = heapq.heappop(empty_chairs)
                friend_to_chairs[friend_id] = occupy_id
            else:
                heapq.heappush(empty_chairs, friend_to_chairs[friend_id])
                friend_to_chairs.pop(friend_id)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity:**

