# Tweet Counts Per Frequency 1348 \(M\)

## Problem

A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller **time chunks** based on a certain frequency \(every **minute**, **hour**, or **day**\).

For example, the period `[10, 10000]` \(in **seconds**\) would be partitioned into the following **time chunks** with these frequencies:

* Every **minute** \(60-second chunks\): `[10,69]`, `[70,129]`, `[130,189]`, `...`, `[9970,10000]`
* Every **hour** \(3600-second chunks\): `[10,3609]`, `[3610,7209]`, `[7210,10000]`
* Every **day** \(86400-second chunks\): `[10,10000]`

Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period \(`10000` in the above example\).

Design and implement an API to help the company with their analysis.

Implement the `TweetCounts` class:

* `TweetCounts()` Initializes the `TweetCounts` object.
* `void recordTweet(String tweetName, int time)` Stores the `tweetName` at the recorded `time` \(in **seconds**\).
* `List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)` Returns a list of integers representing the number of tweets with `tweetName` in each **time chunk** for the given period of time `[startTime, endTime]` \(in **seconds**\) and frequency `freq`.
  * `freq` is one of `"minute"`, `"hour"`, or `"day"` representing a frequency of every **minute**, **hour**, or **day** respectively.

**Example:**

```text
Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);                              // New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60);                             // New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10);                             // New tweet "tweet3" at time 10
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; chunk [0,59] had 2 tweets
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120);                            // New tweet "tweet3" at time 120
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; chunk [0,210] had 4 tweets
```

**Constraints:**

* `0 <= time, startTime, endTime <= 109`
* `0 <= endTime - startTime <= 104`
* There will be at most `104` calls **in total** to `recordTweet` and `getTweetCountsPerFrequency`.

## Solution - Hash + Linear Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class TweetCounts:

    def __init__(self):
        self.dict = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if (tweetName not in self.dict):
            self.dict[tweetName] = [time]
        else:
            self.dict[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.dict:
            return []
        chunk = 1
        if freq == 'minute':
            chunk = 60
        if freq == 'hour':
            chunk = 3600
        if freq == 'day':
            chunk = 86400
        size = int((endTime - startTime)/chunk) + 1
        res = [0 for _ in range(size)]
        for time in self.dict[tweetName]:
            if startTime <= time <= endTime:
                time_id = int((time - startTime)/chunk)
                res[time_id]+=1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * recordTweet\(\):  O\(1\)
  * getTweetCountsPerFrequency\(\): O\(n\)
* **Space Complexity: O\(n\)**

## Solution - Hash + Binary Serach

### Code

{% tabs %}
{% tab title="python" %}
```python
class TweetCounts:

    def __init__(self):
        self.dict = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if (tweetName not in self.dict):
            self.dict[tweetName] = [time]
        else:
            self.dict[tweetName].append(time)
            # depend on which functions called more frequently
            # if recordTweet() is more frequently called, sort here
            self.dict[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.dict:
            return []
        chunk = 1
        if freq == 'minute':
            chunk = 60
        if freq == 'hour':
            chunk = 3600
        if freq == 'day':
            chunk = 86400
        size = int((endTime - startTime)/chunk) + 1
        res = [0 for _ in range(size)]
        times = self.dict[tweetName]
        # depend on which functions called more frequently
        # if getTweetCountsPerFrequency is more frequent, don't sort here
        # times.sort()

        if startTime > times[-1]:
            return res
        start_id = self.binary_search(0, len(times) - 1, times, startTime)
        for id in range(start_id, len(times)):
            if times[id] > endTime:
                break
            time_id = int((times[id] - startTime)/chunk)
            res[time_id]+=1
        return res
    
    def binary_search(self, start, end, times, target):
        while start + 1 < end:
            mid = start + (end - start)//2
            if times[mid] > target:
                end = mid
            elif times[mid] < target:
                start = mid
            else:
                return mid
        if times[start] >= target:
            return start
        if times[end] >= target:
            return end


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

