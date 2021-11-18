# K-diff Pairs in an Array (LeetCode 532) (M)

## Problem

Given an array of integers `nums` and an integer `k`, return _the number of **unique** k-diff pairs in the array_.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

* `0 <= i < j < nums.length`
* `|nums[i] - nums[j]| == k`

**Notice** that `|val|` denotes the absolute value of `val`.

&#x20;

**Example 1:**

```
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

**Example 2:**

```
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

**Example 3:**

```
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

**Example 4:**

```
Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
```

**Example 5:**

```
Input: nums = [-1,-2,-3], k = 1
Output: 2
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-107 <= nums[i] <= 107`
* `0 <= k <= 107`

## Solution - Two Pointer

1. If it is less than `k`, we increment the right pointer.
   * If left and right pointers are pointing to the same number, we increment the right pointer too.
2. If it is greater than `k`, we increment the left pointer.
3. If it is exactly `k`, we have found our pair, we increment our placeholder `result` and increment left pointer.

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, r = 0, 1
        ans = 0
        while l < len(nums) and r < len(nums):
            print('l')
            if l == r or nums[r] - nums[l] < k:
                r+=1
            elif nums[r] - nums[l] > k:
                l+=1
            else:
                l+=1
                ans+=1
                while l < len(nums) and nums[l] == nums[l - 1]:
                    l+=1
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**

## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        rec = collections.Counter(nums)
        ans = 0
        for num in rec:
            # we only need to care the "num + k", don't need to care "num - k"
            # since that would definetly be duplicately counted
            if k > 0 and rec[num + k] > 0:
                ans+=1
            elif k == 0 and rec[num] > 1:
                ans+=1
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
