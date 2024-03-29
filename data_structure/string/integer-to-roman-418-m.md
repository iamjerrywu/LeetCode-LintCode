# Integer to Roman 418 \(M\)

## Problem

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```text
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* `I` can be placed before `V` \(5\) and `X` \(10\) to make 4 and 9. 
* `X` can be placed before `L` \(50\) and `C` \(100\) to make 40 and 90. 
* `C` can be placed before `D` \(500\) and `M` \(1000\) to make 400 and 900.

Given an integer, convert it to a roman numeral.

**Example 1:**

```text
Input: num = 3
Output: "III"
```

**Example 2:**

```text
Input: num = 4
Output: "IV"
```

**Example 3:**

```text
Input: num = 9
Output: "IX"
```

**Example 4:**

```text
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```text
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Constraints:**

* `1 <= num <= 3999`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        ROMAN = {
            1000:   'M', 
             900:  'CM',
             500:   'D',
             400:  'CD', 
             100:   'C',
              90:  'XC',
              50:   'L',
              40:  'XL',
              10:   'X', 
               9:  'IX',
               5:   'V',
               4:  'IV',
               1:   'I',
        }
        ans = ''
        for k, v in ROMAN.items():
            while n >= k:
                n-=k
                ans+=v
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(\(3\(n - 1\) + 1\) \* 4\)**
  * n: digits of n
* **Space Complexity: O\(3\(n - 1\) + 1\)**

