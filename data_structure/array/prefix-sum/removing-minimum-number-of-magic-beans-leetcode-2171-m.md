# Removing Minimum Number of Magic Beans (LeetCode 2171) (M)

## Problem



You are given an array of **positive** integers `beans`, where each integer represents the number of magic beans found in a particular magic bag.

**Remove** any number of beans (**possibly none**) from each bag such that the number of beans in each remaining **non-empty** bag (still containing **at least one** bean) is **equal**. Once a bean has been removed from a bag, you are **not** allowed to return it to any of the bags.

Return _the **minimum** number of magic beans that you have to remove_.

&#x20;

**Example 1:**

<pre><code>Input: beans = [4,1,6,5]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> 
- We remove 1 bean from the bag with only 1 bean.
  This results in the remaining bags: [4,0,6,5]
- Then we remove 2 beans from the bag with 6 beans.
  This results in the remaining bags: [4,0,4,5]
- Then we remove 1 bean from the bag with 5 beans.
  This results in the remaining bags: [4,0,4,4]
We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that remove 4 beans or fewer.
</code></pre>

**Example 2:**

<pre><code>Input: beans = [2,10,3,2]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong>- We remove 2 beans from one of the bags with 2 beans.
  This results in the remaining bags: [0,10,3,2]
- Then we remove 2 beans from the other bag with 2 beans.
  This results in the remaining bags: [0,10,3,0]
- Then we remove 3 beans from the bag with 3 beans. 
  This results in the remaining bags: [0,10,0,0]
We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that removes 7 beans or fewer.
</code></pre>

&#x20;

**Constraints:**

* `1 <= beans.length <= 105`
* `1 <= beans[i] <= 105`



## Solution&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-09-13 at 1.15.34 AM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix_sums = [0]
        for bean in beans:
            prefix_sums.append(prefix_sums[-1] + bean)
        ans = float('inf')
        for i in range(len(beans)):
            # every index modify to as bean amount
            amount = prefix_sums[i] + prefix_sums[len(beans)] - prefix_sums[i + 1] - beans[i] * (len(beans) - i - 1)
            ans = min(amount, ans)
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
