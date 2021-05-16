# Finding Pairs With a Certain Sum 1865 \(M\)

## Problem



You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

1. **Add** a positive integer to an element of a given index in the array `nums2`.
2. **Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value \(`0 <= i < nums1.length` and `0 <= j < nums2.length`\).

Implement the `FindSumPairs` class:

* `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.
* `void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply `nums2[index] += val`.
* `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

**Example 1:**

```text
Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
```

**Constraints:**

* `1 <= nums1.length <= 1000`
* `1 <= nums2.length <= 105`
* `1 <= nums1[i] <= 109`
* `1 <= nums2[i] <= 105`
* `0 <= index < nums2.length`
* `1 <= val <= 105`
* `1 <= tot <= 109`

## Solution - Hash \(1\)

HashMap storing pairsum as key, and their appearance time as val 

{% hint style="danger" %}
LTE
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.pairs_sum = {}
        for i in range(len(self.nums1)):
            for j in range(len(self.nums2)):
                self.pairs_sum[self.nums1[i] + self.nums2[j]] = self.pairs_sum.get(self.nums1[i] + self.nums2[j], 0) + 1
        

    def add(self, index: int, val: int) -> None:
        for num1 in self.nums1:
            self.pairs_sum[num1 + self.nums2[index]]-=1
        self.nums2[index]+=val
        for num1 in self.nums1:
            self.pairs_sum[num1 + self.nums2[index]] = self.pairs_sum.get(num1 + self.nums2[index], 0) + 1
    
    def count(self, tot: int) -> int:
        if tot in self.pairs_sum:
            return self.pairs_sum[tot]
        else:
            return 0
                    
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * Add: O\(n\)
    * n = total pair sum amounts
  * Count: O\(1\)
* **Space Complexity:**

\*\*\*\*

## Solution - Hash \(2\)

HashMap storing pairsum as key, and their appearance time as val 

{% hint style="danger" %}
LTE
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.pairs_sum = {}
        for i in range(len(self.nums1)):
            for j in range(len(self.nums2)):
                self.pairs_sum[self.nums1[i] + self.nums2[j]] = self.pairs_sum.get(self.nums1[i] + self.nums2[j], 0) + 1
        

    def add(self, index: int, val: int) -> None:
        for num1 in self.nums1:
            self.pairs_sum[num1 + self.nums2[index]]-=1
        self.nums2[index]+=val
        for num1 in self.nums1:
            self.pairs_sum[num1 + self.nums2[index]] = self.pairs_sum.get(num1 + self.nums2[index], 0) + 1
    
    def count(self, tot: int) -> int:
        if tot in self.pairs_sum:
            return self.pairs_sum[tot]
        else:
            return 0
                    
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * Add: O\(n\)
    * n = total pair sum amounts
  * Count: O\(1\)
* **Space Complexity:**

