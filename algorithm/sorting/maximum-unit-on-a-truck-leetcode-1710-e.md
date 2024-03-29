# Maximum Unit on a Truck (LeetCode 1710) (E)

## Problem

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

* `numberOfBoxesi` is the number of boxes of type `i`.
* `numberOfUnitsPerBoxi` is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return _the **maximum** total number of **units** that can be put on the truck._

**Example 1:**

```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```

**Example 2:**

```
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
```

**Constraints:**

* `1 <= boxTypes.length <= 1000`
* `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
* `1 <= truckSize <= 106`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda box:-box[1])
        ans = 0
        for box in boxTypes:
            if truckSize >= box[0]:
                truckSize-=box[0]
                ans+=box[0] * box[1]
            else:
                ans+=truckSize * box[1]
                return ans
        return ans
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    static bool compare(vector<int> b1, vector<int> b2) {
        return b1[1] > b2[1];
    }
    
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), compare);

        int res = 0;
        for (vector<int> box : boxTypes) {
            for (int i = 0; i < box[0]; i++) {
                if (truckSize == 0) return res;
                res+=box[1];
                truckSize-=1;
            }
        }
        return res;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O(nlogn)**
  * n: len(boxTypes)
* **Space Complexity:  O(n)**
