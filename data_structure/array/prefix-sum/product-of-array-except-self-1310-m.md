# Product of Array Except Self 1310 (M)

## Problem

Given an array of n integers where n > 1, `nums`, return an array output such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in O(n).Example

**Example1**

```
Input: [1,2,3,4]
Output: [24,12,8,6]
Explanation:
2*3*4=24
1*3*4=12
1*2*4=8
1*2*3=6
```

**Example2**

```
Input: [2,3,8]
Output: [24,16,6]
Explanation:
3*8=24
2*8=16
2*3=6
```

Challenge

Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution - Simulation

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        
        for num in nums:
            if num != 0:
                product*=num
            else:
                zero_cnt+=1
        
        res = []
        
        for num in nums:
            if  zero_cnt == 0:
                res.append(product//num)
                continue
            if zero_cnt > 1 or num != 0:
                res.append(0)
            else:
                res.append(product)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Prefix Product

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        length = len(nums)
        result = [1] * length
        prefix_product = 1
        postfix_product= 1

        for i in range(length):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        
        for i in range(length - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix_product[nums.size() + 1];
        int suffix_product[nums.size() + 1];
        // prfix_product[i] * suffix_product[i + 1]
        int prefix_product_val = 1;
        prefix_product[0] = prefix_product_val;
        for (int i = 0; i < nums.size(); i++) {
            prefix_product_val*=nums[i];
            prefix_product[i + 1] = prefix_product_val;
        }

        int suffix_product_val = 1;
        suffix_product[nums.size()] = suffix_product_val;
        for (int i = nums.size() - 1; i >= 0; i--) {
            suffix_product_val*=nums[i];
            suffix_product[i] = suffix_product_val;
        }

        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            ans.push_back(prefix_product[i] * suffix_product[i + 1]);
        }

        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
