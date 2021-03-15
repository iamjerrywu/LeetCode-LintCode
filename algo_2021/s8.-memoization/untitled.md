# 109. Triangle

## Problem

[https://www.lintcode.com/problem/128](https://www.lintcode.com/problem/128)

### Description 

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

{% hint style="info" %}
Bonus point if you are able to do this using only O\(n\) extra space, where n is the total number of rows in the triangle.
{% endhint %}

### Example

**Example 1:**

```text
Input:  key="abcd", size = 1000
Output: 978
Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978
```

**Example 2:**

```text
Input:  key="abcd", size = 100
Output: 78
Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%100 = 78
```

## Approach

### Intuition 

Follow the problem guideline

### Algorithm

congruence modulo principle: \(a  _b \) % MOD = \(\(a % MOD\)_  \(b % MOD\)\) % MOD

#### Step by step

* Traverse every char in string 
  * ans time 33 than plus ascii value of char
  * mod HASH\_SIZE

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        hash_value = 0
        for c in key: 
            hash_value = (hash_value * 33 + ord(c)) % HASH_SIZE
        return hash_value
```
{% endtab %}

{% tab title="java" %}
```java
public class Solution {
    /**
     * @param key: A string you should hash
     * @param HASH_SIZE: An integer
     * @return: An integer
     */
    public int hashCode(char[] key, int HASH_SIZE) {
        // write your code here
        long ans = 0;
        for (int i = 0; i < key.length; i++) {
            ans = (ans * 33 + (int)key[i]) % HASH_SIZE; 
        }

        return (int)ans;
        
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
  * Traverse all char in string
* **Space Complexity: O\(n\)**





