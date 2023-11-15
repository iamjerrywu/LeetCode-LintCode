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
from collections import deque
class HitCounter:

    def __init__(self):
        self.rec = []

    def hit(self, timestamp: int) -> None:
        self.rec.append(timestamp)
    
    def getHits(self, timestamp: int) -> int:
        tar = timestamp - 300 + 1
        idx = self.bi_search(timestamp - 300 + 1)
        if idx is not None:
            return len(self.rec) - idx
        return 0
    
    def bi_search(self, tar):
        if not self.rec:
            return None
        start, end = 0, len(self.rec) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.rec[mid] > tar:
                end = mid
            elif self.rec[mid] < tar:
                start = mid
            else:
                end = mid
        if self.rec[start] >= tar:
            return start
        if self.rec[end] >= tar:
            return end
        return None
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**



## Solution - Heap



{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
class HitCounter:

    def __init__(self):
        self.rec = deque()

    def hit(self, timestamp: int) -> None:
        self.rec.append(timestamp)
    
    def getHits(self, timestamp: int) -> int:
        while self.rec and self.rec[0] < timestamp - 300 + 1:
            self.rec.popleft()
        return len(self.rec)
    
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

