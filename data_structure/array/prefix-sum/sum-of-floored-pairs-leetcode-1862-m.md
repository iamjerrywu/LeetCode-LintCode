# Sum of Floored Pairs (LeetCode 1862) (M)

## Problem

Given an integer array `nums`, return the sum of `floor(nums[i] / nums[j])` for all pairs of indices `0 <= i, j < nums.length` in the array. Since the answer may be too large, return it **modulo** `109 + 7`.

The `floor()` function returns the integer part of the division.

**Example 1:**

```
Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
```

**Example 2:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 49
```

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 105`

## Solution - Brute Force

{% hint style="danger" %}
Would LTE
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        record = {}
        for num1 in nums:
            for num2 in nums:
                reco rd[floor(num1/num2)] = record.get(floor(num1/num2), 0) + 1
        return sum([k * v for k, v in record.items()])
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**

****

## Solution -Prefix\_Sum

{% hint style="danger" %}
Would LTE
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        # can write 'max_num = 10 ** 5' as well
        # the reason to * 2, is because eventually the max(nums), need to have range when calculating [max(nums):max(nums) * 2 - 1]
        max_num = max(nums) * 2
        MOD = 10**9 + 7
        
        cnt = [0 for _ in range(max_num + 1)]
        prefix_cnt = [0 for _ in range(max_num + 1)]
        n = len(nums)
        
        # init cnt array
        for num in nums:
            cnt[num]+=1
        print(cnt)
        
        # init prefix
        for index in range(1, max_num + 1):
            prefix_cnt[index] = prefix_cnt[index - 1] + cnt[index]
        print(prefix_cnt)
        
        ans = 0
        for index in range(1, max_num + 1):
            if cnt[index] == 0:
                continue
            
            index2 = index + index # skip the '0 ~ index - 1' parts
            # index = 7
            # 0 ~ 6   (answer = 0) can skip
            # 7 ~ 13  (answer = 1) index(14)//7 - 1
            # 14 ~ 20 (answer = 2) index(21)//7 - 1
            ...
            while index2 <= max_num:
                count = prefix_cnt[index2 - 1] - prefix_cnt[index2 - index - 1]
                ans += count * (index2 // index - 1) * cnt[index]
                print(index, index2, ans)
                ans%=MOD
                
                index2+=index
        
        return ans%MOD
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**
