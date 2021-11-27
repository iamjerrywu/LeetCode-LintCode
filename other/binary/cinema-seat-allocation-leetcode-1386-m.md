# Cinema Seat Allocation (LeetCode 1386) (M)

## Problem



![](https://assets.leetcode.com/uploads/2020/02/14/cinema\_seats\_1.png)

A cinema has `n` rows of seats, numbered from 1 to `n` and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array `reservedSeats` containing the numbers of seats already reserved, for example, `reservedSeats[i] = [3,8]` means the seat located in row **3** and labelled with **8** is already reserved.

_Return the maximum number of four-person groups you can assign on the cinema seats._ A four-person group occupies four adjacent seats **in one single row**. Seats across an aisle (such as \[3,3] and \[3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/02/14/cinema\_seats\_3.png)

```
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
```

**Example 2:**

```
Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
```

**Example 3:**

```
Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
```

&#x20;

**Constraints:**

* `1 <= n <= 10^9`
* `1 <= reservedSeats.length <= min(10*n, 10^4)`
* `reservedSeats[i].length == 2`
* `1 <= reservedSeats[i][0] <= n`
* `1 <= reservedSeats[i][1] <= 10`
* All `reservedSeats[i]` are distinct.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # cannot declare [0] * n, since n reach 10^9, too large
        seats = collections.defaultdict(int)
        for row, reserve in reservedSeats:
            seats[row- 1] |= (0x1 << (10 - reserve))
        ans = 2 * n
        for seat in seats.values():
            
            # to accept two groups
            if (seat >> 0x1) & 0xFF == 0:
                continue
            # to accept one group, can have three possibilities
            elif (seat >> 0x1) & 0xF == 0 or (seat >> 0x3) & 0xF == 0 or (seat >> 0x5) & 0xF == 0:
                ans-=1
            # if netiehr two or one group is allowed, then deduct by 2
            else:
                ans-=2
        return ans
            
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(k)**
  * **k: reserved rows length (not entire seats length n)**
* **Space Complexity:**
