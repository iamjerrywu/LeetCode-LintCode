# 128. Hash Function \(E\)

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

