# Max Number of K-Sum Pairs

## Problem

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return _the maximum number of operations you can perform on the array_.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [1,2,3,4], k = 5
</strong><strong>Output: 2
</strong><strong>Explanation: Starting with nums = [1,2,3,4]:
</strong>- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
</code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [3,1,3,4,3], k = 6
</strong><strong>Output: 1
</strong><strong>Explanation: Starting with nums = [3,1,3,4,3]:
</strong>- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 10`<sup>`5`</sup>
* `1 <= nums[i] <= 10`<sup>`9`</sup>
* `1 <= k <= 10`<sup>`9`</sup>



## Solution - Hash Map

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
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        int ans = 0;
        for (int num : nums) {
            // unorderd_map default value = 0
            if (freq[k - num] == 0) {
                freq[num]+=1;
            } else {
                freq[k - num]-=1;
                ans+=1;
            }
        }
        return ans;
        
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

## Solution - Two Pointers

{% tabs %}
{% tab title="Python" %}
```python
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int l = 0, r = nums.size() - 1;
        int ans = 0;
        while(l < r) {
            if (nums[l] + nums[r] > k) {
                r-=1;
            } else if (nums[l] + nums[r] < k) {
                l+=1;
            } else {
                ans+=1;
                l+=1;
                r-=1;
            }
        }
        return ans;
    }
};
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
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        int ans = 0;
        for (int num : nums) {
            // unorderd_map default value = 0
            if (freq[k - num] == 0) {
                freq[num]+=1;
            } else {
                freq[k - num]-=1;
                ans+=1;
            }
        }
        return ans;
        
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

