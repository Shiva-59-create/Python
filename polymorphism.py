# # # # # #polymorphism.py->one name many forms
# # # # # #polymorphism in python is the ability to use a common interface for multiple forms (data types). 
# # # # # # It allows us to define methods in the child class with the same name as defined in their parent class. 
# # # # # # This is useful when we want to perform the same action in different ways depending on the object that is calling the method.
# # # # # #example
# # # # # class Dog:
# # # # #     def speaks(self):
# # # # #         print("Dog barks")
# # # # # class Cat:
# # # # #     def speaks(self):
# # # # #         print("Cat meows")
# # # # # d = Dog()
# # # # # c = Cat()
# # # # # d.speaks()  # Output: Dog barks
# # # # # # c.speaks()  # Output: Cat meows


# # # # # #types of polymorphism
# # # # # 1.method overloading: Method overloading is a feature that allows a class to have more than one method with the same name, but with different parameters. In Python, method overloading is not directly supported, but we can achieve it by using default arguments or variable-length arguments.
# # # # # 2.method overriding: Method overriding is a feature that allows a subclass to provide a specific implementation of
# # # # #     a method that is already defined in its superclass. When a method in a subclass has the same name, return type, and parameters as a method in its superclass, the subclass's method overrides the superclass's method. This allows for dynamic polymorphism, where the method that gets executed is determined at runtime based on the object's actual type.
# # # # # 3. operator overloading: Operator overloading is a feature that allows us to define the behavior of operators (like +, -, *, etc.) for user-defined classes. By implementing special methods (also known as magic methods or dunder methods) in our class, we can specify how operators should behave when applied to instances of that class. This enables us to use operators in a way that is intuitive and meaningful for our custom objects.
# # # # class animal:
# # # #     def speak(self):
# # # #         print("Animal speaks")
# # # # class dog(animal):
# # # #     def speak(self):
# # # #         print("Dog barks")
# # # # class cat(animal):
# # # #     def speak(self):
# # # #         print("Cat meows")
# # # # d = dog()
# # # # c = cat()   
# # # # d.speak()  # Output: Dog barks
# # # # c.speak()  # Output: Cat meows


# # # #method overloading
# # # #mulytiple methods with the same name but different parameters
# # # class calculator:
# # #     def add (self,a,b):
# # #         return a+b
# # #     def add (self,a,b,c):
# # #         return a+b+c
# # # calc = calculator()
# # # # print(calc.add(2,3))  # This will raise an error because the second
# # # calc.add(2,3,4)  # This will work and return 9
# # # calculator.add = lambda self, a, b, c=0: a + b + c  # Using default argument to handle both cases
# # # print(calc.add(2, 3))      # Output: 5

# # #operator polymorphism
# # #operator overloading is a feature that allows us to define the behavior of operators (like +, -, *, etc.) for user-defined classes. By implementing special methods (also known as magic methods or dunder methods) in our class, 
# # # we can specify how operators should behave when applied to instances of that class.
# # #  This enables us to use operator[l\ s in a way that is intuitive and meaningful for our custom objects.
# # # print(10 + 20)
# # # print("Hello" + "World")

# # class Point:
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y
# #     def __add__(self,other):
# #         return Point(self.x + other.x, self.y + other.y)
# # point1 = Point(10,20)
# # point2 = Point(30,40)
# # point3 = point1 + point2
# # print(point3.x, point3.y) 


# #abstraction
# from abc import ABC, abstractmethod
# #ABC CALLED ABSTRACT BASE CLASS
# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# #@abstractmethod decorator is used to declare a method as abstract.
# #  An abstract method is a method that is declared in the abstract base class 
# # but does not have an implementation in that class.
# class dog(animal):
#     def sound(self):
#         print("Dog barks")
# class cat(animal):
#     def sound(self):
#         print("Cat meows")
# d = dog()
# c = cat()
# d.sound()  # Output: Dog barks
# c.sound()  # Output: Cat meows
