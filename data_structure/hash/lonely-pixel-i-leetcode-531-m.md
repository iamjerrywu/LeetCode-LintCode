# Lonely Pixel I (LeetCode 531) (M)

## Problem

Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels, return _the number of **black** lonely pixels_.

A black lonely pixel is a character `'B'` that located at a specific position where the same row and same column don't have **any other** black pixels.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/11/pixel1.jpg)

```
Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/11/pixel2.jpg)

```
Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
Output: 0
```

&#x20;

**Constraints:**

* `m == picture.length`
* `n == picture[i].length`
* `1 <= m, n <= 500`
* `picture[i][j]` is `'W'` or `'B'`.



## Solution&#x20;

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
    int findLonelyPixel(vector<vector<char>>& picture) {
        map<int, int> rowHash;
        for (int i = 0; i < picture.size(); i++) {
            int cnt = 0;
            for (int j = 0; j < picture[i].size(); j++) {
                if (picture[i][j] == 'B') {
                    cnt+=1;
                }
            }
            rowHash[i] = cnt;
        }
        
        map<int, int> colHash;
        for (int j = 0; j < picture[0].size(); j++) {
            int cnt = 0;
            for (int i = 0; i < picture.size(); i++) {
                if (picture[i][j] == 'B') {
                    cnt+=1;
                }
            }
            colHash[j] = cnt;
        }
        int ans = 0;
        for (int i = 0; i < picture.size(); i++) {
            for (int j = 0; j < picture[i].size(); j++) {
                if ((picture[i][j] == 'B') && (rowHash[i] <= 1) && (colHash[j] <= 1)) {
                    ans+=1;
                }
            }
        }
        return ans;
        
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**
