# Pick Fruits 1643 (M)

## Problem

Xiaohong went to the orchard to pick fruit. There are 2 baskets that can hold countless fruits, but each baskert can only hold one type of fruit. Start from the tree at any position and pick it to the right. Stop picking when one of the following two conditions occurs, 1. encountered the third type of fruit, no basket can be put, 2. meet the end. Returns the maximum number of fruits that can be picked.The fruit array is represented by `arr`.

The length of the array does not exceed 100,000Example

**Example 1:**

```
Input：[1,2,1,3,4,3,5,1,2]Output：3Explanation：Select [1, 2, 1] or [3, 4, 3]. The length is 3.
```

**Example 2:**

```
Input：[1,2,1,2,1,2,1]Output：7Explanation：Select  [1, 2, 1, 2, 1, 2, 1].The length is 7.
```

## Solution - Brute Force Enumeration

```python
class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray
    """
    def pickFruits(self, arr):
        # Write your code here.
        max_length = 0
        for start in range(len(arr)):
            for end in range(start, len(arr)):
                s = set()
                for i in range(start, end + 1):
                    s.add(arr[i])
                print(s)
                if len(s) <= 2:
                    max_length = max(max_length, end - start + 1)
        return max_length
```

### Complexity Analysis

* **Time Complexity: O(n^3)**
* **Space Complexity: O(n)**

## Solution - Two Pointers

```python
class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray
    """
    def pickFruits(self, arr):
        # Write your code here.
        j, different_nums = 0, 0
        cnt, max_len = collections.defaultdict(int), 0
        for i in range(len(arr)):
            while j < len(arr) and different_nums < 3:
                # cnt default values as all 0
                cnt[arr[j]]+=1
                if cnt[arr[j]] == 1:
                    different_nums +=1
                j+=1
                if different_nums <= 2:
                    max_len = max(max_len, j - i)
            # once differnet nums too much, move i
            cnt[arr[i]] -=1
            if cnt[arr[i]] == 0:
                different_nums -=1
        
        return max_len
```

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****

## Solution - Two Pointers (2)

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        cnt, ans = 0, 0
        s = 0
        for i in range(len(fruits)):
            fruit = fruits[i]
            if fruit not in basket and len(basket) == 2:
                while len(basket) >= 2:
                    basket[fruits[s]]-=1
                    if basket[fruits[s]] == 0:
                        basket.pop(fruits[s])
                    cnt-=1
                    s+=1
                basket[fruit]+=1
                cnt+=1
            else:
                basket[fruit]+=1
                cnt+=1
            ans = max(ans, cnt)
        return ans
                    
```

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
