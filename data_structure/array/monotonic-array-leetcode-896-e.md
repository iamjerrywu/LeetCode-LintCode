# Monotonic Array (LeetCode 896) (E)

## Problem

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` _if the given array is monotonic, or_ `false` _otherwise_.

&#x20;

**Example 1:**

```
Input: nums = [1,2,2,3]
Output: true
```

**Example 2:**

```
Input: nums = [6,5,4,4]
Output: true
```

**Example 3:**

```
Input: nums = [1,3,2]
Output: false
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `-105 <= nums[i] <= 105`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        inc = False
        dec = False
        for i in range(len(nums) - 1):
            # ignore the == condition, since they don't matter
            if nums[i] < nums[i + 1]:
                if dec:
                    return False
                inc = True
            if nums[i] > nums[i + 1]:
                if inc:
                    return False
                dec = True
        return True
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

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****
