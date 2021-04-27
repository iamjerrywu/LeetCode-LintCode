# DFS

## SubSets \(Non-recursion / Iteration\)

### Binary Transformation:

 For a positive integer, `ith` : 1 means selected / 0 mean not selected. Therefore, in range of 0 ~ 2^n - 1 contains 2^n integers, mapping to subsets amount

```text
{1，2，3} subsets represent in 0 ~ 7

0 -> 000 -> {}
1 -> 001 -> {3}
2 -> 010 -> {2}
3 -> 011 -> {2,3}
4 -> 100 -> {1}
5 -> 101 -> {1,3}
6 -> 110 -> {1,2}
7 -> 111 -> {1,2,3}
```

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        for i in range(1 << n):
            subset = []
            for j in range(n):
                # to check whether that bit is 1 / 0
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
```
{% endtab %}

{% tab title="java" %}
```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < (1 << n); i++) {
            List<Integer> subset = new ArrayList<Integer>();
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.add(nums[j]);
                }
            }
            result.add(subset);
        }
        
        return result;
    }
}
```
{% endtab %}

{% tab title="c++" %}
```cpp
class Solution {
public:
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) {
        vector<vector<int>> result;
        const int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (1 << n); i++) {
            vector<int> subset;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.push_back(nums[j]);
                }
            }
            result.push_back(std::move(subset));
        }
        
        return result;
    }
};
```
{% endtab %}
{% endtabs %}

### BFS 

```text
1st layer: []
2nd layer: [1] [2] [3]
3rd layer: [1, 2] [1, 3], [2, 3]
4th layer: [1, 2, 3]
```

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def subsets(self, nums):
        results = []

        if not nums:
            return results

        nums.sort()

        # BFS
        queue = deque()
        queue.append([])

        while queue:
            subset = queue.popleft()
            results.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    nextSubset = list(subset)
                    nextSubset.append(nums[i])
                    queue.append(nextSubset)

        return results
```
{% endtab %}

{% tab title="java" %}
```java
public class Solution {
    
    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    public List<List<Integer>> subsets(int[] nums) {
        // List vs ArrayList （google）
        List<List<Integer>> results = new LinkedList<>();
        
        if (nums == null) {
            return results; // 空列表
        }
        
        Arrays.sort(nums);
        
        // BFS
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(new ArrayList<Integer>());
        
        while (!queue.isEmpty()) {
            List<Integer> subset = queue.poll();
            results.add(subset);
            
            for (int i = 0; i < nums.length; i++) {
                if (subset.size() == 0 || subset.get(subset.size() - 1) < nums[i]) {
                    List<Integer> nextSubset = new ArrayList<Integer>(subset);
                    nextSubset.add(nums[i]);
                    queue.offer(nextSubset);
                }
            }
        }
        
        return results;
    }
}
```
{% endtab %}

{% tab title="c++" %}
```cpp
class Solution {
public:
    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        
        // BFS
        queue<vector<int>> que;
        que.push({});
        
        while (!que.empty()) {
            vector<int> subset = que.front();
            que.pop();
            results.push_back(subset);
            
            for (int i = 0; i < nums.size(); i++) {
                if (subset.size() == 0 || subset.back() < nums[i]) {
                    vector<int> nextSubset = subset;
                    nextSubset.push_back(nums[i]);
                    que.push(nextSubset);
                }
            }
        }
        
        return results;
    }
};
```
{% endtab %}
{% endtabs %}

