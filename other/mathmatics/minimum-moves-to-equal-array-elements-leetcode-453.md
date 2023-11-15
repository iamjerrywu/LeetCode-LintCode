# Minimum Moves to Equal Array Elements (LeetCode 453)

## Problem

Given an integer array `nums` of size `n`, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment `n - 1` elements of the array by `1`.

&#x20;

**Example 1:**

```
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```

**Example 2:**

```
Input: nums = [1,1,1]
Output: 0
```

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`



## Solution&#x20;

Can also think in this way, that everytime (m - 1) number plus one, equals to one number minus one

![](<../../.gitbook/assets/Screen Shot 2021-11-06 at 1.50.34 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # find min element
        return sum(nums) - len(nums) * min(nums)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

