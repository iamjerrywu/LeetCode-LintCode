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

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-23 at 12.54.43 PM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # if valueDiff == 0:
        #     return True
        
        bucket = {}
        for i, num in enumerate(nums):
            # devided into (valueDiff + 1) group
            bucket_id = num//(valueDiff)
            
            if bucket_id in bucket:
                return True
            if bucket_id - 1 in bucket and abs(bucket[bucket_id - 1] - num) <= valueDiff:
                return True
            if bucket_id + 1 in bucket and abs(bucket[bucket_id + 1] - num) <= valueDiff:
                return True
            # make the bucket always has the latest value
            bucket[bucket_id] = num
            if i >= indexDiff:
                bucket.pop(nums[i - indexDiff]//(valueDiff))
            print(bucket)
        return False
    

        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
