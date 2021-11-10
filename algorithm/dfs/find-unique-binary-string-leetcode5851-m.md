# Find Unique Binary String (LeetCode5851) (M)

## Problem

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return _a binary string of length _`n`_ that **does not appear** in `nums`. If there are multiple answers, you may return **any** of them_.

**Example 1:**

```
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
```

**Example 2:**

```
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
```

**Example 3:**

```
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 16`
* `nums[i].length == n`
* `nums[i] `is either `'0'` or `'1'`.

## Solution&#x20;

Find all the binary combinations then compare with the nums list

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        appear = set(nums)
        all_bi = self.find_binary(len(nums))
        for bi in all_bi:
            if bi not in appear:
                return bi
        
        
    def find_binary(self, n):
        all_bi = []
        self.dfs(0, n, "", all_bi)
        return all_bi
    
    def dfs(self, i, n, tmp, all_bi):
        if i == n:
            all_bi.append(tmp)
            return
        self.dfs(i + 1, n, tmp+'0', all_bi)
        self.dfs(i + 1, n, tmp+'1', all_bi)
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
