# Random Pick Index (LeetCode 398) (M)

## Problem

Given an integer array `nums` with possible **duplicates**, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:

* `Solution(int[] nums)` Initializes the object with the array `nums`.
* `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid i's, then each index should have an equal probability of returning.

&#x20;

**Example 1:**

```
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 2 * 104`
* `-231 <= nums[i] <= 231 - 1`
* `target` is an integer from `nums`.
* At most `104` calls will be made to `pick`.



## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.cnt = defaultdict(list)
        for i in range(len(nums)):
            self.cnt[nums[i]].append(i)

    def pick(self, target: int) -> int:
        random_index = random.randint(0, len(self.cnt[target]) - 1)
        return self.cnt[target][random_index]
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
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

****

## Solution - Reservior Sampling

{% tabs %}
{% tab title="Python" %}
```python
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def pick(self, target: int) -> int:
        cnt = 0
        ans = -1
        for i, num in enumerate(self.arr):
            if num == target:
                cnt+=1
                rand_index = random.uniform(0, 1)
                if rand_index <= 1/cnt:
                    ans = i
        return ans
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
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

****
