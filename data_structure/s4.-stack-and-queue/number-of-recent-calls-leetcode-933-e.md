# Number of Recent Calls (LeetCode 933) (E)

## Problem

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

* `RecentCounter()` Initializes the counter with zero recent requests.
* `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range `[t - 3000, t]`, that is, the new request plus every earlier request that is no more than `3000` milliseconds older.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

&#x20;

**Example 1:**

<pre><code><strong>Input
</strong>["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
<strong>Output
</strong>[null, 1, 2, 3, 3]

<strong>Explanation
</strong>RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
</code></pre>

&#x20;

**Constraints:**

* `1 <= t <= 10`<sup>`9`</sup>
* Each test case will call `ping` with **strictly increasing** values of `t`.
* At most `10`<sup>`4`</sup> calls will be made to `ping`.

## Solution - Queue

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class RecentCounter {
private:
    queue<int> queue;
    // compile-time evaluation and zero runtime memory allocation
    static constexpr int kWindowSize = 3000;
    
public:
    RecentCounter() = default;
    
    int ping(int t) {
        while(!queue.empty() && queue.front() < (t - kWindowSize)) {
            queue.pop();
        }
        queue.push(t);
        return queue.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

## Solution - Vector

In ML compiler runtimes, dynamic memory allocations in the hot path are usually forbidden, and cache misses are costly.

`std::deque` (and by extension `std::queue`) allocates memory in chunks (typically 512 bytes). When it expands, it has to allocate new blocks and maintain an array of pointers to these blocks. Traversing this involves pointer chasing, which is not cache-friendly.

If we leverage the problem constraints—specifically that there will be at most $$ $10^4$ $$ calls to `ping`—we can use a `std::vector` with pre-allocated memory. This guarantees contiguous memory, maximizing L1/L2 cache hits, and completely eliminates dynamic memory allocation during execution.

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class RecentCounter {
private:
    vector<int> pings;
    int head;
    // compile-time evaluation and zero runtime memory allocation
    static constexpr int kWindowSize = 3000;
    
public:
    RecentCounter() : head(0) {
        pings.reserve(10000);
    }
    
    int ping(int t) {
        pings.push_back(t);
        while(pings[head] < t - kWindowSize) {
            head++;
        }
        return pings.size() - head;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
