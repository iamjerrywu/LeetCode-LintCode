# Design Circular Queue (LeetCode 622) (M)

## Problem



Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the `MyCircularQueue` class:

* `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.
* `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.
* `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.
* `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.
* `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.
* `boolean isEmpty()` Checks whether the circular queue is empty or not.
* `boolean isFull()` Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.&#x20;

&#x20;

**Example 1:**

```
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```

&#x20;

**Constraints:**

* `1 <= k <= 1000`
* `0 <= value <= 1000`
* At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.



## Solution&#x20;

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
class MyCircularQueue {
private: 
    vector<int> queue;
    int head = 0;
    int tail = 0;
    int size = 0;
    int max_s = 0;
public:
    MyCircularQueue(int k) {
        max_s = k;
        queue.resize(k);
    }
    
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        queue[tail] = value;
        size+=1;
        tail = (tail + 1)%max_s;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        size-=1;
        head = (head + 1)%max_s;
        return true;
    }
    
    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return queue[head];
    }
    
    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        if (tail == 0) return queue[max_s - 1];
        return queue[tail - 1];
    }
    
    bool isEmpty() {
        return (size == 0);
    }
    
    bool isFull() {
        return (size == max_s);
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */

```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

