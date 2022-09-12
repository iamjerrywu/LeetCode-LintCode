# Add Strings 415 (E)

## Problem

Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.

* The length of both num1 and num2 is < 5100.
* Both num1 and num2 contains only digits 0-9.
* Both num1 and num2 does not contain any leading zero.
* You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example

**Example 1:**

```
Input : num1 = "123", num2 = "45"Output : "168"
```

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        carry = 0
        index_1 = len(num1) - 1
        index_2 = len(num2) - 1
        
        res = ''
        while index_1 >= 0 or index_2 >= 0:
            val_1 = ord(num1[index_1]) - ord('0') if index_1 >= 0 else 0
            val_2 = ord(num2[index_2]) - ord('0') if index_2 >= 0 else 0
            if val_1 + val_2 + carry >= 10:
                res = str((val_1 + val_2 + carry)%10) + res
                carry = 1
            else:
                res = str(val_1 + val_2 + carry) + res
                carry = 0
            index_1-=1
            index_2-=1
        
        if carry == 1:
            res = '1' + res
        return res
```
{% endtab %}

{% tab title="Java" %}
```java
class Solution {
    public String addStrings(String num1, String num2) {
        int n1_ptr = num1.length() - 1;
        int n2_ptr = num2.length() - 1;
        
        int val = 0;
        int carry = 0;
        String ans = "";
        while (n1_ptr >=0 || n2_ptr >= 0 || carry > 0) {
            if(n1_ptr >= 0) {
                val+=Character.getNumericValue(num1.charAt(n1_ptr));
                n1_ptr-=1;
            }
            
            if(n2_ptr >= 0) {
                val+=Character.getNumericValue(num2.charAt(n2_ptr));
                n2_ptr-=1;
            }
            val+=carry;
            carry = val/10;
            val%=10;
            ans = Integer.valueOf(val) + ans;
            val = 0;
        }
        return ans;
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(m + n)**
  * m: len(num1)
  * n: len(num2)
* **Space Complexity: O(1)**
