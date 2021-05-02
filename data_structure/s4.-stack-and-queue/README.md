---
description: 1 (1E)
---

# Queue

接下来我们来学习一下Java的接口（Interface），其他语言的同学可以跳过这一部分。

Java接口\(Interface\)是一系列方法的声明，是一些方法特征的集合，一个接口只有方法的特征没有方法的实现，因此这些方法可以在不同的地方被不同的类实现，而这些实现可以具有不同的行为。打一个比方，接口好比一个戏中的角色，这个角色有一些特定的属性和操作，然后实现接口的类就好比扮演这个角色的人，一个角色可以由不同的人来扮演，而不同的演员之间除了扮演一个共同的角色之外，并不要求其它的共同之处。

接下来我们来介绍几个面试常用的Interface。

### Set

Set注重独一无二,该体系集合可以知道某物是否已经存在于集合中,不会存储重复的元素。Set的实现类在面试中常用的是：**HashSet** 与 **TreeSet**

* HashSet
  * 无重复数据
  * 可以有空数据
  * 数据无序

```text
Set<String> set = new HashSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //不会重复写入数据
set.add(null);//可以写入空数据
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//数据无序 
}// 输出(无序)为 3 4 1 5 null 2
```

* TreeSet
  * 无重复数据
  * 不能有空数据
  * 数据有序

```text
Set<String> set = new TreeSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //不会重复写入数据
//set.add(null);//不可以写入空数据
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//数据有序
}// 输出(有序)为 1 2 3 4 5
```

### Map

Map用于存储具有映射关系的数据。Map中存了两组数据\(key与value\),它们都可以是任何引用类型的数据，key不能重复，我们可以通过key取到对应的value。Map的实现类在面试中常用是：**HashMap** 和 **TreeMap**.

* HashMap
  * key 无重复，value 允许重复
  * 允许 key 和 value 为空
  * 数据无序

```text
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new HashMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key无重复
        map.put("11","1");//value可以重复
        map.put(null, null);//可以为空
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//输出
/*
key = 11, value = 1
key = null, value = null
key = 1, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//输出顺序与输入顺序无关
```

* TreeMap
  * key 无重复，value 允许重复
  * 不允许有null
  * 有序\(存入元素的时候对元素进行自动排序，迭代输出的时候就按排序顺序输出\)

```text
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new TreeMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key无重复
        map.put("11","1");//value可以重复
        //map.put(null, null);//不可以为空
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//输出
/*
key = 1, value = 1
key = 11, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//输出顺序位String排序后的顺序
```

提问

### List

一个 List 是一个元素有序的、可以重复\(这一点与Set和Map不同\)、可以为 null 的集合，List的实现类在面试中常用是：**LinkedList** 和 **ArrayList**

* LinkedList
  * 基于链表实现
* ArrayList
  * 基于动态数组实现
* LinkedList 与 ArrayList 对比：
  * 对于随机访问get和set，ArrayList绝对优于LinkedList，因为LinkedList要移动指针
  * 对于新增和删除操作add和remove，在已经得到了需要新增和删除的元素位置的前提下，LinkedList可以在O\(1\)的时间内删除和增加元素，而ArrayList需要移动`增加或删除元素之后的所有元素`的位置，时间复杂度是O\(n\)的，因此LinkedList优势较大

### Queue

队列是一种比较重要的数据结构，它支持FIFO\(First in First out\)，即尾部添加、头部删除（先进队列的元素先出队列），跟我们生活中的排队类似。

* PriorityQueue
  * 基于堆\(heap\)实现
  * 非FIFO\(最先出队列的是优先级最高的元素\)
* 普通 Queue
  * 基于链表实现
  * FIFO

