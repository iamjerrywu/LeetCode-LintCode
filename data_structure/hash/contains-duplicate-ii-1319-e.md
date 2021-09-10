# Contains Duplicate II 1319 \(E\)

## Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Example 1:**

```text
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```text
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```text
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints:**

* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* `0 <= k <= 105`

## Solution - Sort and Hash

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        rec = collections.defaultdict(list)
        for i in range(len(nums)):
            rec[nums[i]].append(i)
        
        for val_list in rec.values():
            if len(val_list) > 1:
                val_list.sort()
                for i in range(len(val_list) - 1):
                    if val_list[i + 1] - val_list[i] <= k:
                        return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity: O\(n\)**

\*\*\*\*

## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        rec = set()
        for i in range(len(nums)):
            if nums[i] in rec:
                return True
            rec.add(nums[i])
            if len(rec) > k:
                rec.remove(nums[i - k])
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

