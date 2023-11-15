# Minimum Swaps to Group All 1's Together (LeetCode 1151) (M)

## Problem

Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in **any place** in the array.

**Example 1:**

```
Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
```

**Example 2:**

```
Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
```

**Example 3:**

```
Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
```

&#x20;

**Constraints:**

* `1 <= data.length <= 105`
* `data[i]` is either `0` or `1`.

## Solution - Sliding Window

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
    int minSwaps(vector<int>& data) {
        int oneCnt = 0;
        // first count how many zeros must group together
        for (int val : data) {
            if (val == 1) oneCnt+=1;
        }
        
        int l = 0, r = oneCnt - 1;
        int zeroCnt = 0;
        // calculate the init window, how many zeros inside
        for (int i = l; i <= r; i++) {
            if (data[i] == 0) zeroCnt+=1;
        }
        int ans = zeroCnt;
        
        // moving the sliding window
        for (int i = r + 1; i < data.size(); i++) {
            if (data[i] == 0) zeroCnt+=1;
            if (data[l] == 0) zeroCnt-=1;
            l+=1;
            ans = min(ans, zeroCnt);
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity:**

