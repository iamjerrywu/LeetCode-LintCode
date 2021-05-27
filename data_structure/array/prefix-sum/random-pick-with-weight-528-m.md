# Random Pick with Weight 528 \(M\)

## Problem

You are given an array of positive integers `w` where `w[i]` describes the weight of `ith` index \(0-indexed\).

We need to call the function `pickIndex()` which **randomly** returns an integer in the range `[0, w.length - 1]`. `pickIndex()` should return the integer proportional to its weight in the `w` array. For example, for `w = [1, 3]`, the probability of picking the index `0` is `1 / (1 + 3) = 0.25` \(i.e 25%\) while the probability of picking the index `1` is `3 / (1 + 3) = 0.75` \(i.e 75%\).

More formally, the probability of picking index `i` is `w[i] / sum(w)`.

**Example 1:**

```text
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
```

**Example 2:**

```text
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
```

**Constraints:**

* `1 <= w.length <= 10000`
* `1 <= w[i] <= 10^5`
* `pickIndex` will be called at most `10000` times.

## Solution - Linear Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        cur_sum = 0
        for weight in w:
            cur_sum+=weight
            self.prefix_sum.append(cur_sum)
        self.total = cur_sum
        
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        # linear search
        for i, prefix_sum in enumerate(self.prefix_sum):
            if target < prefix_sum:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(2n\)**
  * Establish Prefix\_Sum: O\(n\)
  * Linear Search: O\(n\)
* **Space Complexity: O\(n\)**

\*\*\*\*

## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        cur_sum = 0
        for weight in w:
            cur_sum+=weight
            self.prefix_sum.append(cur_sum)
        self.total = cur_sum
        
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        # binary search search
        return self.binary_search(self.prefix_sum, 0, len(self.prefix_sum) - 1, target) 
    
    def binary_search(self, arr, start, end, target):
        while start + 1 < end:
            mid = (start + end)//2
            
            if arr[mid] <= target:
                start = mid
            else:
                end = mid
            
        if arr[start] > target:
            return start
        elif arr[end] > target:
            return end


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n + logn\)**
  * Establish Prefix\_Sum: O\(n\)
  * Binary Search: O\(n\)
* **Space Complexity:**

