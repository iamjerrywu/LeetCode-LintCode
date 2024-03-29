# Design A Leaderboard (LeetCode 1244) (M)

## Problem



Design a Leaderboard class, which has 3 functions:

1. `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
2. `top(K)`: Return the score sum of the top `K` players.
3. `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

&#x20;

**Example 1:**

```
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
```

&#x20;

**Constraints:**

* `1 <= playerId, K <= 10000`
* It's guaranteed that `K` is less than or equal to the current number of players.
* `1 <= score <= 100`
* There will be at most `1000` function calls.



## Solution - Sort

{% tabs %}
{% tab title="Python" %}
```python
class Leaderboard:

    def __init__(self):
        self.rec = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.rec[playerId]+=score
    def top(self, K: int) -> int:
        score_list = list(self.rec.values())
        score_list.sort(reverse = True)
        return sum(score_list[:K])

    def reset(self, playerId: int) -> None:
        self.rec[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**



## Solution - Heap

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Leaderboard:

    def __init__(self):
        self.rec = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.rec[playerId]+=score
    def top(self, K: int) -> int:
        heap = []
        for val in self.rec.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.rec[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Leaderboard {
public:
    map<int, int> mapping;
    priority_queue<int> q;
    Leaderboard() {
        
    }
    
    void addScore(int playerId, int score) {
        mapping[playerId] += score;
    }
    
    int top(int K) {
        int sum_val = 0;
        for (auto kv : mapping) {
            q.push(-kv.second);
            if(q.size() > K) {
                q.pop();
            }
        }
        while(!q.empty()) {
            sum_val+= -q.top();
            q.pop();
        }
        return sum_val;
    }
    
    void reset(int playerId) {
        mapping.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**



## Solution - SortedDict

{% tabs %}
{% tab title="Python" %}
```python
from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.scores = dict() # playerId -> score
        self.sortedScores = SortedDict() # playerscore -> ppl amount

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            pre_score = self.scores[playerId]
            amt = self.sortedScores[-pre_score]
            if amt == 1:
                del self.sortedScores[-pre_score]
            else:
                self.sortedScores[-pre_score] = amt - 1
            new_score = pre_score + score
            self.scores[playerId] = new_score
            self.sortedScores[-new_score] = self.sortedScores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        cnt, total = 0, 0
        for score, amt in self.sortedScores.items():
            for _ in range(amt):
                total+=score
                cnt+=1
                
                if cnt == K:
                    return -total

    def reset(self, playerId: int) -> None:
        pre_score = self.scores[playerId]
        if self.sortedScores[-pre_score] == 1:
            del self.sortedScores[-pre_score]
        else:
            self.sortedScores[-pre_score]-=1
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
