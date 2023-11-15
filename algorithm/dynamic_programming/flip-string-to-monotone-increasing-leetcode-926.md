# Flip String to Monotone Increasing (LeetCode 926)

## Problem



A binary string is monotone increasing if it consists of some number of `0`'s (possibly none), followed by some number of `1`'s (also possibly none).

You are given a binary string `s`. You can flip `s[i]` changing it from `0` to `1` or from `1` to `0`.

Return _the minimum number of flips to make_ `s` _monotone increasing_.

&#x20;

**Example 1:**

```
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
```

**Example 2:**

```
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
```

**Example 3:**

```
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
```

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `s[i]` is either `'0'` or `'1'`.



## Solution - Greedy

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
    int minFlipsMonoIncr(string s) {
        int zeroCnt = 0;
        for (char c : s) {
            if (c == '0') {
                zeroCnt+=1;
            }
        }
        
        int oneCnt = 0;
        int res = zeroCnt;
        for (char c : s) {
            if (c == '0') zeroCnt-=1;
            else oneCnt+=1;
            res = min(res, oneCnt + zeroCnt);
        }
        return res;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**



## Solution - DP

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
// dp[i][0] means minimum flip time for s[i] last == '0'
// dp[i][1] means minimum flip time for s[i] last == '1'

// s[i] = 1
// dp[i][0] = dp[i - 1][0] + 1
// dp[i][1] = min(dp[i - 1][1], dp[i - 1][0])

// s[i] = 0
// dp[i][0] = dp[i - 1][0]
// dp[i][1] = min(dp[i - 1][1] + 1, dp[i - 1][0] + 1)


class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int n = s.length();
        int dp[n][2];
        
        // init
        if (s[0] == '0') {
            dp[0][0] = 0;
            dp[0][1] = 1;
        } else {
            dp[0][0] = 1;
            dp[0][1] = 0;
        }
        
        for (int i = 1; i < n; i++) {
            if (s[i] == '0') {
                dp[i][0] = dp[i - 1][0];
                dp[i][1] = min(dp[i - 1][1] + 1, dp[i - 1][0] + 1);
            } else {
                dp[i][0] = dp[i - 1][0] + 1;
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]);
            }
        }
        return min(dp[n - 1][0], dp[n - 1][1]);
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity:** O(n)
