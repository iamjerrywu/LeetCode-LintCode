# Subarray Sum Equals to k 838 (E)

## Problem

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.Example

**Example1**

```
Input: nums = [1,1,1] and k = 2
Output: 2
Explanation:
subarray [0,1] and [1,2]
```

**Example2**

```
Input: nums = [2,1,-1,1,2] and k = 3
Output: 4
Explanation:
subarray [0,1], [1,4], [0,3] and [3,4]
```

## Solution - Brute Force Count

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        cnt = 0
        for start in range(len(nums)):
            summ = 0
            for end in range(start, len(nums)):
                summ+=nums[end]
                if summ == k:
                    cnt+=1
        return cnt
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(1)**



## Solution - Prefix Sum

### Code

{% tabs %}
{% tab title="python" %}
```python
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        appears = collections.defaultdict(int)
        appears[0]+=1
        
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum+=num
            ans+=appears[prefix_sum - k]
            appears[prefix_sum]+=1
        return ans
        
```
{% endtab %}

{% tab title="java" %}
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        
        int sumVal = 0;
        Map<Integer, Integer> prefixSums = new HashMap<>();
        prefixSums.put(0, 1);
        
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            sumVal+=nums[i];
            if (prefixSums.containsKey(sumVal - k)) {
                ans+=prefixSums.get(sumVal - k);
            }
            prefixSums.put(sumVal, prefixSums.getOrDefault(sumVal, 0) + 1);
        }
        return ans;
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
