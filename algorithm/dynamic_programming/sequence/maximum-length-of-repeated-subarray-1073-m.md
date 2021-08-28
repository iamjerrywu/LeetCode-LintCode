# Maximum Length of Repeated Subarray 1073 \(M\)

## Problem

Given two integer arrays `nums1` and `nums2`, return _the maximum length of a subarray that appears in **both** arrays_.

**Example 1:**

```text
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

**Example 2:**

```text
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
```

**Constraints:**

* `1 <= nums1.length, nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 100`

## Solution - Brute Force with Hash Map

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_start = collections.defaultdict(list)
        for idx, val in enumerate(nums2):
            nums2_start[val].append(idx)
        cnt = 0
        ans = 0
        for i, val1 in enumerate(nums1):
            for j in nums2_start[val1]:
                k = 0
                while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
                    cnt+=1
                    k+=1
                ans = max(ans, cnt)
                cnt = 0
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^3\)**
* **Space Complexity: O\(n\)**

{% hint style="danger" %}
LTE
{% endhint %}

\*\*\*\*

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        
        # dp[i][j] means the longest repeated subarray btw nums1[0:i] and nums2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
                ans = max(ans, dp[i][j])
                
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(m \* n\)**
* **Space Complexity: O\(m \* n\)**

