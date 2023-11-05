# Add Binary 408 (E)

## Problem

Given two binary strings, return their sum (In binary notation).Example

**Example 1:**

```
Input:a = "0", b = "0"Output:"0"
```

**Example 2:**

```
Input:a = "11", b = "1"Output:"100"
```

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here

        index_a = len(a) - 1
        index_b = len(b) - 1
        ans = ''
        carry = 0
        while index_a >= 0 or index_b >= 0:
            a_val = int(a[index_a]) if index_a >= 0 else 0
            b_val = int(b[index_b]) if index_b >= 0 else 0
            print(a_val, b_val, carry)
            if (a_val + b_val + carry)%2 == 0:
                ans = '0' + ans
            else:
                ans = '1' + ans
            carry = (a_val + b_val + carry)//2
            index_a-=1
            index_b-=1
        if carry == 1:
            ans = '1' + ans
        return ans
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int a_ptr = a.length() - 1;
        int b_ptr = b.length() - 1;
        int digit;
        int carry = 0;
        string ans = "";
        int sum = 0;
        while(a_ptr >= 0 or b_ptr >= 0) {
            if (a_ptr >= 0) {  
                sum+=int(a[a_ptr] - '0');
                a_ptr-=1;
            }
            if (b_ptr >= 0) {
                sum+=int(b[b_ptr] - '0');
                b_ptr-=1;
            }
            sum+=carry;
            digit = sum&0x1;
            carry = sum/2;
            ans = to_string(digit) + ans;
            sum = 0;
        }
        if (carry)
            ans = to_string(carry) + ans;
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n + m)**
  * n: len(a)
  * m: len(b)
* **Space Complexity: O(1)**
