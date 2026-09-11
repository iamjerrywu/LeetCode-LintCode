# Increasing Triplet Subsequences

## Problem

Given an integer array `nums`, return `true` _if there exists a triple of indices_ `(i, j, k)` _such that_ `i < j < k` _and_ `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [1,2,3,4,5]
</strong><strong>Output: true
</strong><strong>Explanation: Any triplet where i &#x3C; j &#x3C; k is valid.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [5,4,3,2,1]
</strong><strong>Output: false
</strong><strong>Explanation: No triplet exists.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: nums = [2,1,5,0,4,6]
</strong><strong>Output: true
</strong><strong>Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 &#x3C; nums[4] == 4 &#x3C; nums[5] == 6.
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 5 * 10`<sup>`5`</sup>
* `-2`<sup>`31`</sup>` ``<= nums[i] <= 2`<sup>`31`</sup>` ``- 1`



## Solution

Step-by-Step VisualizationLet's use the array `nums = [2, 1, 5, 0, 4, 6]`

1. **Build `min_left`** (Scan left to right, keeping track of the smallest number so far):
   * `min_left = [2, 1, 1, 0, 0, 0]`
2. **Build `max_right`** (Scan right to left, keeping track of the largest number so far):
   * `max_right = [6, 6, 6, 6, 6, 6]`
3. **Scan Middle Elements** (Check if `min_left[i] < nums[i] < max_right[i]`):
   * At index 2 (`nums[2] = 5`): Is `min_left[2] (1) < 5 < max_right[2] (6)`? **Yes!** (Triplet: 1, 5, 6) -> Return `true`.

***

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        // create minLeft: min from left
        int minLeft[nums.size()];
        int minVal = INT_MAX;
        for (int i = 0; i < nums.size(); i++) {
            minVal = min(nums[i], minVal);
            minLeft[i] = minVal;
        }
        
        // create maxRight: max from right
        int maxRight[nums.size()];
        int maxVal = INT_MIN;
        for (int i = nums.size() - 1; i >= 0; i--) {
            maxVal = max(nums[i], maxVal);
            maxRight[i] = maxVal;
        }

        // find if valid triplet
        for (int i = 0; i < nums.size(); i++) {
            if ((minLeft[i] < nums[i]) && (nums[i] < maxRight[i])) return true;
        }
        return false;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
