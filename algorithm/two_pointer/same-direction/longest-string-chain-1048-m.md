# Maximize the Confusion of an Exam \(LeetCode 2024\) \(M\)

## Problem

A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer \(multiple trues or multiple falses in a row\).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `ith` question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

* Change the answer key for any question to `'T'` or `'F'` \(i.e., set `answerKey[i]` to `'T'` or `'F'`\).

Return _the **maximum** number of consecutive_ `'T'`s or `'F'`s _in the answer key after performing the operation at most_ `k` _times_.

**Example 1:**

```text
Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
```

**Example 2:**

```text
Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
```

**Example 3:**

```text
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

i \(the right pointer\), j \(the left pointer\)

Only need to move j pointer when k == 0 \(move to the right until reach answerKey\[j\] != target, then move one more step

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        return max(self.find_max_length(answerKey, 'T', k), self.find_max_length(answerKey, 'F', k))
    
    def find_max_length(self, answerKey, target, k):
        max_len = 0
        length = 0
        j = 0
        for i in range(len(answerKey)):
            if answerKey[i] == target:
                length+=1
            else:
                if k == 0:
                    while answerKey[j] == target:
                        j+=1
                    # move one more step
                    j+=1
                    k+=1
                k-=1
                length = i - j + 1
            max_len = max(max_len, length)
        return max_len          
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

