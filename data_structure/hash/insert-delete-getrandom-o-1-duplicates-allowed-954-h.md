# Insert Delete GetRandom O\(1\) - Duplicates Allowed 954 \(H\)

## Problem

Design a data structure that supports all following operations in average **O\(1\)** time.

**Duplicate elements are allowed.**

1. `insert(val):` Inserts an item val to the collection.
2. `remove(val):` Removes an item val from the collection if present.
3. `getRandom:` Returns a random element from current collection of elements. The probability of each element being returned is `linearly related` to the number of same value the collection contains.

Example

**Example 1:**

```text
Input:
insert(1)
insert(1)
insert(2)
getRandom()
remove(1)

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
```

**Example 2:**

```text
Input:
insert(1)
insert(1)
getRandom()
remove(1)
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.val_to_index = [], {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val not in self.val_to_index:
            index_set = set([len(self.nums) - 1])
            self.val_to_index[val] = index_set
            return True
        else:
            self.val_to_index[val].add(len(self.nums) - 1)
            return True
        
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val].pop()
        if len(self.val_to_index[val]) == 0:
            del self.val_to_index[val]

        last = self.nums[-1]
        
        # move last element to index
        self.nums[index] = last
        if last not in self.val_to_index:
            index_set = set([index])
            self.val_to_index[last] = index_set
        else:
            self.val_to_index[last].add(index)
        
        # remove last element in nums
        self.val_to_index[last].remove(len(self.nums) - 1)
        if len(self.val_to_index[last]) == 0:
            del self.val_to_index[last]
        self.nums.pop()
        
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
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

