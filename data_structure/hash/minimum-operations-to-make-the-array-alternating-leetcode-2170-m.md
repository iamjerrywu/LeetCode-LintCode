# Minimum Operations to Make the Array Alternating (LeetCode 2170) (M)

## Problem

****

You are given a **0-indexed** array `nums` consisting of `n` positive integers.

The array `nums` is called **alternating** if:

* `nums[i - 2] == nums[i]`, where `2 <= i <= n - 1`.
* `nums[i - 1] != nums[i]`, where `1 <= i <= n - 1`.

In one **operation**, you can choose an index `i` and **change** `nums[i]` into **any** positive integer.

Return _the **minimum number of operations** required to make the array alternating_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [3,1,3,2,4,3]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong>One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. </code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,2,2,2]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong>One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 105`



## Solution&#x20;

Key implementation step:

* Create two hashmaps to count the frequencies of num with odd and even indices, respectively;
* Search for the `num` in each hashmap with the maximum and second maximum frequencies:
  * If the two `num`'s with the maximum frequencies are not equal, then return `len(nums) - (maxFreqOdd + maxFreqEven)`;
  * Otherwise return `len(nums) - max(maxFreqOdd + secondMaxFreqEven, maxFreqEven + secondMaxFreqOdd)`.

One thing to note in step 2 is that after getting the two hashmaps for odd and even indices, we **don't** need to sort the hashmap keys based on their values or using heaps, but only need to write a subroutine by scanning through all `num`'s in the hashmap, so the overall time complexity is `O(N)` instead of `O(NlogN)`.

Below is my in-contest solution, though I could have made it a bit neater. Please upvote if you find this solution helpful.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        odd_cnt, even_cnt = defaultdict(int), defaultdict(int)
        for i in range(n):
            if i%2:
                odd_cnt[nums[i]]+=1
            else:
                even_cnt[nums[i]]+=1
        
        top_odd, sec_odd = (None, 0), (None, 0)
        for num, cnt in odd_cnt.items():
            if cnt > top_odd[1]:
                top_odd, sec_odd = (num, cnt), top_odd
            elif cnt > sec_odd[1]:
                sec_odd = (num, cnt)
        
        top_even, sec_even = (None, 0), (None, 0)
        for num, cnt in even_cnt.items():
            if cnt > top_even[1]:
                top_even, sec_even = (num, cnt), top_even
            elif cnt > sec_even[1]:
                sec_even = (num, cnt)
        if top_odd[0] != top_even[0]:
            return n - top_odd[1] - top_even[1]
        else:
            return n - max(top_odd[1] + sec_even[1], top_even[1] + sec_odd[1])
        
        
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
