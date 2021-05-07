# Car Fleet 1477 \(M\)

## Problem

`N` cars are going to the same destination along a one lane road. The destination is `target` miles away.

Each car `i` has a constant speed `speed[i]` \(in miles per hour\), and initial position `position[i]` miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

How many car fleets will arrive at the destination?

1.`0 <= N <= 10 ^ 4`  
2.`0 < target <= 10 ^ 6`  
3.`0 < speed[i] <= 10 ^ 6`  
4.`0 <= position[i] < target`  
5.All initial positions are different.Example

**Example 1:**

```text
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

**Example 2:**

```text
Input: target = 20, position = [6,2,17], speed = [3,9,2]
Output: 2
Explanation:
The cars starting at 6 and 2 become a fleet, meeting each other at 18.
The other cars from the 17th car can't catch up with it, so it's a team.
Note that no other cars meet these fleets before the destination, so the answer is 2.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param target: the target
    @param position: the initial position
    @param speed: the speed
    @return: How many car fleets will arrive at the destination
    """
    def carFleet(self, target, position, speed):
        # Write your code here
        
        # calculate the time required for each cars (sorted by their init position)
        time = [(target - p)/s for p, s in sorted(zip(position, speed))]
        
        # 1. a single car is a car fleet
        # since if any car surpass the car ahead, it would  only ride dumper to bumper 
        # therefore, traverse from end of the time list, only if next time is larger than current time
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res+=1
                cur = t

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

