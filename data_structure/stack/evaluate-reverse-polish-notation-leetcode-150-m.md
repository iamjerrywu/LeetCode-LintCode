# Evaluate Reverse Polish Notation (LeetCode 150) (M)

## Problem

&#x20;

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse\_Polish\_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

&#x20;

**Example 1:**

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

&#x20;

**Constraints:**

* `1 <= tokens.length <= 104`
* `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            # str = '-123' -> int(str) = -123 (no need to take care the negative sign)
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(self.division(num1, num2))
        return stack[0]
    
    # make the division toward zeros
    def division(self, a, b):
        return -(-a // b) if (a < 0) ^ (b < 0) else a // b
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;

        for (const string& s : tokens) {
            if (s == "+" or s == "-" or s == "*" or s == "/") {
                int sec = stk.top();
                stk.pop();
                int first = stk.top();
                stk.pop();
                if (s == "+") {
                    stk.push(first + sec);
                } else if (s == "-") {
                    stk.push(first - sec);
                } else if (s == "*") {
                    stk.push(first * sec);
                } else {
                    stk.push(first/sec);
                }
            } else if (is_number(s)){
                stk.push(stoi(s));
            }
        }
        return stk.top();
    }
private:
    static bool is_number(const string& s) {
        for (int i = 0; i < s.length(); i++) {
            if (!isdigit(s[i])) return false;
        }
        return true;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(n)**
* **Space Complexity: O(n)**
