# Adapter

> Itent: Concerned with maintaining flexible and efficient structure

<p align="center"><img src="assets/Captura de tela de 2022-09-28 16-05-48.png"></p>

## When to use Adaptre Pattern?

- Use when we have a class whose interface is not compatible with the rest of the code
- Use when we want to reuse many subclasses with common functionality, which cannot be added to the superclass
- Use when you need to use multiple subclasses existing, however it is impractical to create an interface for each subclass

## Purpose

- Gives a unified interface that allows objects with incompatible interfaces to collaborate
- Converts an object's interface so that another object can understand it

## How does the Adapter Pattern Work?

1. The adapter gains an interface compatible with one of the objects
2. Using interface, object can safely call method inside adapter
3. When called, passes the request to the second object in a way that it will understand

## UML Diagram (Composition)

![uml-comp.png](assets/uml-comp.png)

## UML Diagram (Inheritance)

![uml-inh.png](assets/uml-inh.png)

## Classes

- *Target*
  - Defines the domain-specific interface that *Client* uses
- *Client*
  - Collaborates with objects compatible with the Target interface
- *Adaptee*
  - Defines an existing interface that needs to be adapted
- *Adpter*
  - Adapts the *Adaptee*'s interface to the *Target*'s interface
  
## How to implement the Adapter Pattern?

1. Make sure that you have at least two classes with incompatible interfaces:
    - A useful service class, which you can’t change (often 3rd-party, legacy or with lots of existing dependencies).
    - One or several client classes that would benefit from using the service class.

2. Declare the client interface and describe how clients communicate with the service.

3. Create the adapter class and make it follow the client interface. Leave all the methods empty for now.

4. Add a field to the adapter class to store a reference to the service object. The common practice is to initialize this field via the constructor, but sometimes it’s more convenient to pass it to the adapter when calling its methods.

5. One by one, implement all methods of the client interface in the adapter class. The adapter should delegate most of the real work to the service object, handling only the interface or data format conversion.

6. Clients should use the adapter via the client interface. This will let you change or extend the adapters without affecting the client code.

| Pros | Const |
|:-:|:-:|
|✅ Principle of Single Responsibility.|❌ Increased code complexity with the introduction of new interfaces.|
|✅ Possibility of multiple adapters without breaking the client interface.|
