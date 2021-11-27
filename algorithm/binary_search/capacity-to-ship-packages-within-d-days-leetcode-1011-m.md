# Capacity To Ship Packages Within D Days (LeetCode 1011) (M)

## Problem



A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `ith` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

&#x20;

**Example 1:**

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```

**Example 2:**

```
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

**Example 3:**

```
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

&#x20;

**Constraints:**

* `1 <= days <= weights.length <= 5 * 104`
* `1 <= weights[i] <= 500`



## Solution&#x20;



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = min(weights), sum(weights)
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if not self.can_fill(mid, weights, days):
                start = mid
            else:
                end = mid
            
        if self.can_fill(start, weights, days):
            return start
        if self.can_fill(end, weights, days):
            return end
        return -1
        
    def can_fill(self, capacity, weights, days):
        cnt = 0
        tmp_w = 0
        for w in weights:
            # if weight larger than capacity, can't fit forever
            if w > capacity:
                return False
            
            # if still can fit within remained space, fit in
            if tmp_w + w <= capacity:
                tmp_w+=w
            # if cannot fit in, put it in a new box
            else:
                cnt+=1
                tmp_w = w
        # don't forget add one to count here
        if tmp_w:
            cnt+=1
        return cnt <= days
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogm)**
  * n: weights length
  * m: totals weight sum (500 \* 5 \* 10^4)
* **Space Complexity:**
