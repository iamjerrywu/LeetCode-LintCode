# Guess the Word (LeetCode 843) (H)

## Problem

You are given an array of unique strings `words` where `words[i]` is six letters long. One word of `words` was chosen as a secret word.

You are also given the helper object `Master`. You may call `Master.guess(word)` where `word` is a six-letter-long string, and it must be from `words`. `Master.guess(word)` returns:

* `-1` if `word` is not from `words`, or
* an integer representing the number of exact matches (value and position) of your guess to the secret word.

There is a parameter `allowedGuesses` for each test case where `allowedGuesses` is the maximum number of times you can call `Master.guess(word)`.

For each test case, you should call `Master.guess` with the secret word without exceeding the maximum number of allowed guesses. You will get:

* **`"Either you took too many guesses, or you did not find the secret word."`** if you called `Master.guess` more than `allowedGuesses` times or if you did not call `Master.guess` with the secret word, or
* **`"You guessed the secret word correctly."`** if you called `Master.guess` with the secret word with the number of calls to `Master.guess` less than or equal to `allowedGuesses`.

The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

&#x20;

**Example 1:**

<pre><code>Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
<strong>Output:
</strong> You guessed the secret word correctly.
<strong>Explanation:
</strong>master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.</code></pre>

**Example 2:**

<pre><code>Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
<strong>Output:
</strong> You guessed the secret word correctly.
<strong>Explanation:
</strong> Since there are two words, you can guess both.</code></pre>

&#x20;

**Constraints:**

* `1 <= words.length <= 100`
* `words[i].length == 6`
* `words[i]` consist of lowercase English letters.
* All the strings of `wordlist` are **unique**.
* `secret` exists in `words`.
* `10 <= allowedGuesses <= 30`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = len(words)
        mapping = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i > j:
                    mapping[i][j] = mapping[j][i]
                else:
                    mapping[i][j] = self.cal_same(words[i], words[j])
        
        guessed = set()
        
        possibilities = [i for i in range(n)]
        
        while len(guessed) < 10 and len(possibilities) > 0:
            guess = possibilities[random.randint(0, len(possibilities) - 1)]
            cnt = master.guess(words[guess])
            guessed.add(guess)
            
            if cnt == 6:
                return
        possibilities = [j for j in range(len(possibilities)) if mapping[guess][j] == cnt and j not in guessed]
    def cal_same(self, w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                cnt+=1
        return cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
