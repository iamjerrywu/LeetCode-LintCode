# Range Addition (LeetCode 370)

## &#x20;Problem

You are given an integer `length` and an array `updates` where `updates[i] = [startIdxi, endIdxi, inci]`.

You have an array `arr` of length `length` with all zeros, and you have some operation to apply on `arr`. In the `ith` operation, you should increment all the elements `arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi]` by `inci`.

Return `arr` _after applying all the_ `updates`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/27/rangeadd-grid.jpg)

```
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
```

**Example 2:**

```
Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]
```

&#x20;

**Constraints:**

* `1 <= length <= 105`
* `0 <= updates.length <= 104`
* `0 <= startIdxi <= endIdxi < length`
* `-1000 <= inci <= 1000`



## Solution - Prefix Sum

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        
        // init array 
        int addition[length];
        for (int i = 0; i < length;i++) {
            addition[i] = 0;
        }
        
        for (vector<int> update : updates) {
            addition[update[0]]+=update[2];
            if ((update[1] + 1) < length) addition[update[1] + 1]-=update[2];
        }
        
        vector<int> res;
        int prefixSum = 0;
        for (int val : addition) {
            prefixSum+=val;
            res.push_back(prefixSum);
        }
        return res;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
