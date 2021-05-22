# First Bad Version 74 \(M\)

## Problem

The code base version is an integer start from `1` to `n`. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call `isBadVersion` to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is `SVNRepo.isBadVersion(v)`Example

**Example 1:**

Input:

```text
n = 5first bad version is 4
```

Output:

```text
4
```

Explanation:

isBadVersion\(3\) -&gt; false  
isBadVersion\(5\) -&gt; true  
isBadVersion\(4\) -&gt; true  
Therefore, it can be determined that the fourth version is the first incorrect version.Challenge

You should call _isBadVersion_ as few as possible.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end)//2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        if SVNRepo.isBadVersion(end):
            return end
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(logn\)**
* **Space Complexity: O\(1\)**

