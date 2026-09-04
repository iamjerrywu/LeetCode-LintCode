# Find the Highest Altitude (LeetCode 1732)

## Problem

There is a biker going on a road trip. The road trip consists of `n + 1` points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all (`0 <= i < n)`. Return _the **highest altitude** of a point._

&#x20;

**Example 1:**

<pre><code><strong>Input: gain = [-5,1,5,0,-7]
</strong><strong>Output: 1
</strong><strong>Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: gain = [-4,-3,-2,-1,4,3,2]
</strong><strong>Output: 0
</strong><strong>Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
</strong></code></pre>

&#x20;

**Constraints:**

* `n == gain.length`
* `1 <= n <= 100`
* `-100 <= gain[i] <= 100`

## Solution - Enumeration

{% tabs %}
{% tab title="C++" %}
{% code overflow="wrap" %}
```cpp
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curSum = 0, maxSum = 0;
        
        for (int g : gain) {
            curSum+=g;
            maxSum = max(curSum, maxSum);
        }
        return maxSum;
    }
};
```
{% endcode %}
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
