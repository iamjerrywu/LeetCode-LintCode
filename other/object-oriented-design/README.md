# Object-Oriented Design

## SOLID Principle

* S: Single Responsibility Principle
* O: Open close principle
* L: Liskov substitution principle
* I: Interface segregation principle
* D: Dependency inversion principle

### S: Single Responsibility Principle

A class should only have one reason to modify it, which means it should only have one speific task

#### Example

```java
public class AreaCalculator
{
    private float result;
    public float getResult()
    {
        return this.result;
    }
    
    public float calculator(Triangle t)
    {
        this.result = h * b / 2;
    } 
}

pulbic class Printer 
{
    public printInJson(float number)
    {
        jsonPrinter.initialize();
        jsonPrnter.print(this.result);
        jsonPrinter.close();
    }
}
        
```

### O: Open Close Principle

A class should always be flexible to extension, but close to modification

```java
// A bad example
pulic class AreaCalculator
{
    public float calculateArea(Triangle t)
    {
        // calculate area of triangle
    }
    
    public float calculateArea(Rectangle r)
    {
        // calculates the area for rectangle
    }
    // need to implmenet calculateArea when a new shape is added
    // not flexible for extension
```

Modified one

```java
public interface Shape
{
    public float getArea();
}

public class Triangle implements Shape
{
    public float getArea()
    {
        return b * h / 2;
    }
}

public class AreaCalculator
{
    private float result;
    
    public float getResult()
    {
        return this.result;
    }
    
    public float calculateArea(Shape s)
    {
        this.result = s.getArea();
    }
}
```

### Liskov substitution principle

```java
public class Shape
{
    abstract public float calculateVolumn();
    abstract public float calculateArea();
}

// this is invalid, since rectagle can never have volumn 
public class Rectangle extends Shape
{
    //...
}

// this is valid
public class Cube extends Shape
{
    //...
}
```

### Dependency Inversion Principle

1. Abstract class should not depend on physical class, and physical class should depend on abstract
2. High-Level class should not depend on low-level class

```java
public class AreaCalculator
{
    private float result;
    private Triangle t; // bad usage here, it depends on class definiton outside
    
    public float getResult()
    {
        return this.result;
    }
    
    public float calculateArea()
    {
        this.result = t.h * t.b / 2;
    }
}
```

```java
public interface Shape
{
    public float getArea();
}

public class Triangle implements Shape
{
    public float getArea()
    {
        return b * h / 2;
    }
}

public class AreaCalculator
{
    private float result;
    public float getResult()
    {
        return this.result;
    }
    
    public float calculateArea(Shape s)
    {
        this.result = s.getArea();
    }
```

## 5C Principle 

* Clarify: 
  * Clarify the question and its requirement, boundary and function
* Core objects:
  * What classes/objects are involved, and their relationships with others
* Cases:
  * The scenario and function for this problems
* Classes:
  * Make sure what class are required
* Correctness
  * Check the system you design, and make sure they fulfill the requirements

## Design Pattern 



