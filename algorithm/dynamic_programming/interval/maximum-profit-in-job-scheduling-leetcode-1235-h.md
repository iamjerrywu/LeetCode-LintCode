# Maximum Profit in Job Scheduling (LeetCode 1235) (H)

## Problem

&#x20;

We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/10/10/sample1\_1584.png)

```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/10/10/sample22\_1584.png)

```
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/10/10/sample3\_1584.png)

```
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
```

&#x20;

**Constraints:**

* `1 <= startTime.length == endTime.length == profit.length <= 5 * 104`
* `1 <= startTime[i] < endTime[i] <= 109`
* `1 <= profit[i] <= 104`

## Solution - DP + Linear Search (LTE!)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key = lambda e : e[1])
        end_times = [e for s, e, p in jobs]
        n = len(jobs)
        # dp[i] means the maximum profit I can make at ith
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            s = jobs[i][0]
            e = jobs[i][1]
            p = jobs[i][2]
            
            prev_index = self.linear_search(end_times, s)
            prev_profit = dp[prev_index] + p if prev_index >= 0 else p
            dp[i] = max(dp[i - 1], prev_profit)
        return dp[-1]
    
    # linear search
    def linear_search(self, arr, target):
        if arr[-1] < target:
                return len(arr) - 1
        if arr[0] > target:
            return -1
        prev = 0
        for i in range(len(arr)):
            if arr[i] > target:
                return prev
            prev = i  
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(n^2)**
* **Space Complexity: O(n)**

## Solution - DP + Binary Search&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key = lambda e : e[1])
        end_times = [e for s, e, p in jobs]
        n = len(jobs)
        # dp[i] means the maximum profit I can make at ith
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            s = jobs[i][0]
            e = jobs[i][1]
            p = jobs[i][2]
            
            prev_index = self.binary_search(end_times, s)
            prev_profit = dp[prev_index] + p if prev_index >= 0 else p
            dp[i] = max(dp[i - 1], prev_profit)
        return dp[-1]
    
    # linear search
    def binary_search(self, arr, target):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if arr[mid] < target:
                start = mid
            else:
                end = mid
        if arr[end] <= target:
            return end
        if arr[start] <= target:
            return start
        return -1
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
