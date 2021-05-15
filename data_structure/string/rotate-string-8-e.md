# Rotate String 8 \(E\)

## Problem

Description

Given a string of char array and an offset, rotate the string by offset `in place`. \(from left to right\).  
In different languages, `str` will be given in different ways. For example, the string `"abc"` will be given in following ways:

* Java: char\[\] str = {'a', 'b', 'c'};
* Python：str = \['a', 'b', 'c'\]
* C++：string str = "abc";

offset &gt;= 0  
the length of str &gt;= 0  
`In place` means you should change strings in the function. You don't return anything.Example

**Example 1:**

Input:

```text
str = "abcdefg"
offset = 3
```

Output:

```text
"efgabcd"
```

Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

**Example 2:**

Input:

```text
str = ""abcdefg"
offset = 0
```

Output:

```text
"abcdefg"
```

Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "abcdefg".

**Example 3:**

Input:

```text
str = ""abcdefg"
offset = 1
```

Output:

```text
"gabcdef"
```

Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "gabcdef".

**Example 4:**

Input:

```text
str = ""abcdefg"
offset = 2
```

Output:

```text
"fgabcde"
```

Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "fgabcde".

**Example 5:**

Input:

```text
str = ""abcdefg"
offset = 10
```

Output:

```text
"efgabcd"
```

Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if s:
            offset%=len(s)
            if offset!= 0:
                new_string = s[len(s) - offset:] + s[:offset + 2]
                for i in range(len(s)):
                    s[i] = new_string[i]
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution - In Place

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s:
            return ''

        offset = offset%len(s)

        self.reverse(s, 0, len(s) - 1)
        self.reverse(s, 0, offset - 1)
        self.reverse(s, offset, len(s) - 1)
        return s
    
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## 

