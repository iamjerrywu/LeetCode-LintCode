# Number of Atoms (LeetCode 726) (H)

## Problem

Given a string `formula` representing a chemical formula, return _the count of each atom_.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `1`. If the count is `1`, no digits will follow.

* For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.

Two formulas are concatenated together to produce another formula.

* For example, `"H2O2He3Mg4"` is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

* For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than `1`), followed by the second name (in sorted order), followed by its count (if that count is more than `1`), and so on.

The test cases are generated so that all the values in the output fit in a **32-bit** integer.

&#x20;

**Example 1:**

<pre><code>Input: formula = "H2O"
<strong>Output:
</strong> "H2O"
<strong>Explanation:
</strong> The count of elements are {'H': 2, 'O': 1}.</code></pre>

**Example 2:**

<pre><code>Input: formula = "Mg(OH)2"
<strong>Output:
</strong> "H2MgO2"
<strong>Explanation:
</strong> The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.</code></pre>

**Example 3:**

<pre><code>Input: formula = "K4(ON(SO3)2)2"
<strong>Output:
</strong> "K4N2O14S4"
<strong>Explanation:
</strong> The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.</code></pre>

&#x20;

**Constraints:**

* `1 <= formula.length <= 1000`
* `formula` consists of English letters, digits, `'('`, and `')'`.
* `formula` is always valid.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        stack = [collections.Counter()]
        while i < n:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i+=1
            elif formula[i] == ')':
                top = stack.pop()
                i+=1
                i_start = i
                while i < n and formula[i].isdigit():
                    i+=1
                multiplicity = int(formula[i_start:i] or 1)
                for name, v in top.items():
                    stack[-1][name]+=v * multiplicity
            else:
                i_start = i
                i+=1
                while i < n and formula[i].islower():
                    i+=1
                name = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i+=1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity
        return "".join([name + (str(stack[-1][name] if stack[-1][name] > 1 else '')),   for name in sorted(stack[-1])])        
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
