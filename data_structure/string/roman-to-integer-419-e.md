# Roman to Integer 419 (M)

## Problem

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
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

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.&#x20;
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.&#x20;
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
```

**Example 2:**

```
Input: s = "IV"
Output: 4
```

**Example 3:**

```
Input: s = "IX"
Output: 9
```

**Example 4:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 5:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Constraints:**

* `1 <= s.length <= 15`
* `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
* It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Solution&#x20;

### Oberservation

<figure><img src="../../.gitbook/assets/Screen Shot 2022-08-27 at 1.16.27 PM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I" :    1, 
            "V" :    5,
            "X" :   10,
            "L" :   50,
            "C" :  100,
            "D" :  500,
            "M" : 1000}
        ans = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and hash_map[s[i]] < hash_map[s[i + 1]]:
                ans+=-hash_map[s[i]]
            else:
                ans+=hash_map[s[i]]
            i+=1
        return ansinte
```
{% endtab %}

{% tab title="Java" %}
```java
class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> map = new HashMap<>() {{
            put("I", 1);
            put("V", 5);
            put("X", 10);
            put("L", 50);
            put("C", 100);
            put("D", 500);
            put("M", 1000);
        }};
        
        int i = 0, ans = 0;
        while (i < s.length()) {
            if (i < s.length() - 1 && map.get(String.valueOf(s.charAt(i))) < map.get(String.valueOf(s.charAt(i + 1)))) {
                ans -= map.get(String.valueOf(s.charAt(i)));
            } else {
                ans += map.get(String.valueOf(s.charAt(i)));
            }
            i+=1;
        }
        return ans;
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> rec = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        int i = 0;
        int ans = 0;
    
        while (i < s.length()) {
            if (i < s.length() - 1 && rec[s[i]] < rec[s[i + 1]]) {
                ans-=rec[s[i]];
            } else {
                ans+=rec[s[i]];
            }
            i++;
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
