# Relative Ranks 1200 \(E\)

## Problem

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

N is a positive integer and won't exceed 10,000.  
All the scores of athletes are guaranteed to be unique.Example

Example 1:

```text
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the right two athletes, you just need to output their relative ranks according to their scores.
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        if not nums:
            return ['']
        sorted_nums = sorted(nums, reverse = True)
        sorted_record = {}
        for i in range(len(sorted_nums)):
            if i == 0:
                sorted_record[sorted_nums[i]] = "Gold Medal"
            elif i == 1:
                sorted_record[sorted_nums[i]] = "Silver Medal"
            elif i == 2:
                sorted_record[sorted_nums[i]] = "Bronze Medal"
            else:
                sorted_record[sorted_nums[i]] = str(i + 1)

        res = []
        for num in nums:
            res.append(sorted_record[num])
        return res
        
        

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

