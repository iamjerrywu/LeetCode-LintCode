# Valid Triangle Number (LeetCode 611) (H)

## Problem

Given an integer array `nums`, return _the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [2,2,3,4]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</code></pre>

**Example 2:**

<pre><code>Input: nums = [4,2,3,4]
<strong>Output:
</strong> 4
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `0 <= nums[i] <= 1000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def search(start, s_val, end, e_val):
            while start + 1 < end:
                mid = start + (end - start)//2
                m_val = nums[mid]
                if is_valid(s_val, e_val, m_val):
                    end = mid
                else:
                    start = mid
            if is_valid(s_val, e_val, nums[start]):
                return start
            if is_valid(s_val, e_val, nums[end]):
                return end
            return -1
    
        def is_valid(v1, v2, v3):
            return v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2
        
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if j - i > 1:
                    # smallest middle num to form with nums[i], nums[j]
                    idx = search(i + 1, nums[i], j - 1, nums[j])
                    if idx >= 0:
                        ans+=j - idx
        return ans
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



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        cnt = 0
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    r -= 1
                else:
                    cnt += r - l
                    l += 1
        return cnt
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
