# Simplify Path 421 (M)

## Problem

Given an absolute path for a file (Unix-style), simplify it.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.

The result must always begin with `/`, and there must be only a single `/` between two directory names. The last directory name (if it exists) must not end with a trailing `/`. Also, the result must be the shortest string representing the absolute path.

*   Did you consider the case where path is `"/../"`?

    In this case, you should return `"/"`.
*   Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.

    In this case, you should ignore redundant slashes and return `"/home/foo"`.

Example

**Example 1:**

```
Input: "/home/"
Output: "/home"
```

**Example 2:**

```
Input: "/a/./../../c/"
Output: "/c"
Explanation: "/" has no parent directory, so "/../" equals "/".
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path_list = path.split('/')
        
        for ele in path_list:
            if ele == '.' or ele == '':
                continue
            if ele == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        
        ans = '/' + "/".join(stack)
        return ans
```
{% endtab %}

{% tab title="C++" %}


```cpp
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        string curStr = "";

        curStr.reserve(path.size());
        for (int i = 0; i <= path.size(); i++) {
            if (path[i] == '/' || i == path.size()) {
                if (curStr == "") {
                    continue;
                }
                if (curStr == "..") {
                    if (!stack.empty()) {
                        stack.pop_back();
                    }
                } else if (curStr != ".") {
                    stack.push_back(curStr);
                }
                curStr.clear();
            } else {
                curStr+=path[i];
            }
        }
        if (stack.empty()) return "/";
        
        string ans;
        ans.reserve(path.size());
        for (string &s : stack) {
            ans+='/';
            ans+=s;
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
