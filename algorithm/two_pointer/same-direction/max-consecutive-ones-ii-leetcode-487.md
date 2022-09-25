# Max Consecutive Ones II (LeetCode 487)



## Problem

Given a binary array `nums`, return _the maximum number of consecutive_ `1`_'s in the array if you can flip at most one_ `0`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,0,1,1,0]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,0,1,1,0,1]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `nums[i]` is either `0` or `1`.

&#x20;

**Follow up:** What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        zero_cnt = 0
        ans = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_cnt+=1
            
            while zero_cnt > 1:
                if nums[start] == 0:
                    zero_cnt-=1
                start+=1
            ans = max(ans, end - start + 1)
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
