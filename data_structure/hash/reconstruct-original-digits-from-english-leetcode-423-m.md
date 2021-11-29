# Reconstruct Original Digits from English (LeetCode 423) (M)

## Problem

****

Given a string `s` containing an out-of-order English representation of digits `0-9`, return _the digits in **ascending** order_.

&#x20;

**Example 1:**

```
Input: s = "owoztneoer"
Output: "012"
```

**Example 2:**

```
Input: s = "fviefuro"
Output: "45"
```

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `s[i]` is one of the characters `["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]`.
* `s` is **guaranteed** to be valid.



## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-11-29 at 12.00.12 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        
        ans = {}
        
        ans[0] = count['z']
        ans[2] = count['w']
        ans[4] = count['u']
        ans[6] = count['x']
        ans[8] = count['g']
        ans[3] = count['h'] - ans[8]
        ans[5] = count['f'] - ans[4]
        ans[7] = count['v'] - ans[5]
        ans[1] = count['o'] - ans[0] - ans[2] - ans[4]
        ans[9] = count['i'] - ans[5] - ans[6] - ans[8]
        res = ''
        for k, v in ans.items():
            # ignore if count is zero
            if v == 0:
                continue
            else:
                for _ in range(v):
                    res+=str(k)
        return ''.join(sorted(res))
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
