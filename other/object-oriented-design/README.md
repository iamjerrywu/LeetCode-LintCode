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

A class should always be flexible to extencion, but close to modification

