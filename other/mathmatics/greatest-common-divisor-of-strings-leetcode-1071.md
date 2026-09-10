# Greatest Common Divisor of Strings (LeetCode 1071)

## Problem

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return _the largest string_ `x` _such that_ `x` _divides both_ `str1` _and_ `str2`.

&#x20;

**Example 1:**

**Input:** str1 = "ABCABC", str2 = "ABC"

**Output:** "ABC"

**Example 2:**

**Input:** str1 = "ABABAB", str2 = "ABAB"

**Output:** "AB"

**Example 3:**

**Input:** str1 = "LEET", str2 = "CODE"

**Output:** ""

**Example 4:**

**Input:** str1 = "AAAAAB", str2 = "AAA"

**Output:** ""​​​​​​​

&#x20;

**Constraints:**

* `1 <= str1.length, str2.length <= 1000`
* `str1` and `str2` consist of English uppercase letters.



## Solution

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
    string gcdOfStrings(string str1, string str2) {
        // if they have gcdStr, then following formula should be true
        if (str1 + str2 != str2 + str1) return "";
        
        // since we guarantee they have common divisor of strings, now becomes a math problem
        int gcdLength = gcd(str1.length(), str2.length());
        return str1.substr(0, gcdLength);
    }

private:
    int gcd(int num1, int num2) {
        while(num2!=0) {
            int tmp = num2;
            num2 = num1%num2;
            num1 = tmp;
        }
        return num1;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** $$O(\log(\min(str1_len, str2_len))$$
* **Space Complexity: O(1)**
