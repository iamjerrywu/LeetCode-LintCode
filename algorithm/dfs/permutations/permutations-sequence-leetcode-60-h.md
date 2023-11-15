# Permutations Sequence (LeetCode 60) (H)

## Problem



The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given `n` and `k`, return the `kth` permutation sequence.

&#x20;

**Example 1:**

<pre><code>Input: n = 3, k = 3
<strong>Output:
</strong> "213"
</code></pre>

**Example 2:**

<pre><code>Input: n = 4, k = 9
<strong>Output:
</strong> "2314"
</code></pre>

**Example 3:**

<pre><code>Input: n = 3, k = 1
<strong>Output:
</strong> "123"
</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 9`
* `1 <= k <= n!`

## Solution&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-10-16 at 2.24.47 PM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        nums = [i for i in range(1, n + 1)]
        
        for i in range(1, n + 1):
            index = 0
            cnt = factorial(n - i)
            
            while k > cnt:
                k-=cnt
                index+=1
            ans+=str(nums[index])
            nums.remove(nums[index])
        return ans
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

* **Time Complexity:**
* **Space Complexity:**
