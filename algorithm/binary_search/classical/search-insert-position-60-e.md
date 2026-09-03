# Search Insert Position 60 (E)

## Problem

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume **NO** duplicates in the array.Example

**Example 1:**

Input:

```
array = [1,3,5,6]
target = 5
```

Output:

```
2
```

Explanation:

5 is indexed to 2 in the array.

**Example 2:**

Input:

```
array = [1,3,5,6]
target = 2
```

Output:

```
1
```

Explanation:

2 should be inserted into the position with index 1.

**Example 3:**

Input:

```
array = [1,3,5,6]
target = 7
```

Output:

```
4
```

Explanation:

7 should be inserted into the position with index 4.

**Example 4:**

Input:

```
array = [1,3,5,6]
target = 0
```

Output:

```
0
```

Explanation:

0 should be inserted into the position with index 0.Challenge

O(log(n)) time

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
        
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int start = 0, end = nums.size() - 1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;

            if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }            
        }

        if (nums[start] >= target) return start;
        if (nums[end] >= target) return end;
        return nums.size();
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
