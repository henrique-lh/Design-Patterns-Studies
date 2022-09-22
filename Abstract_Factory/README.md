# Abstract Factory

> Intent: It's a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

![Analogy photo](/assets/im-1.png)

## When to use Abstract Facotry Pattern?

* A system must be independent of how it's are created, composed or represented;
* A system must be configured as product of a multi-product family;
* A family of product-objects is designed to be used, and you need to enforce this constraint;
* Only show the interface, not the implementation;

## UML Diagram

![Abstract Factory Diagram](/assets/diagram-1.png "UML Diagram 1")

## Classes

* *AbstractFactory*
  * Declare an interface for operations that create abstract product-objects
* *Concrete Factory*
  * Implement operations that create concrete product-objects
* *AbstractProduct*
  * Declare an interface for a product-object type
* *ConcreteProduct*
  * Defines a product-objetc to be created by the corresponding concrete factory
  * Implements *Abstract Product* interface
* *Client*
  * Uses only interfaces declared by the *Abstract Factory* and *Abstract Product* classes

| Pros | Const |
|:-:|:-:|
|✅ You can be sure that the products you’re getting from a factory are compatible with each other.|❌ The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.|
|✅ You avoid tight coupling between concrete products and client code.|
|✅ Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.|
|✅ Open/Closed Principle. You can introduce new variants of products without breaking existing client code.|

### Examples

* [Refactoring-guru](https://refactoring.guru/design-patterns/abstract-factory/python/example)
* [Python Design Patterns Guide](https://python-patterns.guide/gang-of-four/abstract-factory/)
