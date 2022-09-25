# Maximize the Confusion of an Exam (LeetCode 2024) (M)

## Problem

A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `ith` question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

* Change the answer key for any question to `'T'` or `'F'` (i.e., set `answerKey[i]` to `'T'` or `'F'`).

Return _the **maximum** number of consecutive_ `'T'`s or `'F'`s _in the answer key after performing the operation at most_ `k` _times_.

**Example 1:**

```
Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
```

**Example 2:**

```
Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
```

**Example 3:**

```
Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
```

**Constraints:**

* `n == answerKey.length`
* `1 <= n <= 5 * 104`
* `answerKey[i]` is either `'T'` or `'F'`
* `1 <= k <= n`

## Solution - Sliding Window

Maintain Two Pointers:

i (the right pointer), j (the left pointer)

Only need to move j pointer when k == 0 (move to the right until reach answerKey\[j] != target, then move one more step

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        F_cnt, F_start = 0, 0
        T_cnt, T_start = 0, 0
        ans = 0
        for end in range(len(answerKey)):
            if answerKey[end] == 'F':
                F_cnt+=1
            while F_cnt > k:
                if answerKey[F_start] == 'F':
                    F_cnt-=1
                F_start+=1
            
            if answerKey[end] == 'T':
                T_cnt+=1
            while T_cnt > k:
                if answerKey[T_start] == 'T':
                    T_cnt-=1
                T_start+=1
            
            ans = max(ans, end - F_start + 1, end - T_start + 1)
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
