# Simplify Path 421 \(M\)

## Problem

Given an absolute path for a file \(Unix-style\), simplify it.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.

The result must always begin with `/`, and there must be only a single `/` between two directory names. The last directory name \(if it exists\) must not end with a trailing `/`. Also, the result must be the shortest string representing the absolute path.

* Did you consider the case where path is `"/../"`?

  In this case, you should return `"/"`.

* Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.

  In this case, you should ignore redundant slashes and return `"/home/foo"`.

Example

**Example 1:**

```text
Input: "/home/"
Output: "/home"
```

**Example 2:**

```text
Input: "/a/./../../c/"
Output: "/c"
Explanation: "/" has no parent directory, so "/../" equals "/".
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        
        #use list as stack
        stack = []
        # split the path based on '/', and return list (array)
        arr = path.split('/')
        
        for s in arr:
            #if empty s or '.', do nothing
            if s == '.' or s == '':
                continue
            #if '..', should back to previous folder
            if s == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(s)
        if not stack:
            return '/'
        answer = ''
        while stack:
            answer = '/' + stack.pop() + answer
        return answer
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

