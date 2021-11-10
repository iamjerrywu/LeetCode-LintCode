# Sum Game (LeetCode 1927) (M)

## Problem

Alice and Bob take turns playing a game, with **Alice starting first**.

You are given a string `num` of **even length** consisting of digits and `'?'` characters. On each turn, a player will do the following if there is still at least one `'?'` in `num`:

1. Choose an index `i` where `num[i] == '?'`.
2. Replace `num[i]` with any digit between `'0'` and `'9'`.

The game ends when there are no more `'?'` characters in `num`.

For Bob to win, the sum of the digits in the first half of `num` must be **equal** to the sum of the digits in the second half. For Alice to win, the sums must **not be equal**.

* For example, if the game ended with `num = "243801"`, then Bob wins because `2+4+3 = 8+0+1`. If the game ended with `num = "243803"`, then Alice wins because `2+4+3 != 8+0+3`.

Assuming Alice and Bob play **optimally**, return `true` _if Alice will win and _`false` _if Bob will win_.

**Example 1:**

```
Input: num = "5023"
Output: false
Explanation: There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
```

**Example 2:**

```
Input: num = "25??"
Output: true
Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
```

**Example 3:**

```
Input: num = "?3295???"
Output: false
Explanation: It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
```

**Constraints:**

* `2 <= num.length <= 105`
* `num.length` is **even**.
* `num` consists of only digits and `'?'`.

## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        # number of ?s
        a = b = 0

        # left sums and right sums
        l = r = 0

        # first half: counting ?s and sums
        for c in num[ : n // 2]:
            if c == "?":
                a += 1
            else:
                l += int(c)

        # second half: counting ?s and sums
        for c in num[n // 2 : ]:
            if c == "?":
                b += 1
            else:
                r += int(c)

        # # Odd ?s, Alice will always win cuz she has the final say
        # if (a + b) % 2 == 1:
        #     return True

        # The only situation Bob can win
        
        # using 4.5 is because (Alice filled 0 / Bob filled 9 or Alice filled 1 / Bob filled 0) 
        if l - r == 9 * (b - a) // 2:
            return False
        return True

        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
