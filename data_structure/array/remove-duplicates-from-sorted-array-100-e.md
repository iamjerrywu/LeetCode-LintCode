# Remove Duplicates from Sorted Array 100 (E)

## Problem

Given a sorted array, 'remove' the duplicates in place such that each element appear only once and return the 'new' length.

Do not allocate extra space for another array, you must do this in place with constant memory.Example

**Example 1:**

Input:

```
nums = []
```

Output:

```
0
```

Explanation:

The array is empty.\
**Example 2:**

Input:

```
nums = [1,1,2]
```

Output:

```
2
```

Explanation:

uniqued array: \[1,2]

## Solution - Two Pointer

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index+=1
                nums[index] = nums[i]
        return index + 1


```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] != nums[l]) {
                l+=1;
                nums[l] = nums[r];
            }
        }
        return l + 1;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
