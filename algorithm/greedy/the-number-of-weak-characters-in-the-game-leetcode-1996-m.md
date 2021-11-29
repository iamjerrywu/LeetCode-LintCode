# The Number of Weak Characters in the Game (LeetCode 1996) (M)

## Problem

You are playing a game that contains multiple characters, and each of the characters has **two** main properties: **attack** and **defense**. You are given a 2D integer array `properties` where `properties[i] = [attacki, defensei]` represents the properties of the `ith` character in the game.

A character is said to be **weak** if any other character has **both** attack and defense levels **strictly greater** than this character's attack and defense levels. More formally, a character `i` is said to be **weak** if there exists another character `j` where `attackj > attacki` and `defensej > defensei`.

Return _the number of **weak** characters_.

**Example 1:**

```
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
```

**Example 2:**

```
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
```

**Example 3:**

```
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
```

**Constraints:**

* `2 <= properties.length <= 105`
* `properties[i].length == 2`
* `1 <= attacki, defensei <= 105`

## Solution - Brute Force (LTE, pass 39/44)

Find the attack, defense pairs respectively, then find their intersections.&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mapping = {}
        for i in range(len(properties)):
            mapping[tuple(properties[i])] = i
        properties = [tuple(property) for property in properties]
        counter = collections.Counter(properties)
        ori_properties = list(properties)
        
        # sort with attack
        attack_ranges = []
        properties.sort(key = lambda p:(p[0], p[1]))
        for i in range(len(properties) - 1):
            # linear search for larger
            for j in range(i + 1, len(properties)):
                if properties[i][0] < properties[j][0]:
                    attack_ranges.append([i, j, len(properties)])
                    break
        attack_cnt = set()
        for attack_range in attack_ranges:
            for i in range(attack_range[1], attack_range[2]):
                attack_cnt.add((mapping[properties[attack_range[0]]], mapping[properties[i]]))       
        
        # sort with defense
        defense_ranges = []
        properties.sort(key = lambda p:(p[1], p[0]))

        for i in range(len(properties) - 1):
            # linear search for larger
            for j in range(i + 1, len(properties)):
                if properties[i][1] < properties[j][1]:
                    defense_ranges.append([i, j, len(properties)])
                    break
        defense_cnt = set()
        for defense_range in defense_ranges:
            for i in range(defense_range[1], defense_range[2]):
                defense_cnt.add((mapping[properties[defense_range[0]]], mapping[properties[i]]))   
        
        
        ans = 0
        weak_set = set()
        for item in attack_cnt:
            if item in defense_cnt:
                weak_set.add(item[0])
        for weak in weak_set:
            ans+=counter[ori_properties[weak]]
        return ans
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity:**&#x20;

## Solution - Brute Force with Binary Search (LTE, pass39/44)

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mapping = {}
        for i in range(len(properties)):
            mapping[tuple(properties[i])] = i
        properties = [tuple(property) for property in properties]
        counter = collections.Counter(properties)
        ori_properties = list(properties)
        
        # sort with attack
        attack_ranges = []
        properties.sort(key = lambda p:(p[0], p[1]))
        for i in range(len(properties) - 1):
            # binary search for larger
            j = self.bi_search(properties[i][0], properties[i + 1:], 0)
            if j != -1:
                attack_ranges.append([i, i + j + 1, len(properties)])
        attack_cnt = set()
        for attack_range in attack_ranges:
            for i in range(attack_range[1], attack_range[2]):
                attack_cnt.add((mapping[properties[attack_range[0]]], mapping[properties[i]]))       
        
        # sort with defense
        defense_ranges = []
        properties.sort(key = lambda p:(p[1], p[0]))

        for i in range(len(properties) - 1):
            # binary search for larger
            j = self.bi_search(properties[i][1], properties[i + 1:], 1)
            if j != -1:
                defense_ranges.append([i, i + j + 1, len(properties)])
        defense_cnt = set()
        for defense_range in defense_ranges:
            for i in range(defense_range[1], defense_range[2]):
                defense_cnt.add((mapping[properties[defense_range[0]]], mapping[properties[i]]))   
        
        
        ans = 0
        weak_set = set()
        for item in attack_cnt:
            if item in defense_cnt:
                weak_set.add(item[0])
        for weak in weak_set:
            ans+=counter[ori_properties[weak]]
        return ans
    
    def bi_search(self, target, arr, idx):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if arr[mid][idx] <= target:
                start = mid
            else:
                end = mid
        if arr[start][idx] > target:
            return start
        if arr[end][idx] > target:
            return end
        return -1
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity:**&#x20;

## Solution - Stack one pass

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(x[0], x[1]))
        print(properties)
        
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1][0] < a and stack[-1][1] < d:
                stack.pop()
                ans+=1
            stack.append((a, d))
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity:**&#x20;
