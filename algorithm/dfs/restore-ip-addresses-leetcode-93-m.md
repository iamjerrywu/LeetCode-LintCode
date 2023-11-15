# Restore IP Addresses (LeetCode 93) (M)

## Problem

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

* For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return _all possible valid IP addresses that can be formed by inserting dots into_ `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

&#x20;

**Example 1:**

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

**Example 2:**

```
Input: s = "0000"
Output: ["0.0.0.0"]
```

**Example 3:**

```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

&#x20;

**Constraints:**

* `0 <= s.length <= 20`
* `s` consists of digits only.

## Solution - &#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(0, "", s, 0, ans)
        return ans
    
    
    def dfs(self, idx, string, s, cnt,  ans):
        if cnt > 4:
            return 
        
        if idx == len(s):
            if cnt == 4:
                ans.append(string[1:])
            return 
            
        # take one digit
        self.dfs(idx + 1, string + '.' + s[idx], s, cnt + 1, ans)
        
        # take two digits
        if idx + 1 < len(s) and 10 <= int(s[idx:idx + 2]) <= 99:
            self.dfs(idx + 2, string + '.' + s[idx:idx + 2], s, cnt + 1, ans)
        
        # take three digits
        if idx + 2 < len(s) and 100 <= int(s[idx:idx + 3]) <= 255:
            self.dfs(idx + 3, string + '.' + s[idx:idx + 3], s, cnt + 1, ans)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n^3)**
* **Space Complexity: O(n^3)**

