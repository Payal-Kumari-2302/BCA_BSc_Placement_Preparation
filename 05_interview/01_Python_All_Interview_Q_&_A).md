<div align="center">

# 🐍 Python Technical Interview Preparation

### Complete Python Concepts with Definitions & Real-World Examples

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)
![Questions](https://img.shields.io/badge/Questions-118-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Basic%20to%20Advanced-orange?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-IT%20Placements-red?style=for-the-badge)

**Target Companies:** TCS, Wipro, Infosys, Accenture, Cognizant, Deloitte, Genpact & Other IT Companies.

**Target Audience:** BCA Students | Freshers | Entry-Level IT Professionals

</div>

---

# 📚 PART 01 – Python Fundamentals (15 Questions)

### 1. What is Python?
**Definition:** Python is a high-level, interpreted, general-purpose programming language known for its simple syntax and readability.

**Example:**
```python
print("Hello, World!")
```
**Real-World Example:** Python is used in web development, automation, data analysis and AI applications.

### 2. What are the main features of Python?
**Definition:** Python is simple, interpreted, dynamically typed, portable, open-source and supports object-oriented programming.

**Example:**
```python
name = "Payal"
print(name)
```
**Real-World Example:** Developers use Python to build applications quickly with less code.

### 3. Why is Python called an interpreted language?
**Definition:** Python code is executed by the Python interpreter. In CPython, source code is first compiled into bytecode and then executed by the Python virtual machine.

**Example:**
```python
print(10 + 20)
```
**Real-World Example:** Developers can run Python scripts directly using the Python interpreter.

### 4. Is Python dynamically typed or statically typed?
**Definition:** Python is dynamically typed because variable types are determined at runtime.

**Example:**
```python
x = 10
x = "Python"
```
**Real-World Example:** Developers can reuse variables with different data types without declaring their types explicitly.

### 5. What are the advantages and disadvantages of Python?
**Definition:** Python is easy to learn, readable and has many libraries, but it can be slower than compiled languages and may use more memory.

**Example:**
```python
print(sum([10, 20, 30]))
```
**Real-World Example:** Python is useful for automation and data analysis, but performance-critical systems may use C or C++.

### 6. What is the difference between Python 2 and Python 3?
**Definition:** Python 3 is the modern version with improved syntax, Unicode support and updated features. Python 2 is discontinued.

**Example:**
```python
print("Hello Python 3")
```
**Real-World Example:** Modern IT projects generally use Python 3 for development and maintenance.

### 7. What are keywords in Python?
**Definition:** Keywords are reserved words that have special meanings in Python and cannot be used as ordinary identifiers.

**Example:**
```python
if True:
    print("Python")
```
**Real-World Example:** Keywords such as `if`, `else`, `for` and `while` control program execution.

### 8. What are identifiers in Python?
**Definition:** Identifiers are names used to identify variables, functions, classes and other objects.

**Example:**
```python
student_name = "Payal"
```
**Real-World Example:** Developers use identifiers to name employee records, functions and database-related variables.

### 9. What are variables in Python?
**Definition:** Variables are names that refer to objects and their values in a program.

**Example:**
```python
name = "Payal"
age = 22
```
**Real-World Example:** An application uses variables to store usernames, prices and customer details.

### 10. What are the rules for naming variables?
**Definition:** Variable names must start with a letter or underscore, cannot start with a number and cannot contain spaces or reserved keywords.

**Example:**
```python
student_name = "Payal"
_age = 22
```
**Real-World Example:** Meaningful variable names make software easier to understand and maintain.

### 11. What are comments in Python?
**Definition:** Comments are non-executable statements used to explain code.

**Example:**
```python
# Calculate total marks
marks = 450
```
**Real-World Example:** Developers use comments to explain complex business logic to team members.

### 12. What is indentation in Python?
**Definition:** Indentation means spaces at the beginning of a code line to define a block of code.

**Example:**
```python
if 10 > 5:
    print("Greater")
```
**Real-World Example:** Indentation helps organize conditions, loops and functions.

### 13. Why is indentation important in Python?
**Definition:** Python uses indentation to identify code blocks instead of curly braces.

**Example:**
```python
if True:
    print("Correct")
```
**Real-World Example:** Proper indentation prevents indentation errors and improves code readability.

### 14. What is the difference between a compiler and an interpreter?
**Definition:** A compiler translates source code into another form before execution, while an interpreter executes instructions through a runtime environment.

**Example:** C commonly uses compilation, while Python uses an interpreter-based execution model.

**Real-World Example:** Developers use compiled languages for many performance-critical applications and Python for rapid development.

### 15. What is PEP 8?
**Definition:** PEP 8 is the official Python style guide that provides coding conventions for writing readable Python code.

**Example:**
```python
student_name = "Payal"
total_marks = 450
```
**Real-World Example:** Development teams follow PEP 8 to maintain consistent coding standards.

---

# 📚 PART 02 – Data Types and Variables (10 Questions)

### 16. What are data types in Python?
**Definition:** Data types define the type of value an object represents.

**Example:**
```python
age = 22
name = "Payal"
price = 99.5
```
**Real-World Example:** Applications use integers for age, strings for names and floats for prices.

### 17. What are the built-in data types in Python?
**Definition:** Python provides built-in data types such as int, float, complex, str, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray and NoneType.

**Example:**
```python
age = 22
name = "Payal"
marks = [80, 90, 95]
```
**Real-World Example:** Different data types help applications store different kinds of information.

### 18. What is the difference between mutable and immutable data types?
**Definition:** Mutable objects can be changed after creation, while immutable objects cannot be changed after creation.

**Example:**
```python
my_list = [10, 20]
my_list.append(30)

name = "Python"
```
**Real-World Example:** Lists are useful for updating shopping cart items, while strings represent immutable text values.

### 19. What is type casting?
**Definition:** Type casting means converting one data type into another.

**Example:**
```python
age = "22"
age = int(age)
```
**Real-World Example:** Converting user input into an integer before performing calculations.

### 20. What is the difference between implicit and explicit type conversion?
**Definition:** Implicit conversion happens automatically, while explicit conversion is performed manually by the programmer.

**Example:**
```python
# Implicit
a = 10
b = 2.5
c = a + b

# Explicit
x = int("100")
```
**Real-World Example:** Converting user-entered text into numeric values for billing calculations.

### 21. What is the difference between int, float and complex?
**Definition:** int stores whole numbers, float stores decimal numbers and complex stores numbers with real and imaginary parts.

**Example:**
```python
a = 10
b = 10.5
c = 3 + 4j
```
**Real-World Example:** Integers represent quantities, floats represent prices and complex numbers are useful in scientific calculations.

### 22. What is the difference between list, tuple and set?
**Definition:** A list is ordered and mutable, a tuple is ordered and immutable, and a set stores unique elements without guaranteed positional order.

**Example:**
```python
my_list = [10, 20, 10]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
```
**Real-World Example:** Lists store cart items, tuples store fixed coordinates and sets remove duplicate records.

### 23. What is a dictionary in Python?
**Definition:** A dictionary is a mutable collection that stores data in key-value pairs.

**Example:**
```python
student = {
    "name": "Payal",
    "age": 22
}
```
**Real-World Example:** Dictionaries store employee details, user profiles and configuration settings.

### 24. What is the difference between None, 0 and False?
**Definition:** None represents the absence of a value, 0 is an integer and False is a Boolean value.

**Example:**
```python
a = None
b = 0
c = False
```
**Real-World Example:** None can represent missing information, 0 can represent a zero balance and False can represent an inactive account.

### 25. What is dynamic typing?
**Definition:** Dynamic typing allows a variable name to refer to objects of different types during program execution.

**Example:**
```python
x = 100
x = "Hello"
```
**Real-World Example:** Developers can assign different types of values to the same variable when processing different inputs.

---

# 📚 PART 03 – Operators and Control Flow (11 Questions)

### 26. What are operators in Python?
**Definition:** Operators are symbols or keywords used to perform operations on values and variables.

**Example:**
```python
a = 10
b = 5
print(a + b)
```
**Real-World Example:** Operators calculate product prices, discounts and employee salaries.

### 27. Explain arithmetic operators.
**Definition:** Arithmetic operators perform mathematical operations such as addition, subtraction, multiplication, division, modulus, floor division and exponentiation.

**Example:**
```python
a = 10
b = 3
print(a + b)
print(a % b)
```
**Real-World Example:** Calculating bills, taxes and discounts in business applications.

### 28. What is the difference between / and //?
**Definition:** `/` performs division and returns a floating-point result, while `//` performs floor division.

**Example:**
```python
print(10 / 3)
print(10 // 3)
```
**Real-World Example:** Floor division can calculate the number of complete groups or packages.

### 29. What is the difference between == and is?
**Definition:** `==` compares values, while `is` checks whether two references point to the same object.

**Example:**
```python
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)
```
**Real-World Example:** Developers use `is None` to check whether a value is missing.

### 30. What are logical operators?
**Definition:** Logical operators combine or reverse Boolean conditions using and, or and not.

**Example:**
```python
age = 22
print(age >= 18 and age <= 60)
```
**Real-World Example:** Checking login conditions and user permissions.

### 31. What are membership operators?
**Definition:** Membership operators `in` and `not in` check whether a value exists in a sequence or collection.

**Example:**
```python
names = ["Payal", "Riya"]
print("Payal" in names)
```
**Real-World Example:** Checking whether a username exists in a user list.

### 32. What are identity operators?
**Definition:** Identity operators `is` and `is not` check whether two references point to the same object.

**Example:**
```python
a = None
print(a is None)
```
**Real-World Example:** Checking whether a database result or function output is None.

### 33. What is the difference between break, continue and pass?
**Definition:** `break` terminates a loop, `continue` skips the current iteration and `pass` performs no operation.

**Example:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
**Real-World Example:** Break can stop searching after finding a record, while continue can skip invalid records.

### 34. What is the difference between if, elif and else?
**Definition:** These statements are used for conditional decision-making. `if` checks the first condition, `elif` checks additional conditions and `else` runs when none is true.

**Example:**
```python
marks = 80

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```
**Real-World Example:** Assigning grades based on student marks.

### 35. What is a nested loop?
**Definition:** A nested loop is a loop placed inside another loop.

**Example:**
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```
**Real-World Example:** Processing rows and columns in a table or matrix.

### 36. What is the difference between for and while loops?
**Definition:** A for loop iterates over a sequence, while a while loop repeats as long as a condition is true.

**Example:**
```python
for i in range(3):
    print(i)

x = 0
while x < 3:
    print(x)
    x += 1
```
**Real-World Example:** For loops process employee records, while loops can repeatedly ask for valid login input.

---

# 📚 PART 04 – Strings (9 Questions)

### 37. What is a string in Python?
**Definition:** A string is an immutable sequence of Unicode characters enclosed in quotes.

**Example:**
```python
name = "Python"
```
**Real-World Example:** Storing names, addresses, email IDs and messages.

### 38. Are strings mutable or immutable?
**Definition:** Strings are immutable, meaning their characters cannot be changed directly after creation.

**Example:**
```python
name = "Python"
name = "Java"
```
**Real-World Example:** Usernames and messages are stored as string values; modifications create new string objects.

### 39. What is string slicing?
**Definition:** String slicing extracts a portion of a string using start, stop and step indexes.

**Example:**
```python
text = "Python"
print(text[0:3])
```
**Real-World Example:** Extracting country codes or specific parts of an email address.

### 40. What is negative indexing?
**Definition:** Negative indexing accesses elements from the end of a sequence.

**Example:**
```python
text = "Python"
print(text[-1])
```
**Real-World Example:** Accessing the last character of a filename or text.

### 41. What is the difference between find() and index()?
**Definition:** Both methods search for a substring. `find()` returns -1 if it is not found, while `index()` raises a ValueError.

**Example:**
```python
text = "Python"
print(text.find("z"))
```
**Real-World Example:** Searching for keywords in user messages without necessarily raising an exception.

### 42. What is the difference between split() and join()?
**Definition:** `split()` converts a string into a list, while `join()` combines strings from an iterable into one string.

**Example:**
```python
text = "Python Java C"
print(text.split())

words = ["Python", "Java"]
print(" ".join(words))
```
**Real-World Example:** Splitting CSV-like text into fields and joining names into a formatted message.

### 43. What is the difference between strip(), lstrip() and rstrip()?
**Definition:** `strip()` removes whitespace from both ends, `lstrip()` from the left and `rstrip()` from the right.

**Example:**
```python
text = "  Python  "
print(text.strip())
```
**Real-World Example:** Cleaning extra spaces from user input before storing it in a database.

### 44. What are f-strings?
**Definition:** F-strings are formatted string literals that allow expressions and variables inside strings using curly braces.

**Example:**
```python
name = "Payal"
print(f"Hello {name}")
```
**Real-World Example:** Generating personalized messages and formatted reports.

### 45. How can you reverse a string in Python?
**Definition:** A string can be reversed using slicing with a step of -1.

**Example:**
```python
text = "Python"
print(text[::-1])
```
**Real-World Example:** Reversing text for palindrome checking and string-processing tasks.

---

# 📚 PART 05 – Lists, Tuples, Sets and Dictionaries (15 Questions)

### 46. What is a list?
**Definition:** A list is an ordered, mutable collection that allows duplicate elements.

**Example:**
```python
fruits = ["Apple", "Mango", "Banana"]
```
**Real-World Example:** Storing shopping cart items and student marks.

### 47. What is the difference between append() and extend()?
**Definition:** `append()` adds one element to a list, while `extend()` adds elements from an iterable.

**Example:**
```python
a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])
```
**Real-World Example:** Adding one product or multiple products to a shopping cart.

### 48. What is the difference between remove(), pop() and del?
**Definition:** `remove()` deletes a specified value, `pop()` removes an element by index and returns it, while `del` deletes an element or slice.

**Example:**
```python
numbers = [10, 20, 30]
numbers.remove(20)
numbers.pop()
del numbers[0]
```
**Real-World Example:** Removing products from a cart or deleting unwanted records.

### 49. What is list comprehension?
**Definition:** List comprehension is a short way to create a new list using an expression and an iterable.

**Example:**
```python
squares = [x*x for x in range(5)]
```
**Real-World Example:** Creating a list of filtered employee salaries.

### 50. What is a nested list?
**Definition:** A nested list is a list that contains other lists as elements.

**Example:**
```python
matrix = [[1, 2], [3, 4]]
```
**Real-World Example:** Representing rows and columns in spreadsheets and matrices.

### 51. What is a tuple?
**Definition:** A tuple is an ordered and immutable collection that allows duplicate elements.

**Example:**
```python
coordinates = (10, 20)
```
**Real-World Example:** Storing fixed coordinates or database records.

### 52. Why are tuples immutable?
**Definition:** Tuples are designed to prevent changes to their element references after creation.

**Example:**
```python
data = (10, 20, 30)
```
**Real-World Example:** Storing fixed configuration values that should not be modified accidentally.

### 53. What is tuple packing and unpacking?
**Definition:** Packing combines multiple values into a tuple, while unpacking assigns tuple elements to separate variables.

**Example:**
```python
data = 10, 20, 30
a, b, c = data
```
**Real-World Example:** Returning multiple values from a function.

### 54. What is a set?
**Definition:** A set is an unordered collection of unique elements.

**Example:**
```python
numbers = {10, 20, 10, 30}
```
**Real-World Example:** Maintaining a unique list of registered email addresses.

### 55. Why does a set not allow duplicate elements?
**Definition:** A set stores unique elements and automatically removes duplicates based on equality and hashing.

**Example:**
```python
numbers = {1, 2, 2, 3}
print(numbers)
```
**Real-World Example:** Removing duplicate customer IDs from a dataset.

### 56. What are union, intersection and difference in sets?
**Definition:** Union combines elements, intersection returns common elements and difference returns elements present in one set but not the other.

**Example:**
```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)
print(a & b)
print(a - b)
```
**Real-World Example:** Comparing registered users across two platforms.

### 57. What is a dictionary?
**Definition:** A dictionary is a mutable collection that stores unique keys with corresponding values.

**Example:**
```python
student = {"name": "Payal", "age": 22}
```
**Real-World Example:** Storing customer profiles and employee information.

### 58. What is the difference between keys(), values() and items()?
**Definition:** `keys()` returns dictionary keys, `values()` returns values and `items()` returns key-value pairs.

**Example:**
```python
student = {"name": "Payal", "age": 22}

print(student.keys())
print(student.values())
print(student.items())
```
**Real-World Example:** Extracting employee names, salaries or complete employee records.

### 59. What is the difference between get() and direct key access?
**Definition:** `get()` returns None or a default value if the key is missing, while direct access using square brackets raises KeyError.

**Example:**
```python
data = {"name": "Payal"}
print(data.get("age"))
```
**Real-World Example:** Safely retrieving optional customer information.

### 60. Can a dictionary contain duplicate keys?
**Definition:** No. Dictionary keys must be unique. Assigning a value to an existing key replaces its previous value.

**Example:**
```python
data = {"name": "Payal", "name": "Riya"}
print(data)
```
**Real-World Example:** Updating an existing employee record using their unique employee ID.

---

# 📚 PART 06 – Functions (14 Questions)

### 61. What is a function in Python?
**Definition:** A function is a reusable block of code designed to perform a specific task.

**Example:**
```python
def greet():
    print("Hello")
```
**Real-World Example:** A login function can be reused across different application screens.

### 62. What are the advantages of using functions?
**Definition:** Functions improve code reusability, readability, organization and maintainability.

**Example:**
```python
def add(a, b):
    return a + b
```
**Real-World Example:** A payment calculation function can be reused in multiple parts of an application.

### 63. What is the difference between built-in and user-defined functions?
**Definition:** Built-in functions are provided by Python, while user-defined functions are created by programmers.

**Example:**
```python
print(len("Python"))

def greet():
    print("Hello")
```
**Real-World Example:** Using built-in functions for calculations and custom functions for business logic.

### 64. What are parameters and arguments?
**Definition:** Parameters are variables defined in a function, while arguments are actual values passed when calling it.

**Example:**
```python
def greet(name):
    print(name)

greet("Payal")
```
**Real-World Example:** Passing customer details to a registration function.

### 65. What is the difference between return and print()?
**Definition:** `return` sends a value back from a function, while `print()` displays information on the screen.

**Example:**
```python
def add(a, b):
    return a + b
```
**Real-World Example:** Returning a calculated bill amount to another function.

### 66. What are default arguments?
**Definition:** Default arguments are parameters that have predefined values used when no argument is provided.

**Example:**
```python
def greet(name="Guest"):
    print(name)
```
**Real-World Example:** Providing a default language or country setting in an application.

### 67. What are keyword arguments?
**Definition:** Keyword arguments pass values using parameter names.

**Example:**
```python
def student(name, age):
    print(name, age)

student(age=22, name="Payal")
```
**Real-World Example:** Passing named configuration options to functions.

### 68. What are positional arguments?
**Definition:** Positional arguments are values assigned to parameters according to their position in a function call.

**Example:**
```python
def add(a, b):
    return a + b

add(10, 20)
```
**Real-World Example:** Passing product quantity and price to a billing function.

### 69. What are *args and **kwargs?
**Definition:** `*args` collects extra positional arguments into a tuple, while `**kwargs` collects extra keyword arguments into a dictionary.

**Example:**
```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
```
**Real-World Example:** Creating flexible functions that accept different numbers of user details or settings.

### 70. What is recursion?
**Definition:** Recursion is a programming technique in which a function calls itself until a base condition is reached.

**Example:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
**Real-World Example:** Traversing hierarchical folders and tree structures.

### 71. What is a lambda function?
**Definition:** A lambda function is a small anonymous function written using the lambda keyword.

**Example:**
```python
square = lambda x: x * x
print(square(5))
```
**Real-World Example:** Sorting records using a short custom expression.

### 72. What is the difference between local and global variables?
**Definition:** Local variables are defined inside a function, while global variables are defined outside functions.

**Example:**
```python
x = 10

def demo():
    y = 20
```
**Real-World Example:** Local variables store temporary calculations, while global constants may store application-wide settings.

### 73. What is the global keyword?
**Definition:** The global keyword allows a function to reassign a variable defined in the global scope.

**Example:**
```python
x = 10

def update():
    global x
    x = 20
```
**Real-World Example:** Updating a shared application-level counter.

### 74. What is the nonlocal keyword?
**Definition:** The nonlocal keyword allows a nested function to modify a variable in its nearest enclosing function scope.

**Example:**
```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
```
**Real-World Example:** Maintaining shared state between nested functions.

---

# 📚 PART 07 – Object-Oriented Programming (18 Questions)

### 75. What is Object-Oriented Programming?
**Definition:** OOP is a programming approach that organizes code using classes and objects.

**Example:**
```python
class Student:
    pass
```
**Real-World Example:** Developing banking, employee management and student management systems.

### 76. What is a class in Python?
**Definition:** A class is a blueprint used to create objects containing attributes and methods.

**Example:**
```python
class Student:
    name = "Payal"
```
**Real-World Example:** An Employee class defines common properties of employees.

### 77. What is an object?
**Definition:** An object is an instance of a class that contains data and behavior.

**Example:**
```python
class Student:
    pass

s1 = Student()
```
**Real-World Example:** Individual employee records created from an Employee class.

### 78. What is the difference between a class and an object?
**Definition:** A class is a blueprint, while an object is an actual instance created from that blueprint.

**Example:**
```python
class Car:
    pass

car1 = Car()
```
**Real-World Example:** Car is a class, while a particular Honda car is an object.

### 79. What is a constructor?
**Definition:** A constructor is a mechanism used to initialize an object when it is created. In Python, `__init__()` commonly performs initialization.

**Example:**
```python
class Student:
    def __init__(self, name):
        self.name = name
```
**Real-World Example:** Initializing employee names and IDs when creating employee objects.

### 80. What is the __init__() method?
**Definition:** `__init__()` is an initializer method automatically called after an object is created.

**Example:**
```python
class Student:
    def __init__(self):
        self.name = "Payal"
```
**Real-World Example:** Setting default values for new customer objects.

### 81. What is the self keyword?
**Definition:** `self` refers to the current instance of a class and is used to access its attributes and methods.

**Example:**
```python
class Student:
    def show(self):
        print("Hello")
```
**Real-World Example:** Accessing the details of a particular employee object.

### 82. What are the four pillars of OOPs?
**Definition:** The four pillars are inheritance, polymorphism, encapsulation and abstraction.

**Example:** A banking application can use all four concepts to manage accounts securely.

**Real-World Example:** Building reusable and maintainable enterprise applications.

### 83. What is inheritance?
**Definition:** Inheritance allows one class to acquire attributes and methods from another class.

**Example:**
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
```
**Real-World Example:** Different employee types can inherit common employee details from a base class.

### 84. What are the different types of inheritance?
**Definition:** Python supports single, multiple, multilevel, hierarchical and hybrid inheritance.

**Example:** A child class can inherit from one or multiple parent classes.

**Real-World Example:** Designing application classes with shared functionality.

### 85. What is multiple inheritance?
**Definition:** Multiple inheritance allows a class to inherit from more than one parent class.

**Example:**
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```
**Real-World Example:** Combining features from multiple reusable classes.

### 86. What is polymorphism?
**Definition:** Polymorphism means one interface or method name can represent different behaviors depending on the object.

**Example:**
```python
print(len("Python"))
print(len([10, 20, 30]))
```
**Real-World Example:** Different payment methods can implement the same `pay()` operation differently.

### 87. What is method overriding?
**Definition:** Method overriding occurs when a child class provides its own implementation of a method inherited from its parent class.

**Example:**
```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```
**Real-World Example:** Different employee types can implement their own salary calculation methods.

### 88. What is method overloading?
**Definition:** Method overloading means using the same method name with different parameter lists. Python does not support traditional compile-time method overloading directly, but similar behavior can be achieved using default arguments or variable-length arguments.

**Example:**
```python
def add(a, b=0):
    return a + b
```
**Real-World Example:** Designing flexible functions that accept different numbers of inputs.

### 89. What is encapsulation?
**Definition:** Encapsulation combines data and methods inside a class and controls access to internal details.

**Example:**
```python
class Account:
    def __init__(self):
        self.__balance = 1000
```
**Real-World Example:** Protecting account-related data from unintended direct modification.

### 90. What is abstraction?
**Definition:** Abstraction hides implementation details and exposes only essential functionality.

**Example:**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
```
**Real-World Example:** A user drives a car without needing to understand its internal engine mechanism.

### 91. What is the difference between instance, class and static methods?
**Definition:** Instance methods work with object data, class methods work with class-level data and static methods are utility methods that do not automatically receive an instance or class reference.

**Example:**
```python
class Demo:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```
**Real-World Example:** Employee-specific operations, class-level counters and general utility calculations.

### 92. What is the difference between super() and self?
**Definition:** `self` refers to the current object, while `super()` provides access to methods in the next class in the method resolution order.

**Example:**
```python
class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        super().show()
```
**Real-World Example:** Reusing parent-class initialization and functionality in child classes.

---

# 📚 PART 08 – Exception Handling (8 Questions)

### 93. What is an exception?
**Definition:** An exception is an event that interrupts the normal flow of a program during execution.

**Example:**
```python
print(10 / 0)
```
**Real-World Example:** A program may encounter an exception when a user enters invalid data.

### 94. What is exception handling?
**Definition:** Exception handling is a mechanism used to detect and handle runtime errors without unexpectedly terminating the program.

**Example:**
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```
**Real-World Example:** Handling failed database connections or invalid user input.

### 95. What is the difference between an error and an exception?
**Definition:** Errors are problems in a program, while exceptions are runtime events that can often be handled using exception-handling mechanisms.

**Example:** SyntaxError occurs due to invalid syntax, while ZeroDivisionError occurs during execution.

**Real-World Example:** Developers fix syntax errors and handle expected runtime exceptions.

### 96. What is the use of try and except?
**Definition:** `try` contains code that may raise an exception, while `except` handles the specified exception.

**Example:**
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
```
**Real-World Example:** Validating user input in registration forms.

### 97. What is the purpose of finally?
**Definition:** The finally block executes whether an exception occurs or not, and is commonly used for cleanup operations.

**Example:**
```python
try:
    print("Processing")
finally:
    print("Completed")
```
**Real-World Example:** Closing resources or releasing connections after database operations.

### 98. What is the use of else in exception handling?
**Definition:** The else block executes when no exception occurs in the try block.

**Example:**
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(x)
```
**Real-World Example:** Processing a payment only when the validation operation succeeds.

### 99. What is the raise keyword?
**Definition:** The raise keyword is used to manually trigger an exception.

**Example:**
```python
age = 15

if age < 18:
    raise ValueError("Not eligible")
```
**Real-World Example:** Rejecting invalid ages or incorrect transaction amounts.

### 100. How can you create a custom exception?
**Definition:** A custom exception is created by defining a class that inherits from the Exception class.

**Example:**
```python
class InvalidAgeError(Exception):
    pass
```
**Real-World Example:** Creating application-specific exceptions for invalid employee IDs or payment failures.

---

# 📚 PART 09 – Advanced Python (18 Questions)

### 101. What is an iterator?
**Definition:** An iterator is an object that returns elements one at a time using `__next__()`.

**Example:**
```python
numbers = iter([10, 20, 30])
print(next(numbers))
```
**Real-World Example:** Processing large datasets one record at a time.

### 102. What is an iterable?
**Definition:** An iterable is an object that can return an iterator using `iter()`.

**Example:**
```python
numbers = [10, 20, 30]

for n in numbers:
    print(n)
```
**Real-World Example:** Iterating over lists of employees or customer records.

### 103. What is a generator?
**Definition:** A generator is a special iterator that produces values one at a time, usually using the yield keyword.

**Example:**
```python
def numbers():
    yield 1
    yield 2
    yield 3
```
**Real-World Example:** Reading large files without loading all data into memory at once.

### 104. What is the difference between yield and return?
**Definition:** `return` ends a function and sends back a value, while `yield` produces a value and suspends the function's execution.

**Example:**
```python
def demo():
    yield 10
    yield 20
```
**Real-World Example:** Generating records gradually from a large database query.

### 105. What is a decorator?
**Definition:** A decorator is a function that modifies or extends another function's behavior without changing its original code.

**Example:**
```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
    return wrapper
```
**Real-World Example:** Logging, authentication and performance monitoring.

### 106. What is a module in Python?
**Definition:** A module is a Python file containing reusable code such as functions, variables and classes.

**Example:**
```python
import math
print(math.sqrt(25))
```
**Real-World Example:** Using separate Python files to organize application functionality.

### 107. What is a package in Python?
**Definition:** A package is a way to organize related Python modules into a directory hierarchy.

**Example:**
```python
import os
```
**Real-World Example:** Organizing large applications into authentication, database and payment modules.

### 108. What is the difference between a module and a package?
**Definition:** A module is generally a single Python file, while a package organizes multiple modules into a directory structure.

**Example:** `math` is a module, while `email` is an example of a standard-library package.

**Real-World Example:** Separating application code into organized modules and packages.

### 109. What is the purpose of pip?
**Definition:** pip is Python's package installer used to install and manage third-party packages.

**Example:**
```bash
pip install requests
```
**Real-World Example:** Installing libraries required for web development and API integration.

### 110. What is a virtual environment?
**Definition:** A virtual environment is an isolated Python environment with its own installed packages.

**Example:**
```bash
python -m venv myenv
```
**Real-World Example:** Maintaining different dependencies for multiple software projects.

### 111. What is file handling?
**Definition:** File handling means creating, reading, writing and managing files using Python.

**Example:**
```python
file = open("data.txt", "r")
print(file.read())
file.close()
```
**Real-World Example:** Reading reports, storing logs and processing text files.

### 112. What are the different file opening modes?
**Definition:** File modes specify how a file should be accessed, such as read (`r`), write (`w`), append (`a`), create (`x`) and binary (`b`).

**Example:**
```python
with open("data.txt", "w") as file:
    file.write("Hello")
```
**Real-World Example:** Writing application logs and reading configuration files.

### 113. What is the difference between read(), readline() and readlines()?
**Definition:** `read()` reads the entire file or a specified number of characters, `readline()` reads one line and `readlines()` returns all lines as a list.

**Example:**
```python
with open("data.txt", "r") as file:
    print(file.readline())
```
**Real-World Example:** Reading large log files line by line.

### 114. What is the with statement?
**Definition:** The with statement manages resources automatically and ensures proper cleanup when the block exits.

**Example:**
```python
with open("data.txt", "r") as file:
    print(file.read())
```
**Real-World Example:** Automatically closing files and managing database connections.

### 115. What is the purpose of __name__ == "__main__"?
**Definition:** It checks whether a Python file is being executed directly rather than imported as a module.

**Example:**
```python
if __name__ == "__main__":
    print("Program Started")
```
**Real-World Example:** Separating application execution code from reusable module code.

### 116. What is shallow copy and deep copy?
**Definition:** A shallow copy creates a new outer object but shares references to nested objects, while a deep copy recursively copies nested objects.

**Example:**
```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
c = copy.deepcopy(a)
```
**Real-World Example:** Copying complex customer records without unintentionally sharing nested data.

### 117. What is garbage collection?
**Definition:** Garbage collection is the process of managing and reclaiming memory occupied by objects that are no longer needed.

**Example:**
```python
import gc
gc.collect()
```
**Real-World Example:** Managing memory in long-running applications.

### 118. What is the Global Interpreter Lock (GIL)?
**Definition:** In traditional CPython builds, the GIL is a mechanism that allows only one thread at a time to execute Python bytecode within a process.

**Example:** Multiple threads can perform I/O operations, but CPU-bound Python threads may not execute bytecode in parallel under the traditional GIL.

**Real-World Example:** Understanding thread performance when developing multithreaded applications.

---

<div align="center">

### 🚀 Learn | Understand | Practise | Revise | Succeed

**Strong Concepts + Practical Knowledge = Interview Confidence**

</div>
