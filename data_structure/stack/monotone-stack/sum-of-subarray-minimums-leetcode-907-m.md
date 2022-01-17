# Sum of Subarray Minimums (LeetCode 907) (M)

## Problem

Given an array of integers arr, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer **modulo** `109 + 7`.

&#x20;

**Example 1:**

```
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

**Example 2:**

```
Input: arr = [11,81,94,43,3]
Output: 444
```

&#x20;

**Constraints:**

* `1 <= arr.length <= 3 * 104`
* `1 <= arr[i] <= 3 * 104`



## Solution&#x20;

![](<../../../.gitbook/assets/Screen Shot 2021-11-27 at 1.14.05 AM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [1] * n
        dec_q = [(arr[0], 1)]
        
        # left 
        for i in range(1, n):
            while dec_q and arr[i] <= dec_q[-1][0]:
                left[i]+=dec_q.pop()[1]
            dec_q.append((arr[i], left[i]))
        
        # right
        right = [1] * n
        dec_q = [(arr[-1], 1)]
        
        for i in range(n - 2, -1, -1):
            while dec_q and arr[i] < dec_q[-1][0]:
                right[i]+=dec_q.pop()[1]
            dec_q.append((arr[i], right[i]))
        
        ans = 0
        for i in range(n):
            ans += arr[i] * left[i] * right[i]
        print(left)
        print(right)
        MOD = 10**9 + 7
        return ans % MOD
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
