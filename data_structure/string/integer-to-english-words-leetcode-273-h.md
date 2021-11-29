# Integer to English Words (LeetCode 273) (H)

## Problem

Convert a non-negative integer `num` to its English words representation.

**Example 1:**

```
Input: num = 123
Output: "One Hundred Twenty Three"
```

**Example 2:**

```
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

**Example 3:**

```
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Example 4:**

```
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

**Constraints:**

* `0 <= num <= 231 - 1`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
dic = {
        1000000000: "Billion",
        1000000: "Million",
        1000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
        0: "Zero",
    }

segments = [float('inf'), 1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20]
        

class Solution:
    def numberToWords(self, num: int) -> str:
        res=[]
        if num == 0:
            return dic[0]
        
        for i in range(1, len(segments)):
            if segments[i] <= num < segments[i - 1]:
                div, rest = num//segments[i], num%segments[i]
                # saying "One Hundred", "One Thoushand", but not saying "One Fifty"
                
                # the order of processing and adding:
                # div -> segments[i] -> rest
                if div > 0 and i < 5:
                    res.append(self.numberToWords(div))
                res.append(dic[segments[i]])
                if rest > 0:
                    res.append(self.numberToWords(rest))
                return " ".join(res)
        
        return dic[num]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
