public class MyQueue {
    /*
     * @param item: An integer
     * @return: nothing
     */
    
    public int head, tail;
    public int SIZE = 1000000;
    public int[] queue = new int[SIZE];

    public void enqueue(int item) {
        // write your code here
        if (((tail + 1) % SIZE) == head) {
            return;
        }

        queue[tail] = item;
        tail = (tail + 1) % SIZE;
    } 

    /*
     * @return: An integer
     */
    public int dequeue() {
        // write your code here
        if ((head % SIZE) == tail) {
            return -1000;
        }
        int item = queue[head];
        head = (head + 1) % SIZE;
        return item;
    }
}