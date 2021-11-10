# Pairs of Songs With Total Durations Divisible by 60 (LeetCode 1010) (M)

## Problem



You are given a list of songs where the ith song has a duration of `time[i]` seconds.

Return _the number of pairs of songs for which their total duration in seconds is divisible by_ `60`. Formally, we want the number of indices `i`, `j` such that `i < j` with `(time[i] + time[j]) % 60 == 0`.

&#x20;

**Example 1:**

```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

**Example 2:**

```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
```

&#x20;

**Constraints:**

* `1 <= time.length <= 6 * 104`
* `1 <= time[i] <= 500`



## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rec = collections.defaultdict(int)
        cnt = 0
        for num in time:
            num%=60
            cnt+=rec[(60 - num)%60]
            rec[num]+=1
        return cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****
