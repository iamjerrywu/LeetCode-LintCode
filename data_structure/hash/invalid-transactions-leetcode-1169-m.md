# Invalid Transactions (LeetCode 1169) (M)

## Problem



A transaction is possibly invalid if:

* the amount exceeds `$1000`, or;
* if it occurs within (and including) `60` minutes of another transaction with the **same name** in a **different city**.

You are given an array of strings `transaction` where `transactions[i]` consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of `transactions` that are possibly invalid. You may return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Output:
</strong> ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Explanation:
</strong> The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
</code></pre>

**Example 2:**

<pre><code>Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
<strong>Output:
</strong> ["alice,50,1200,mtv"]
</code></pre>

**Example 3:**

<pre><code>Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
<strong>Output:
</strong> ["bob,50,1200,mtv"]
</code></pre>

&#x20;

**Constraints:**

* `transactions.length <= 1000`
* Each `transactions[i]` takes the form `"{name},{time},{amount},{city}"`
* Each `{name}` and `{city}` consist of lowercase English letters, and have lengths between `1` and `10`.
* Each `{time}` consist of digits, and represent an integer between `0` and `1000`.
* Each `{amount}` consist of digits, and represent an integer between `0` and `2000`.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # {name:[time, city, tcs, idx]}
        rec = defaultdict(list)
        ans = []
        selected = set()
        for i, transac in enumerate(transactions):
            tsc_list = transac.split(',')
            name = tsc_list[0]
            time = int(tsc_list[1])
            amt = int(tsc_list[2])
            city = tsc_list[3]
            
            # check within 60 mins
            for t, c, tsc, idx in rec[name]:
                if abs(time - t) <= 60 and city != c:
                    if idx not in selected:
                        ans.append(tsc)
                        selected.add(idx)
                    if i not in selected:
                        selected.add(i)
                        ans.append(transac)
            rec[name].append([time, city, transac, i])
            # check amt
            if amt > 1000:
                if i not in selected:
                    selected.add(i)
                    ans.append(transac)
        return list(ans)
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
