public class MyQueue {
    /*
     * @param item: An integer
     * @return: nothing
     */

    int MAXSIZE = 100000;
    int[] queue = new int[MAXSIZE];
    int head = 0, tail = 0;
    
    public void enqueue(int item) {
        // write your code here
        // if queue full
        if (tail == MAXSIZE) {
            return; 
        }
        queue[tail++] = item;
    }

    /*
     * @return: An integer
     */
    public int dequeue() {
        // write your code here
        // if queue empty 
        if (head == tail) {
            return -1;
        }
        int item = queue[head++];
        return item; 
    }
}