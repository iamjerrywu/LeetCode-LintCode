# Keep Multiplying Found Values by Two (LeetCode 2154) (E)

## Problem



You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:

1. If `original` is found in `nums`, **multiply** it by two (i.e., set `original = 2 * original`).
2. Otherwise, **stop** the process.
3. **Repeat** this process with the new number as long as you keep finding the number.

Return _the **final** value of_ `original`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [5,3,6,1,12], original = 3
<strong>Output:
</strong> 24
<strong>Explanation:
</strong> 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
</code></pre>

**Example 2:**

<pre><code>Input: nums = [2,7,9], original = 4
<strong>Output:
</strong> 4
<strong>Explanation:
</strong>- 4 is not found in nums. Thus, 4 is returned.
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i], original <= 1000`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        reference = set(nums)
        
        while original in reference:
            original*=2
        return original
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
