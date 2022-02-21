# Decode String 575 (M)

## Problem

Given an expression `s` contains numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

Numbers can only appear in front of “\[]”.Example

**Example1**

```
Input: S = abc3[a]
Output: "abcaaa"
```

**Example2**

```
Input: S = 3[2[ad]3[pf]]xyz
Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
```

Challenge

Can you do it without recursion?

## Solution - stack

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        
        for c in s:
            #']' is a end signal
            if c != ']':
                stack.append(c)
                continue
            strs = []
            #keep popping elements out until meet '['
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            #pop out '['
            stack.pop()
            repeats = 0
            base = 1
            #'234' = 4 * 10 ^ 0 + 3 * 10 ^ 1 + 2 * 10 ^ 2
            # stack not empty and top is a number
            while stack and stack[-1].isdigit():
                repeats+=(ord(stack.pop()) - ord('0')) * base
                base*= 10
            # first reversed, then repeat the string, finanly push back to stack
            stack.append(''.join(reversed(strs)) * repeats)
        
        return ''.join(stack)
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    string decodeString(string s) {
        string str = "";
        stack<string> stack;
        
        for (char c : s) {
            if (c != ']') {
                stack.push(string(1, c));
                continue;
            }
            str = "";
            while (stack.top() != "[") {
                str = stack.top() + str;
                stack.pop();
            }
            stack.pop();
            int repeats = 0;

            int tens = 1;
            while ((!stack.empty()) && isStrDigit(stack.top())) {
                repeats = stoi(stack.top()) * tens + repeats;
                tens*=10;
                stack.pop();
            }
            string new_string = "";
            while (repeats) {
                cout << repeats;
                new_string+=str;
                repeats-=1;
            }
            stack.push(new_string);
        }
        
        vector<string> vec;
        while (!stack.empty()) {
            vec.push_back(stack.top());
            stack.pop();
        }
        string ans;
        for (int i = vec.size() - 1; i >= 0; i--) {
            ans+=vec[i];
        }
        return ans;
    }
    bool isStrDigit(string s) {
        for (char c : s) {
            if (!isdigit(c)) return false;
        }
        return true;
    }
};
```
{% endtab %}

{% tab title="C++ (deque)" %}
```cpp
class Solution {
private:
    bool isStrDigit(string s) {
        for (char c : s) {
            if (!isdigit(c)) return false;
        }
        return true;
    }
public:
    string decodeString(string s) {
        string str = "";
        deque<string> deq;
        
        for (char c : s) {
            if (c != ']') {
                deq.push_back(string(1, c));
                continue;
            }
            str = "";
            while (deq.back() != "[") {
                str = deq.back() + str;
                deq.pop_back();
            }
            deq.pop_back();
            int repeats = 0;

            int tens = 1;
            while ((!deq.empty()) && isStrDigit(deq.back())) {
                repeats = stoi(deq.back()) * tens + repeats;
                tens*=10;
                deq.pop_back();
            }
            string new_string = "";
            while (repeats) {
                new_string+=str;
                repeats-=1;
            }
            deq.push_back(new_string);
        }
    
        string ans;
        while (!deq.empty()) {
            ans+=deq.front();
            deq.pop_front();
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
