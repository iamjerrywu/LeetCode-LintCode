# All Divisions With the Highest Score of a Binary Array (LeetCode 2155) (M)

## Problem

****

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where `0 <= i <= n)` into two arrays (possibly empty) `numsleft` and `numsright`:

* `numsleft` has all the elements of `nums` between index `0` and `i - 1` **(inclusive)**, while `numsright` has all the elements of nums between index `i` and `n - 1` **(inclusive)**.
* If `i == 0`, `numsleft` is **empty**, while `numsright` has all the elements of `nums`.
* If `i == n`, `numsleft` has all the elements of nums, while `numsright` is **empty**.

The **division score** of an index `i` is the **sum** of the number of `0`'s in `numsleft` and the number of `1`'s in `numsright`.

Return _**all distinct indices** that have the **highest** possible **division score**_. You may return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: nums = [0,0,1,0]
<strong>Output:
</strong> [2,4]
<strong>Explanation:
</strong> Division at index
- 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
- 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
- 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
- 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
- 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.</code></pre>

**Example 2:**

<pre><code>Input: nums = [0,0,0]
<strong>Output:
</strong> [3]
<strong>Explanation:
</strong> Division at index
- 0: numsleft is []. numsright is [0,0,0]. The score is 0 + 0 = 0.
- 1: numsleft is [0]. numsright is [0,0]. The score is 1 + 0 = 1.
- 2: numsleft is [0,0]. numsright is [0]. The score is 2 + 0 = 2.
- 3: numsleft is [0,0,0]. numsright is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,1]
<strong>Output:
</strong> [0]
<strong>Explanation:
</strong> Division at index
- 0: numsleft is []. numsright is [1,1]. The score is 0 + 2 = 2.
- 1: numsleft is [1]. numsright is [1]. The score is 0 + 1 = 1.
- 2: numsleft is [1,1]. numsright is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 105`
* `nums[i]` is either `0` or `1`.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_sums = [0]
        one_sums = [0]
        for num in nums:
            zero_sums.append(zero_sums[-1])
            one_sums.append(one_sums[-1])
            if num == 0:
                zero_sums[-1]+=1
            if num == 1:
                one_sums[-1]+=1
        rec = []
        ans = set()
        max_score = 0
        for i in range(len(nums) + 1):
            score = zero_sums[i] + one_sums[-1] - one_sums[i]
            if score > max_score:
                ans.clear()
                ans.add(i)
                max_score = score
            elif score == max_score:
                ans.add(i)
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

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
