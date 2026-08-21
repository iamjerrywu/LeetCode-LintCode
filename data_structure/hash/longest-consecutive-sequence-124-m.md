# Longest Consecutive Sequence 124 (M)

## Problem

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.Example

_**Example 1**_

```
Input : [100, 4, 200, 1, 3, 2]
Output : 4
Explanation : The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4
```

## Solution - HashMap Brute Force

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        # ref = {n : True for n in num}
        cnt = {}
        for n in num:
            # if n - 1 in ref:
            #     continue
            if n in cnt:
                continue
            cnt[n] = 1
            if n - 1 in cnt:
                cnt[n]+=cnt[n - 1]
            while n + 1 in cnt:
                cnt[n + 1] = cnt[n] + 1
                n = n + 1
        return max(cnt.values())
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
  * Would Time Limite Exceed
* **Space Complexity: O(n)**



## Solution - HashMap Optimized&#x20;

Only need to start counting on the minimum number in any consecutive sublist

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        ref = {n : True for n in num}
        cnt, max_val = 0, 0
        for n in num:
            # if n is the minimum number in any consecutive subsets
            if n - 1 not in ref:
                cnt = 0
                while n in ref:
                    cnt+=1
                    n = n + 1
                max_val = max(max_val, cnt)
        return max_val
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // if nums is empty vector
        if (nums.empty()) return 0;
        
        /*
            logic here is like, the start of the sequence val is that we cannot find the val - 1 in the nums
            so we can use a set to store all the nums
        */
        
        // O(n)
        std::unordered_set<int> seen(nums.begin(), nums.end());
        
        int max_length = 0;
        // iterate the seen dict instead of the num
        for (int num : seen) {
            int cur_val = num;
            // current num as 1 length
            int length = 1;
                
            if (!seen.contains(cur_val - 1)) {
                // start finding the sequence
                while(seen.contains(cur_val + 1)) {
                    length+=1;
                    cur_val+=1;
                }
            }
            max_length = std::max(max_length, length);
        }
        return max_length;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**
