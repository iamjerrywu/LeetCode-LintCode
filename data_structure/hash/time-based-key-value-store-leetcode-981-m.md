# Time Based Key-Value Store (LeetCode 981) (M)

## Problem

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

* `TimeMap()` Initializes the object of the data structure.
* `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
* `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

**Example 1:**

```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "ba2r" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

**Constraints:**

* `1 <= key.length, value.length <= 100`
* `key` and `value` consist of lowercase English letters and digits.
* `1 <= timestamp <= 107`
* All the timestamps `timestamp` of `set` are strictly increasing.
* At most `2 * 105` calls will be made to `set` and `get`.

## Solution - Linear Get()

{% tabs %}
{% tab title="Python" %}
```python
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.mapping:
            prev_key = ""
            for val in self.mapping[key]:
                if val[1] <= timestamp:
                    prev_key = val[0]
            return prev_key
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * Set(): O(1)
  * Get(): O(n)
* **Space Complexity:**

## Solution - Binary Search Get()

{% tabs %}
{% tab title="Python" %}
```python
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mapping:
            return self.binary_search(timestamp, self.mapping[key])
        else:
            return ""
    
    def binary_search(self, timestamp, vals_times):
        start, end = 0, len(vals_times) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if vals_times[mid][1] < timestamp:
                start = mid
            else:
                end = mid
        
        if vals_times[end][1] <= timestamp:
            return vals_times[end][0]
        if vals_times[start][1] <= timestamp:
            return vals_times[start][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```
{% endtab %}

{% tab title="C++" %}
```cpp
class TimeMap {
public:
    map<string, vector<pair<string, int>>> mapping;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if (!mapping.count(key)) {
            vector<pair<string, int>> store = {pair<string, int>(value, timestamp)};
            mapping[key] = store;
        } else {
            mapping[key].push_back(pair<string, int>(value, timestamp));
        }
    }
    
    string get(string key, int timestamp) {
        if (!mapping.count(key)) return "";
        vector<pair<string, int>> &vec = mapping[key];
        int start = 0, end = vec.size() - 1;
        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (vec[mid].second < timestamp) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (vec[end].second <= timestamp) return vec[end].first;
        if (vec[start].second <= timestamp) return vec[start].first;
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
*
  * Set(): O(1)
  * Get(): O(logn)
* **Space Complexity:**
