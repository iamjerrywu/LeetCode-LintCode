# Valid Palindrome II 891 \(M\)

## Problem

Description

Given a non-empty string `s`, you may delete at most one character. Judge whether you can make it a palindrome.

1. The string will only contain lowercase characters.
2. The maximum length of the string is 50000.

Example

**Example 1:**

```text
Input: s = "aba"
Output: true
Explanation: Originally a palindrome.
```

**Example 2:**

```text
Input: s = "abca"
Output: true
Explanation: Delete 'b' or 'c'.
```

**Example 3:**

```text
Input: s = "abc"
Output: false
Explanation: Deleting any letter can not make it a palindrome.
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if s is None:
            return False
        left, right = self.find_difference(s, 0, len(s) - 1)
        if left >= right:
            return True
        
        return self.is_palindrom(s, left + 1, right) or self.is_palindrom(s, left, right - 1)
    
    def is_palindrom(self, s, left, right):
        left, right = self.find_difference(s, left, right)
        return left >= right
    
    def find_difference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left+=1
            right-=1
        return left, right
```
{% endtab %}

{% tab title="java" %}
```
class Pair {
    int left, right;
    public Pair(int left, int right) {
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    /**
     * @param s: a string
     * @return: whether you can make s a palindrome by deleting at most one character
     */
    public boolean validPalindrome(String s) {
        // Write your code here
        
        if (s == null) {
            return false;
        }
        
        Pair pair = findDifference(s, 0, s.length() - 1);
        if (pair.left >= pair.right) {
            return true;
        }
        
        return isPalindrom(s, pair.left + 1, pair.right) || isPalindrom(s, pair.left, pair.right - 1);
    }
    
    private boolean isPalindrom(String s, int left, int right) {
        Pair pair = findDifference(s, left, right);
        return pair.left >= pair.right;
    }
    
    private Pair findDifference(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return new Pair(left, right);
            }
            left++;
            right--;
        }
        return new Pair(left, right);
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

