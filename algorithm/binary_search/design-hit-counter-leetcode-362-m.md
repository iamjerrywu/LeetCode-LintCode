# Design Hit Counter (LeetCode 362) (M)

## Problem

Design a hit counter which counts the number of hits received in the past `5` minutes (i.e., the past `300` seconds).

Your system should accept a `timestamp` parameter (**in seconds** granularity), and you may assume that calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the `HitCounter` class:

* `HitCounter()` Initializes the object of the hit counter system.
* `void hit(int timestamp)` Records a hit that happened at `timestamp` (**in seconds**). Several hits may happen at the same `timestamp`.
* `int getHits(int timestamp)` Returns the number of hits in the past 5 minutes from `timestamp` (i.e., the past `300` seconds).

&#x20;

**Example 1:**

```
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
```

&#x20;

**Constraints:**

* `1 <= timestamp <= 2 * 109`
* All the calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing).
* At most `300` calls will be made to `hit` and `getHits`.

&#x20;

**Follow up:** What if the number of hits per second could be huge? Does your design scale?

## Solution - Binary Search



{% tabs %}
{% tab title="Python" %}
```python
import collections
class HitCounter:

    def __init__(self):
        self.rec = []

    def hit(self, timestamp: int) -> None:
        self.rec.append(timestamp)
    
    def getHits(self, timestamp: int) -> int:
        if not self.rec:
            return 0
        
        target = timestamp - 300 + 1
        if target < 0:
            target = 0
        
        idx = self.binary_search(self.rec, target)
        return 0 if idx < 0 else len(self.rec) - idx
        
    
    def binary_search(self, rec, target):
        start, end = 0, len(rec) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if rec[mid] < target:
                start = mid
            else:
                end = mid
        if rec[start] >= target:
            return start
        if rec[end] >= target:
            return end
        return -1

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
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
