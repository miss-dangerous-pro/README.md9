# README.md9
# Python OOPs Concepts: 
Object-Oriented Programming (OOP) in Python is  based on the concept of objects, which contain both data (attributes or properties) and code (methods or functions) to manipulate that data. 
It is a programming approach based an class and object in simpla language. OOP is the method to represent the real world entity in the programming.
* Class in Python
* Objects in Python
* Polymorphism in Python
* Encapsulation in Python
* Inheritance in Python
* Data Abstraction in Python
# Python3 Intermediate Level Topics:
variables, data types such as strings, integers, floats, lists, tuples, dictionaries, control structures such as if statements, loops, functions, modules, and file handling.
# Class, Object and Members:
In Python, classes and objects are the foundation of Object-Oriented Programming (OOP).
* Class
* A class is like a blueprint for creating objects. It defines the data and methods or functions   that the objects created from the class will have.
* Classes are created using the class keyword, followed by the class name.
* Classes can include an initializer method, called __init__, which is used to initialize the attributes of the class when an object is created.
* Object_
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
Each object has its own copy of the class’s attributes and methods.
Objects are created by calling the class as if it were a function.
* Members
Members of a class are its attributes (variables) and methods (functions). A member function is function which present inside the body of a class . It is same as normal function but it can only called by using an object rather a normal function can be called directly.
# Data Hiding and Object Printing:
* Data Hiding
Data hiding is a key concept in object-oriented programming, aimed at restricting access to certain attributes and methods of a class.
Data hiding, also called "data encapsulation," keeps the user from seeing how certain parts of a service work.
* Object Printing
Python print() function is used to print the specified object to the standard output device (screen) or to a text stream file. The Python print() method is used to print a given message to the screen or to display an object's value on the terminal.
# Inheritance, examples of object, issubclass and super
In Python, inheritance is a fundamental concept in object-oriented programming where a class (called a child or derived class) inherits attributes and behaviors (methods) from another class (called a parent or base class).
# issubclass
The issubclass() function in Python checks if a particular class is a subclass of another class or a tuple of classes. It returns True if the specified class is indeed a subclass, otherwise it returns False.
# super 
In Python, super() is used in inheritance to allow a child class to access methods and properties of its parent class. 
# Polymorphism in Python
Polymorphism in Python allows methods or functions to process objects differently based on their data types or classes.
# Class and static variable in python
* Class Variable: Typically associated with instances of the class and can be accessed or modified through any instance or the class itself.
* Static Variable: Often used as constants within static methods, not tied to any instance of the class. Generally, it’s accessed directly through the class name.
# Class method and static method in python
* class method 
1) A class method is a method that is bound to the class rather than the instance of the class.
2) It takes cls as the first parameter instead of self. cls refers to the class itself, allowing the method to access and modify class state that applies across all instances.
3) Class methods are defined using the @classmethod decorator.
* static method 
1) A static method is a method that belongs to the class, but it does not have access to the instance (self) or class (cls) attributes.
2) Static methods are defined using the @staticmethod decorator.
