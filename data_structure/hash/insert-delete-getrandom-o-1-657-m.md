# Insert Delete GetRandom O(1) 657 (M)

## Problem

Design a data structure that supports all following operations in average `O(1)` time.

* `insert(val)`: Inserts an item val to the set if not already present.
* `remove(val)`: Removes an item val from the set if present.
* `getRandom`: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example

```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

## Solution

To O(1) access the specific val in list, use a hashmap to store their index (from val to index)

Also, when ever remove specific value, place the last value in list in the target location, then pop out last element (can achieve O(1))

![](<../../.gitbook/assets/Screen Shot 2021-04-26 at 12.39.46 AM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
import random
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums, self.val_to_index = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        # can't have repeated values
        if val in self.val_to_index:
            return False
        
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last = self.nums[-1]
        
        # move last element to index
        self.nums[index] = last
        self.val_to_index[last] = index
        
        # remove last element in nums
        self.nums.pop()
        del self.val_to_index[val]

        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
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
