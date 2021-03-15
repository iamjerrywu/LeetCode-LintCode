# 109. Triangle

## Problem

[https://www.lintcode.com/problem/128](https://www.lintcode.com/problem/128)

### Description 

In data structure Hash, hash function is used to convert a string\(or any other type\) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:

hashcode\("abcd"\) = \(ascii\(a\) \* 333 + ascii\(b\) \* 332 + ascii\(c\) \*33 + ascii\(d\)\) % HASH\_SIZE 

                              = \(97\* 333 + 98 \* 332 + 99 \* 33 +100\) % HASH\_SIZE

                              = 3595978 % HASH\_SIZE

here HASH\_SIZE is the capacity of the hash table \(you can assume a hash table is like an array with index 0 ~ HASH\_SIZE-1\).

Given a string as a key and the size of hash table, return the hash value of this key.

{% hint style="info" %}
For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.
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





