# Contains Duplicate 1320 \(E\)

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

```text
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**

```text
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**

```text
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**

* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for num in nums:
            if num in dup:
                return True
            dup.add(num)
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(n\)**
* **Space Complexity:  O\(n\)**

