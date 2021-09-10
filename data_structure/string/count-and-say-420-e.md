# Count and Say 420 \(E\)

## Problem

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

* `countAndSay(1) = "1"`
* `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the **minimal** number of groups so that each group is a contiguous section all of the **same character.** Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string `"3322251"`:![](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg)

Given a positive integer `n`, return _the_ `nth` _term of the **count-and-say** sequence_.

**Example 1:**

```text
Input: n = 1
Output: "1"
Explanation: This is the base case.
```

**Example 2:**

```text
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

**Constraints:**

* `1 <= n <= 30`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        base = '1'
        for i in range(2, n + 1):
            base = self.process(base)
        return base
    
    # process the ans:
    # i.e: '21' -> ans should be 'one two one one ' -> '1211'
    def process(self, base):
        cnt = 0
        ans = ''
        p1, p2 = 0, 0
        while p2 < len(base):
            while p2 < len(base) and base[p1] == base[p2]:
                p2+=1
                cnt+=1    
            ans+=str(cnt) + base[p1]
            p1 = p2
            cnt = 0
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:** 

