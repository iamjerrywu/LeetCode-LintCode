class Node {
   public int val;
   public Node next;
   public Node(int _val) {
       val = _val;
       next = null;
   } 
}

public class MyQueue {
    /*
     * @param item: An integer
     * @return: nothing
     */
    public Node head, tail;
    public void enqueue(int item) {
        // write your code here
        if (head == null) {
            head = new Node(item);
            tail = head;
        } else {
            tail.next = new Node(item);
            tail = tail.next;
        }  
    }

    /*
     * @return: An integer
     */
    public int dequeue() {
        // write your code here
        if (head == null) {
            return -1000;
        }
        int item = head.val;
        head = head.next;
        return item;
    }
}