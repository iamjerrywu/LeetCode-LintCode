# Least Number of Unique Integers after K Removals (LeetCode 1481) (M)

## Problem

Given an array of integers `arr` and an integer `k`. Find the _least number of unique integers_ after removing **exactly** `k` elements**.**

1.

**Example 1:**

```
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```

**Example 2:**

```
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^9`
* `0 <= k <= arr.length`

## Solution&#x20;

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

{% tab title="C++" %}
```cpp
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int, int> counter;
        
        for (int val : arr) {
            if (counter.count(val) == 0) counter[val] = 1;
            else counter[val]+=1;
        }
        
        vector<int> appears;
        for (auto &kv : counter) {
            appears.push_back(kv.second);
        }
        
        sort(appears.begin(), appears.end());
        
        for (int i = 0; i < appears.size(); i++) {
            while (appears[i]) {
                if (k == 0) return appears.size() - i;
                k-=1;
                appears[i]-=1;
            }
        }
        return 0;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O(nlogn)**
* **Space Complexity: O(n)**
