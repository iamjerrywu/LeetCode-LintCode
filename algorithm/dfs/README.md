---
description: 18 (14M/4H)
---

# DFS

## Recursion 

### Stack vs Heap

我们通常所说的内存空间，包含了两个部分：栈空间（Stack space）和堆空间（Heap space）

当一个程序在执行的时候，操作系统为了让进程可以使用一些固定的不被其他进程侵占的空间用于进行函数调用，递归等操作，会开辟一个固定大小的空间（比如 8M）给一个进程使用。这个空间不会太大，否则内存的利用率就很低。这个空间就是我们说的栈空间，Stack space。

我们通常所说的栈溢出（Stack Overflow）是指在函数调用，或者递归调用的时候，开辟了过多的内存，超过了操作系统余留的那个很小的固定空间导致的。那么哪些部分的空间会被纳入栈空间呢？栈空间主要包含如下几个部分：

1. 函数的参数与返回值
2. 函数的局部变量

我们来看下面的这段代码：  
Java:

```text
public int f(int n) {
    int[] nums = new int[n];
    int sum = 0;
    for (int i = 0; i < n; i++) {
        nums[i] = i;
        sum += i;
    }
    return sum;
}
```

Python:

```text
def f(n):
    nums = [0]*n  # 相当于Java中的new int[n]
    sum = 0
    for i in range(n):
        nums[i] = i
        sum += i
    return sum
```

C++:

```text
int f(int n) {
   int *nums = new int[n];
    int sum = 0;
    for (int i = 0; i < n; i++) {
        nums[i] = i;
        sum += i;
    }
    return sum;
}
```

根据我们的定义，参数 n，最后的函数返回值f，局部变量 sum 都很容易的可以确认是放在栈空间里的。那么主要的难点在 nums。

这里 nums 可以理解为两个部分：

1. 一个名字叫做 nums 的局部变量，他存储了指向内存空间的一个地址（Reference），这个地址也就是 4 个字节（32位地址总线的计算机，地址大小为 4 字节）
2. new 出来的，一共有 n 个位置的整数数组，int\[n\]。一共有 4 \* n 个字节。

这里 nums 这个变量本身，是存储在栈空间的，因为他是一个局部变量。但是 nums 里存储的 n 个整数，是存储在`堆空间`里的，Heap space。他并不占用栈空间，并不会导致栈溢出。

在大多数的编程语言中，特别是 Java, Python 这样的语言中，万物皆对象，基本上每个变量都包含了变量自己和变量所指向的内存空间两个部分的逻辑含义。

来看这个例子：

Java:

```text
public int[] copy(int[] nums) {
    int[] arr = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
        arr[i] = nums[i]
    }
    return arr;
}

public void main() {
    int[] nums = new int[10];
    nums[0] = 1;
    int[] new_nums = copy(nums);
}
```

Python:

```text
def copy(nums):
    arr = [0]*len(nums)  # 相当于Java中的new int[nums.length]
		for i in range(len(nums)):
        arr[i] = nums[i]
    return arr
		
# 用list comprehension实现同样功能
def copy(nums):
    arr = [x for x in nums]
    return arr
		
# 以下相当于Java中的main函数
if __name__ == "__main__":
    nums = [0]*10
    nums[0] = 1
    new_nums = copy(nums)
```

C++

```text
int* copy(int nums[], int length) {
    int *arr = new int[length];
    for (int i = 0; i < length; i++) {
        arr[i] = nums[i];
    }
    return arr;
}

int main() {
    int *nums = new int[10];
    nums[0] = 1;
    int *new_nums = copy(nums, 10);
	return 0;
}
```

在 copy 这个函数中，arr 是一个局部变量，他在 copy 函数执行结束之后就会被销毁。但是里面 new 出来的新数组并不会被销毁。  
这样，在 main 函数里，new\_nums 里才会有被复制后的数组。所以可以发现一个特点：

> 栈空间里存储的内容，会在函数执行结束的时候被撤回

简而言之可以这么区别栈空间和堆空间：

> new 出来的就放在堆空间，其他都是栈空间

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

