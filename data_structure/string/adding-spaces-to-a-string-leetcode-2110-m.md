# Adding Spaces to a String (LeetCode 2110) (M)

## Problem

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

* For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy`` `**`Y`**`our`` `**`C`**`offee"`.

Return **** _the modified string **after** the spaces have been added._

&#x20;

**Example 1:**

<pre><code>Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
<strong>Output:
</strong> "Leetcode Helps Me Learn"
<strong>Explanation:
</strong> 
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.</code></pre>

**Example 2:**

<pre><code>Input: s = "icodeinpython", spaces = [1,5,7,9]
<strong>Output:
</strong> "i code in py thon"
<strong>Explanation:
</strong>The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.</code></pre>

**Example 3:**

<pre><code>Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
<strong>Output:
</strong> " s p a c i n g"
<strong>Explanation:
</strong>We are also able to place spaces before the first character of the string.</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 3 * 105`
* `s` consists only of lowercase and uppercase English letters.
* `1 <= spaces.length <= 3 * 105`
* `0 <= spaces[i] <= s.length - 1`
* All the values of `spaces` are **strictly increasing**.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        cnt = 0
        sp_id = 0
        ans = ""
        for c in s:
            if sp_id < len(spaces) and cnt == spaces[sp_id]:
                ans+=' '
                sp_id+=1
            ans+=c
            cnt+=1
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

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****
