# Snapshot Array (LeetCode 1146) (M)

## Problem



Implement a SnapshotArray that supports the following interface:

* `SnapshotArray(int length)` initializes an array-like data structure with the given length.  **Initially, each element equals 0**.
* `void set(index, val)` sets the element at the given `index` to be equal to `val`.
* `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.
* `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

&#x20;

**Example 1:**

```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

&#x20;

**Constraints:**

* `1 <= length <= 50000`
* At most `50000` calls will be made to `set`, `snap`, and `get`.
* `0 <= index < length`
* `0 <= snap_id <` (the total number of times we call `snap()`)
* `0 <= val <= 10^9`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        # here use hashmap instead of array is because
        # we may not having so many values within the length of space
        # for those didn't set value, are 0 actaully
        self.arr = {}
        self.mapping = {}

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        snap_id = len(self.mapping)
        # if we use arr here, then snap requires to copy the entire array, giving a awful time complexity
        self.mapping[snap_id] = self.arr.copy()
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        # print(self.mapping)
        if snap_id in self.mapping and index in self.mapping[snap_id]:
            return self.mapping[snap_id][index]
        return 0
            
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

