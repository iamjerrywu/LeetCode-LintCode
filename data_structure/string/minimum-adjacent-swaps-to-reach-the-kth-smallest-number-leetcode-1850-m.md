# Minimum Adjacent Swaps to Reach the Kth Smallest Number \(LeetCode 1850\) \(M\)

## Problem



You are given a string `num`, representing a large integer, and an integer `k`.

We call some integer **wonderful** if it is a **permutation** of the digits in `num` and is **greater in value** than `num`. There can be many wonderful integers. However, we only care about the **smallest-valued** ones.

* For example, when `num = "5489355142"`:
  * The 1st smallest wonderful integer is `"5489355214"`.
  * The 2nd smallest wonderful integer is `"5489355241"`.
  * The 3rd smallest wonderful integer is `"5489355412"`.
  * The 4th smallest wonderful integer is `"5489355421"`.

Return _the **minimum number of adjacent digit swaps** that needs to be applied to_ `num` _to reach the_ `kth` _**smallest wonderful** integer_.

The tests are generated in such a way that `kth` smallest wonderful integer exists.

**Example 1:**

```text
Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355142" -> "5489355412"
- Swap index 8 with index 9: "5489355412" -> "5489355421"
```

**Example 2:**

```text
Input: num = "11112", k = 4
Output: 4
Explanation: The 4th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "11112" -> "11121"
- Swap index 2 with index 3: "11121" -> "11211"
- Swap index 1 with index 2: "11211" -> "12111"
- Swap index 0 with index 1: "12111" -> "21111"
```

**Example 3:**

```text
Input: num = "00123", k = 1
Output: 1
Explanation: The 1st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "00123" -> "00132"
```

**Constraints:**

* `2 <= num.length <= 1000`
* `1 <= k <= 1000`
* `num` only consists of digits.

## Solution 

First find the kth permutation number, then do the swap counts calculation

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num_next = [c for c in num]
        num_original = [c for c in num]
        for i in range(k):
            num_next = self.get_next_permutation(num_next)
        return self.get_swap_count(num_next, num_original)
    
    def get_next_permutation(self, num):
        n = len(num)
        if n <= 1:
            return num
        
        i = n - 1
        while i > 0 and num[i] <= num[i - 1]:
            i-=1
        
        if i != 0:
            j = n - 1
            while num[j] <= num[i - 1]:
                j-=1
            num[j], num[i - 1] = num[i - 1], num[j]
        
        j = n - 1
        while i < j:
            num[i], num[j] = num[j], num[i]
            j-=1
            i+=1
        return num
    def get_swap_count(self, num, num_o):
        cnt = 0
        for i in range(len(num)):
            if num[i] != num_o[i]:
                index = i + 1
                while num_o[index] != num[i]:
                    index +=1
                while index != i:
                    num_o[index], num_o[index - 1] = num_o[index - 1], num_o[index]
                    cnt+=1
                    index-=1
        return cnt
        
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

