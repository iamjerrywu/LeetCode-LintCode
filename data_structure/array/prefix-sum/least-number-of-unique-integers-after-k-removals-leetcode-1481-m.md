# Least Number of Unique Integers after K Removals \(LeetCode 1481\) \(M\)

## Problem

Given an array of integers `arr` and an integer `k`. Find the _least number of unique integers_ after removing **exactly** `k` elements**.**

1. 
**Example 1:**

```text
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```

**Example 2:**

```text
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^9`
* `0 <= k <= arr.length`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        counter_list = []
        for key, val in counter.items():
            counter_list.append([key, val])
        
        counter_list.sort(key=lambda counter : counter[1])
        ans = len(counter_list)
        cnt = 0
        for i in range(len(counter_list)):
            if cnt == k:
                return ans
            
            for i in range(counter_list[i][1]):
                if cnt == k:
                    return ans
                cnt+=1
            ans-=1
        if cnt == k:
            return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

