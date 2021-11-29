# Contains Duplicate III 1318 (M)

## Problem

Given an integer array `nums` and two integers `k` and `t`, return `true` if there are **two distinct indices** `i` and `j` in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k`.

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

**Example 3:**

```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

**Constraints:**

* `0 <= nums.length <= 2 * 104`
* `-231 <= nums[i] <= 231 - 1`
* `0 <= k <= 104`
* `0 <= t <= 231 - 1`

## Solution - Sliding Window + Buckets

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        buckets={}
        for i in range(len(nums)):
            bucket_id = nums[i]//(t+1)
            if bucket_id in buckets.keys():
                return True
            if bucket_id - 1 in buckets.keys() and abs(buckets[bucket_id-1] - nums[i]) <= t:
                return True
            if bucket_id + 1 in buckets.keys() and abs(buckets[bucket_id+1] - nums[i]) <= t:
                return True
            buckets[bucket_id] = nums[i]
            if i >= k :
                del buckets[nums[i-k]//(t+1)]
        
        return False
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
