# Global and Local Inversions (LeetCode 775) (M)

## Problem

****

You are given an integer array `nums` of length `n` which represents a permutation of all the integers in the range `[0, n - 1]`.

The number of **global inversions** is the number of the different pairs `(i, j)` where:

* `0 <= i < j < n`
* `nums[i] > nums[j]`

The number of **local inversions** is the number of indices `i` where:

* `0 <= i < n - 1`
* `nums[i] > nums[i + 1]`

Return `true` _if the number of **global inversions** is equal to the number of **local inversions**_.

&#x20;

**Example 1:**

```
Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.
```

**Example 2:**

```
Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.
```

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 105`
* `0 <= nums[i] < n`
* All the integers of `nums` are **unique**.
* `nums` is a permutation of all the numbers in the range `[0, n - 1]`.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        max_val = float('-inf')
        
        for i in range(len(nums) - 2):
            max_val = max(nums[i], max_val)
            if max_val > nums[i + 2]:
                return False
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

* **Time Complexity:**
* **Space Complexity:**

****
