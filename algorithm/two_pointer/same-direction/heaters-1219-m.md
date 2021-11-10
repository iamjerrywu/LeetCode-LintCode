# Heaters 1219 (M)

## Problem

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

1.Numbers of houses and heaters you are given are non-negative and will not exceed 25000.\
2.Positions of houses and heaters you are given are non-negative and will not exceed 10^9.\
3.As long as a house is in the heaters' warm radius range, it can be warmed.\
4.All the heaters follow your radius standard and the warm radius will the same.Example

**Example 1:**

```
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
```

**Example 2:**

```
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
```

## Solution - Binary Search

When house choosing heater, must be following two cases:

* Left last one heater <= house location&#x20;
* Right first one heater >= house location

![](<../../../.gitbook/assets/Screen Shot 2021-05-10 at 11.04.46 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        
        # sort the heaters, since we want to find the house position inside heaters 
        heaters.sort()

        heat_radius = 0
        for house in houses:
            radius = self.get_minimum_radius(house, heaters)
            heat_radius = max(heat_radius, radius)
        return heat_radius
    
    def get_minimum_radius(self, house, heaters):
        left, right = 0, len(heaters) - 1
        while left + 1 < right:
            mid = (left + right)//2
            if heaters[mid] <= house:
                left = mid
            else:
                right = mid
        
        # find answer btw left/right
        left_distance = abs(heaters[left] - house)
        right_distance = abs(heaters[right] - house)

        return min(left_distance, right_distance)

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O((n+m)\*logm)**
  * Sort: O(mlogm)
  * Traverse + Binary search: O(n \* logm)
* **Space Complexity: O(n)**

## Solution - Two Pointer

Consider if heaters\[j] can provide heat to house\[i]

* If heaters\[j] is closer to house\[i] than heaters\[j+1] => then i+1
* If heaters\[j + 1] is closer to house\[i] then heaters\[j] => then j + 1

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        houses.sort()
        heaters.sort()
        n, m = len(houses), len(heaters)
        i, j = 0, 0
        heat_radius = 0
        while i < n and j < m:
            now_radius = abs(heaters[j], houses[i])
            next_radius = float('inf')
            if j < m - 1:
                next_radius = abs(heaters[j + 1] - houses[i])
            if now_radius < next_radius:
                heat_radius = max(heat_radius, now_radius)
                i+=1
            else:
                j+=1
        return heat_radius


```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn + mlogm)**
  * Sort: O(nlogn + mlogm)
  * traverse: O(n + m)
* **Space Complexity: O(1)**
