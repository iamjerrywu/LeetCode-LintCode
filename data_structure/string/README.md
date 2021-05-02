---
description: 5 (1E/4M)
---

# String

## Knowledge about String 

{% tabs %}
{% tab title="Java" %}
```java
public class StringTest {  
    public static void main(String[] args) {
        String H = "hello";  
        String H_1 = H;  
        String H_2 = "hel";  
        String H_3 = H_2 + "lo";  
        String H_4 = H_2.concat("lo");  
              
        System.out.println(H);            // hello
        System.out.println(H_1);          // hello
        System.out.println(H_2);          // hel
        System.out.println(H_3);          // hello
        System.out.println(H_4);          // hello
        
        //==等号测试  
        System.out.println(H == H_1);     // true
        System.out.println(H == H_3);     // false
        System.out.println(H == H_4);     // false
        System.out.println(H_3 == H_4);   // false
              
        //equals函数测试  
        System.out.println(H.equals(H_1));   // true
        System.out.println(H.equals(H_3));   // true
        System.out.println(H.equals(H_4));   // true
        System.out.println(H_3.equals(H_4)); // true
              
        //StringBuilder测试  
        StringBuilder helloBuilder = new StringBuilder("hel");  
        System.out.println(helloBuilder.equals(H_2));    // false
   }   
}  
```
{% endtab %}

{% tab title="Python" %}
```python

```
{% endtab %}

{% tab title="C++" %}
```cpp

```
{% endtab %}
{% endtabs %}

**为什么Java中不能直接用 == 判等？**

Java中**String**类型具有一个**equals**的方法可以用于判断两种字符串是否相等，但是这种相等又与运算符“==”所判断的“相等”有所不同。

* 使用“==”判断的相等时指相同的内存地址，也就是同一个对象实例。
* 使用equals方法判断的相等在不同的对象中实现不同，意义也不同。

Java中所有的对象都继承自Object 类，在Object类中实现的equals\(\) 方法如下：

```text
public boolean equals(Object obj) {  
    return (this == obj);  
} 
```

也就是等同于“==”, 只有在内存一样的时候才返回true。

* String类重写了这个方法，重写后的方法首先判断内存地址是否一致，如果一致返回true，否则比较字符串的内容是否一致，如果内容一致也返回true。因此，使用String类的**equals**方法是比较内容是否一致，而使用“==”是比较实例是否是同一个实例。
* StringBuilder类并没有重写equals方法，因此使用equals比较时，需要时同一个实例才会返回true。否则返回false。

**Java创建字符串的过程**

在我们使用“=”赋值时，如果内存中已经有这个字符串，就会直接将其地址给这个变量，不会产生新的字符串。  
如上面代码中的“H”与“H\_1”， 二者指向同一个实例。

当我们使用“+”或者“concat”方法拼接字符串的时候，会创建一个新的字符串，占用新的内存空间，因此使用“==”判断时返回false。

**Java 中String的引用方式**

```text
public class Hello {
    public static void main(String argv[]) {
        String sa = "abc";
        String sb = "abc";
        if (sa == sb) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
```

上面这段代码的结果是Yes。

程序运行的过程是这样，先在内存中创建字符串“abc”, 然后将地址的引用给了变量sa， 随后又把这个地址的引用给了sb。因此sa和sb引用的是同一段内存。  
由于String类是一个不可更改的类。字符串不可被更改，所以这样的方式并不会产生问题。

**Python中判断字符串相等的方式**

Python可以直接使用==判断字符串是否相等:

```text
s = "Hello"
s1 = s
s2 = "He"
s3 = "llo"
s4 = s2+s3

print(s)   # "Hello"
print(s1)  # "Hello"
print(s2)  # "He"
print(s3)  # "llo"
print(s4)  #  "Hello"

print(s == s1)  # True
print(s == s2)  # False
print(s == s3)  # False
print(s == s4)  # True
```

代码中的注释为运行结果。

**C++中判断字符串相等的方式**

跟Python类似，C++也可以直接使用==比较字符串是否相等。

```text
string s = "Hello";
string s1 = s;
string s2 = "He";
string s3 = "llo";
string s4 = s2+s3;

cout << s  << endl;  // "Hello"
cout << s1 << endl;  // "Hello"
cout << s2 << endl;  // "He"
cout << s3 << endl;  // "llo"
cout << s4 << endl;  //  "Hello"

cout << (s == s1) << endl;  // 1
cout << (s == s2) << endl;  // 0
cout << (s == s3) << endl;  // 0
cout << (s == s4) << endl;  // 1
```

接下来我们来看一下如何遍历字符串

### 如何遍历字符串

**Java:**

```text
String s = new String("Hello");
for(int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    // ....
}
```

使用上述方式来遍历Java中的字符串。  
其中s.length\(\) 获取字符串的长度。  
String 不支持下标索引的方式访问，所以需要使用charAt\(i\)的方式访问对应位置的字符。同时也就没有办法使用下标的方式对String进行修改。

String是一种不可变类，字符串一但生成就不能被改变。例如我们使用\*\*‘+’进行字符串连接，会产生新的字符串，原串不会发生任何变化；使用replace\(\)\*\* 进行替换某些字符的时候也是产生新的字符串，不会更改原有字符串。

**Python:**

```text
s = "Hello"
for i in range(len(s)):
    s[i].....
#另一种写法
for c in s:
    c......
```

使用上述方式来遍历python中的字符串。  
其中len\(s\) 获取字符串的长度, 使用s\[i\]可以访问对应位置的字符。  
Python中的字符串是不可变的，字符串一但生成就不能被改变，因此不能直接用s\[i\]=x的方式改变字符串。例如我们使用\*\*‘+’进行字符串连接，会产生新的字符串，原串不会发生任何变化；使用replace\(\)\*\* 进行替换某些字符的时候也是产生新的字符串，不会更改原有字符串。

**C++:**

```text
string s = "Hello";
for (int i = 0; i < s.size(); ++i) {
    s[i] ...
}
// 或者
for (char c: s) {
    c...
}
// 跟上一种写法一样，但是此时改变c的值会同时改变原字符串
for (char& c: s) {
   c...
}
```

使用上述方式来遍历python中的字符串。  
其中s.size\(\) 获取字符串的长度, 使用s\[i\]可以访问对应位置的字符。c++中的字符串是可变的，可以直接用s\[i\]=x的方式改变字符串。

在字符串问题中，我们会看到null和"",但这两者有什么区别呢

### null和 "" 有什么区别

#### null 表示空对象

Java中一切皆对象的思想，null用来表示空对象。我们不能对空对象做任何操作，除了"=" 和"=="。  
Java:

```text
String s = null;
```

Python:

```text
s = None
```

C++:

```text
string &p = *static_cast<string *>(nullptr);
```

#### 空串

Java:

```text
String s = "";
```

Python:

```text
s = ""
s = str() # 等价于 s= ''
```

C++:

```text
string s;
```

这个声明中，s不是空对象，是指向实实在在的堆内存的。只是这段内存中没有数据而已，s此时是个空串。  
我们可以对s做所有字符串的操作。例如取长度、拼接、替换、查找字符等。

同时这里我总结了10个常见的字符串函数，也需要大家了解和掌握

Java中  
String demo = "Hello,world!";  
1.int length = demo.length\(\); //获取字符串的长度  
2.boolean equals = demo.equals\("Hello,world"\); // 比较两个字符串相等  
3.boolean contains = demo.contains\("word"\); // 是否包含子串  
4.String replace = demo.replace\("Hello,", "Yeah@"\); // 将指定字符串\(或正则表达式\)替换，返回替换后的结果  
5.char little = demo.charAt\(5\); // 查找字符串中索引为5的字符（索引从0开始）  
6.String trim = demo.trim\(\); // 将字符串左右空格去除，返回去除空格后的结果  
7.String concat = demo.concat\("Great!"\); // 拼接字符串，返回拼接结果  
8.char\[\] charArray = demo.toCharArray\(\); // 返回该字符串组成的字符数组  
9.String upperCase = demo.toUpperCase\(\); // 返回该字符串的大写形式  
10.String lowerCase = demo.toLowerCase\(\); // 返回该字符串的小写形式

Python中  
s = "Hello,World"  
1.print\(s\[1\]\) \# 'e', 取出某个位置的字符  
2.print\(s\[1:6\]\) \# 'ello,' ，字符串切片  
3.print\(len\(s\)\) \# 11, 返回字符串的长度  
4.print\("e" in s\) \# True, 返回字符是否在字符串中  
5.print\(s.lower\(\)\) \# 'hello,world', 将字符串所有元素变为小写  
6.print\(s.upper\(\)\) \# 'HELLO,WORLD', 将字符串所有元素变为大写  
7.s += '...' \# Hello,World... ，字符串拼接，在字符串后拼接另一个字符串  
8.print\(s.find\('lo'\)\) \# 3, 返回第一次找到指定字符串的起始位置（从左往右找）  
9.print\(s.swapcase\(\)\) \# hELLO,wORLD..., 将大小写互换  
10.print\(s.split\(','\)\) \# \['Hello', 'World...'\], 将字符串根据目标字符分割

