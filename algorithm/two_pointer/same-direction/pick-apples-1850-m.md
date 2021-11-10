# Pick Apples 1850 (M)

## Problem

Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N.\
Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees.\
They want to choose to disjoint segements (one consisting of K trees of Alice and the other consisting of L trees for Bob) so as not to disturb each other. you should return the maximum number of apples that they can collect.

* N is an integer within the range: \[2, 600]
* K and L are integers within the range: \[1, N - 1]
* each element of array A is an integer within the range: \[1, 500]

Example

**Example 1:**

```
input:
A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
Output: 
24
Explanation: 
beacuse Alice can choose tree 3 to 5 and collect 4 + 6 + 3 = 13 apples, and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples.Thus, they will collect 13 + 11 = 24.
```

**Example 2:**

```
Input:
A = [10, 19, 15]
K = 2
L = 2
Output: 
-1
Explanation: 
beacause it is not possible for Alice and Bob to choose two disjoint intervals.
```

## Solution&#x20;

![](<../../../.gitbook/assets/Screen Shot 2021-05-19 at 4.31.11 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        # write your code here
        n = len(A)
        max_apples = float('-inf')
        for i in range(n):
            left_max_l = self.find_max(A, L, 0, i)
            right_max_l = self.find_max(A, L, i, n)
            left_max_k = self.find_max(A, K, 0, i)
            right_max_k = self.find_max(A, K, i, n)

            if left_max_l != -1 and right_max_k != -1:
                max_apples = max(max_apples, left_max_l + right_max_k)
            if left_max_k != -1 and right_max_l != -1:
                max_apples = max(max_apples, left_max_k + right_max_l)
        if max_apples == float('-inf'):
            return -1
        return max_apples

    def find_max(self, A, k, start, end):
        if k > end - start:
            return -1

        apples, max_apples = 0, 0
        for i in range(start, start + k):
            apples += A[i]
        max_apples = apples

        left, right = start, start + k
        while right < end:
            apples+=A[right]
            apples-=A[left]
            max_apples = max(max_apples, apples)

            left+=1
            right+=1
        return max_apples    
    

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
