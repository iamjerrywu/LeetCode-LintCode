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

