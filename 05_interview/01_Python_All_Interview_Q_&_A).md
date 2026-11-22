<div align="center">

# 🐍 Python Technical Interview Preparation

### 118 Important Questions | Short Definitions | Examples | Real-World Uses

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)
![Questions](https://img.shields.io/badge/Questions-118-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Basic%20to%20Advanced-orange?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-IT%20Placements-red?style=for-the-badge)

**Target Companies:** TCS, Wipro, Infosys, Accenture, Cognizant, Deloitte, Genpact & Other IT Companies.

**Target Audience:** BCA Students | Freshers | Entry-Level IT Professionals

</div>

---

# 📚 PART 01 – Python Fundamentals (15 Questions)

### 🕰️ A Short History of Python

- **Created by:** Guido van Rossum.
- **Development started:** December 1989 in the Netherlands.
- **First released:** 1991.
- **Name origin:** Inspired by *Monty Python's Flying Circus*.
- **Python 2:** Released in 2000; discontinued in 2020.
- **Python 3:** Released in 2008; modern Python version.

### 1. What is Python?
**Definition:** Python is a high-level, interpreted, general-purpose programming language known for simple syntax and readability.

**Example:**
```python
print("Hello, World!")
```
**Real-World Example:** Used in web development, automation, data analysis and AI.

### 2. What are the main features of Python?
**Definition:** Python is simple, interpreted, dynamically typed, portable, open-source and object-oriented.

**Example:**
```python
name = "Payal"
print(name)
```
**Real-World Example:** Developers build applications quickly using less code.

### 3. Why is Python called an interpreted language?
**Definition:** Python code is executed through an interpreter. CPython compiles source code into bytecode before execution.

**Example:**
```python
print(10 + 20)
```
**Real-World Example:** Running Python scripts directly through the Python interpreter.

### 4. Is Python dynamically typed or statically typed?
**Definition:** Python is dynamically typed because variable types are determined at runtime.

**Example:**
```python
x = 10
x = "Python"
```
**Real-World Example:** Variables can refer to different data types during execution.

### 5. What are the advantages and disadvantages of Python?
**Definition:** Python is easy to learn and has many libraries, but can be slower than compiled languages.

**Example:**
```python
print(sum([10, 20, 30]))
```
**Real-World Example:** Useful for automation and data analysis; C or C++ may suit performance-critical tasks.

### 6. What is the difference between Python 2 and Python 3?
**Definition:** Python 3 has improved syntax and Unicode support; Python 2 is discontinued.

**Example:**
```python
print("Hello Python 3")
```
**Real-World Example:** Modern IT projects generally use Python 3.

### 7. What are keywords in Python?
**Definition:** Keywords are reserved words with special meanings that cannot be used as ordinary identifiers.

**Example:**
```python
if True:
    print("Python")
```
**Real-World Example:** `if`, `else`, `for` and `while` control program execution.

### 8. What are identifiers in Python?
**Definition:** Identifiers are names used for variables, functions, classes and other objects.

**Example:**
```python
student_name = "Payal"
```
**Real-World Example:** Naming employee records, functions and variables.

### 9. What are variables in Python?
**Definition:** Variables are names that refer to objects and their values.

**Example:**
```python
name = "Payal"
age = 22
```
**Real-World Example:** Storing usernames, prices and customer details.

### 10. What are the rules for naming variables?
**Definition:** Names must start with a letter or underscore, cannot start with numbers or contain spaces, and cannot be keywords.

**Example:**
```python
student_name = "Payal"
_age = 22
```
**Real-World Example:** Meaningful names improve code readability.

### 11. What are comments in Python?
**Definition:** Comments are non-executable statements used to explain code.

**Example:**
```python
# Calculate total marks
marks = 450
```
**Real-World Example:** Explaining business logic to team members.

### 12. What is indentation in Python?
**Definition:** Indentation means spaces at the beginning of a line to define a code block.

**Example:**
```python
if 10 > 5:
    print("Greater")
```
**Real-World Example:** Organizing conditions, loops and functions.

### 13. Why is indentation important in Python?
**Definition:** Python uses indentation to identify code blocks instead of curly braces.

**Example:**
```python
if True:
    print("Correct")
```
**Real-World Example:** Preventing indentation errors and improving readability.

### 14. What is the difference between a compiler and an interpreter?
**Definition:** A compiler translates source code before execution, while an interpreter executes code through a runtime environment.

**Example:** C commonly uses compilation; Python uses an interpreter-based execution model.

**Real-World Example:** Compiled languages are often used for performance-critical applications.

### 15. What is PEP 8?
**Definition:** PEP 8 is Python's official style guide for writing readable and consistent code.

**Example:**
```python
student_name = "Payal"
total_marks = 450
```
**Real-World Example:** Development teams follow PEP 8 coding standards.

---

# 📚 PART 02 – Data Types and Variables (10 Questions)

### 16. What are data types in Python?
**Definition:** Data types define the kind of value an object represents.

**Example:**
```python
age = 22
name = "Payal"
price = 99.5
```
**Real-World Example:** Integers store age, strings store names and floats store prices.

### 17. What are the built-in data types in Python?
**Definition:** Built-in types include int, float, complex, str, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray and NoneType.

**Example:**
```python
age = 22
name = "Payal"
marks = [80, 90, 95]
```
**Real-World Example:** Different types store different kinds of application data.

### 18. What is the difference between mutable and immutable data types?
**Definition:** Mutable objects can be changed after creation; immutable objects cannot.

**Example:**
```python
my_list = [10, 20]
my_list.append(30)

name = "Python"
```
**Real-World Example:** Lists store changing cart items; strings represent immutable text.

### 19. What is type casting?
**Definition:** Type casting converts one data type into another.

**Example:**
```python
age = "22"
age = int(age)
```
**Real-World Example:** Converting user input into numbers for calculations.

### 20. What is the difference between implicit and explicit type conversion?
**Definition:** Implicit conversion happens automatically; explicit conversion is performed manually.

**Example:**
```python
# Implicit
a = 10
b = 2.5
c = a + b

# Explicit
x = int("100")
```
**Real-World Example:** Converting entered text into numeric values for billing.

### 21. What is the difference between int, float and complex?
**Definition:** int stores whole numbers, float stores decimal numbers and complex stores real and imaginary parts.

**Example:**
```python
a = 10
b = 10.5
c = 3 + 4j
```
**Real-World Example:** Quantities use integers, prices use floats and scientific calculations may use complex numbers.

### 22. What is the difference between list, tuple and set?
**Definition:** A list is ordered and mutable, a tuple is ordered and immutable, and a set stores unique elements without guaranteed positional order.

**Example:**
```python
my_list = [10, 20, 10]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
```
**Real-World Example:** Lists store cart items, tuples store fixed coordinates and sets remove duplicates.

### 23. What is a dictionary in Python?
**Definition:** A dictionary is a mutable collection of key-value pairs.

**Example:**
```python
student = {"name": "Payal", "age": 22}
```
**Real-World Example:** Storing employee details and user profiles.

### 24. What is the difference between None, 0 and False?
**Definition:** None represents absence of a value, 0 is an integer and False is a Boolean value.

**Example:**
```python
a = None
b = 0
c = False
```
**Real-World Example:** None represents missing information, 0 represents a zero balance and False represents a negative Boolean condition.

### 25. What is dynamic typing?
**Definition:** Dynamic typing allows a variable name to refer to objects of different types during execution.

**Example:**
```python
x = 100
x = "Hello"
```
**Real-World Example:** Processing different input types using the same variable name.

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
**Real-World Example:** Calculating prices, discounts and salaries.

### 27. Explain arithmetic operators.
**Definition:** Arithmetic operators perform addition, subtraction, multiplication, division, modulus, floor division and exponentiation.

**Example:**
```python
a = 10
b = 3
print(a + b)
print(a % b)
```
**Real-World Example:** Calculating bills, taxes and discounts.

### 28. What is the difference between / and //?
**Definition:** `/` performs division and returns a float; `//` performs floor division.

**Example:**
```python
print(10 / 3)
print(10 // 3)
```
**Real-World Example:** Calculating complete groups or packages.

### 29. What is the difference between == and is?
**Definition:** `==` compares values, while `is` checks object identity.

**Example:**
```python
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)
```
**Real-World Example:** Using `is None` to check missing values.

### 30. What are logical operators?
**Definition:** Logical operators combine or reverse conditions using `and`, `or` and `not`.

**Example:**
```python
age = 22
print(age >= 18 and age <= 60)
```
**Real-World Example:** Checking login conditions and user permissions.

### 31. What are membership operators?
**Definition:** `in` and `not in` check whether a value exists in a collection.

**Example:**
```python
names = ["Payal", "Riya"]
print("Payal" in names)
```
**Real-World Example:** Checking whether a username exists.

### 32. What are identity operators?
**Definition:** `is` and `is not` check whether references point to the same object.

**Example:**
```python
a = None
print(a is None)
```
**Real-World Example:** Checking whether a database result is None.

### 33. What is the difference between break, continue and pass?
**Definition:** `break` terminates a loop, `continue` skips an iteration and `pass` does nothing.

**Example:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
**Real-World Example:** Stopping a search, skipping invalid records or creating an empty code block.

### 34. What is the difference between if, elif and else?
**Definition:** `if` checks the first condition, `elif` checks additional conditions and `else` runs when none is true.

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
**Real-World Example:** Assigning grades based on marks.

### 35. What is a nested loop?
**Definition:** A nested loop is a loop placed inside another loop.

**Example:**
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```
**Real-World Example:** Processing rows and columns in a matrix.

### 36. What is the difference between for and while loops?
**Definition:** A for loop iterates over a sequence; a while loop repeats while a condition is true.

**Example:**
```python
for i in range(3):
    print(i)

x = 0
while x < 3:
    print(x)
    x += 1
```
**Real-World Example:** Processing employee records or repeatedly asking for valid input.

---

# 📚 PART 04 – Strings (9 Questions)

### 37. What is a string in Python?
**Definition:** A string is an immutable sequence of Unicode characters enclosed in quotes.

**Example:**
```python
name = "Python"
```
**Real-World Example:** Storing names, addresses and messages.

### 38. Are strings mutable or immutable?
**Definition:** Strings are immutable; their characters cannot be changed directly after creation.

**Example:**
```python
name = "Python"
name = "Java"
```
**Real-World Example:** Changing a text value creates a new string object.

### 39. What is string slicing?
**Definition:** Slicing extracts part of a string using start, stop and step indexes.

**Example:**
```python
text = "Python"
print(text[0:3])
```
**Real-World Example:** Extracting parts of an email address.

### 40. What is negative indexing?
**Definition:** Negative indexing accesses sequence elements from the end.

**Example:**
```python
text = "Python"
print(text[-1])
```
**Real-World Example:** Accessing the last character of a filename.

### 41. What is the difference between find() and index()?
**Definition:** Both search for a substring. `find()` returns -1 if missing; `index()` raises ValueError.

**Example:**
```python
text = "Python"
print(text.find("z"))
```
**Real-World Example:** Searching for keywords in user messages.

### 42. What is the difference between split() and join()?
**Definition:** `split()` converts a string into a list; `join()` combines strings into one string.

**Example:**
```python
text = "Python Java C"
print(text.split())

words = ["Python", "Java"]
print(" ".join(words))
```
**Real-World Example:** Splitting text into fields and joining names into a message.

### 43. What is the difference between strip(), lstrip() and rstrip()?
**Definition:** `strip()` removes whitespace from both ends, `lstrip()` from the left and `rstrip()` from the right.

**Example:**
```python
text = "  Python  "
print(text.strip())
```
**Real-World Example:** Cleaning user input before database storage.

### 44. What are f-strings?
**Definition:** F-strings format strings by inserting variables and expressions inside curly braces.

**Example:**
```python
name = "Payal"
print(f"Hello {name}")
```
**Real-World Example:** Generating personalized messages and reports.

### 45. How can you reverse a string in Python?
**Definition:** A string can be reversed using slicing with a step of -1.

**Example:**
```python
text = "Python"
print(text[::-1])
```
**Real-World Example:** Reversing text for palindrome checking.

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
**Definition:** `append()` adds one element; `extend()` adds elements from an iterable.

**Example:**
```python
a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])
```
**Real-World Example:** Adding one product or multiple products to a cart.

### 48. What is the difference between remove(), pop() and del?
**Definition:** `remove()` deletes a value, `pop()` removes and returns an indexed element, and `del` deletes an element or slice.

**Example:**
```python
numbers = [10, 20, 30]
numbers.remove(20)
numbers.pop()
del numbers[0]
```
**Real-World Example:** Removing products or deleting unwanted records.

### 49. What is list comprehension?
**Definition:** List comprehension creates a list using a compact expression and iterable.

**Example:**
```python
squares = [x*x for x in range(5)]
```
**Real-World Example:** Creating a filtered list of employee salaries.

### 50. What is a nested list?
**Definition:** A nested list is a list containing other lists.

**Example:**
```python
matrix = [[1, 2], [3, 4]]
```
**Real-World Example:** Representing spreadsheet rows and columns.

### 51. What is a tuple?
**Definition:** A tuple is an ordered, immutable collection that allows duplicates.

**Example:**
```python
coordinates = (10, 20)
```
**Real-World Example:** Storing fixed coordinates or records.

### 52. Why are tuples immutable?
**Definition:** Tuples prevent changes to their element references after creation.

**Example:**
```python
data = (10, 20, 30)
```
**Real-World Example:** Storing fixed configuration values.

### 53. What is tuple packing and unpacking?
**Definition:** Packing combines values into a tuple; unpacking assigns tuple elements to variables.

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
**Real-World Example:** Maintaining unique email addresses.

### 55. Why does a set not allow duplicate elements?
**Definition:** Sets store unique elements based on equality and hashing.

**Example:**
```python
numbers = {1, 2, 2, 3}
print(numbers)
```
**Real-World Example:** Removing duplicate customer IDs.

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
**Real-World Example:** Comparing users registered on two platforms.

### 57. What is a dictionary?
**Definition:** A dictionary is a mutable collection of unique keys and corresponding values.

**Example:**
```python
student = {"name": "Payal", "age": 22}
```
**Real-World Example:** Storing customer profiles and employee details.

### 58. What is the difference between keys(), values() and items()?
**Definition:** `keys()` returns keys, `values()` returns values and `items()` returns key-value pairs.

**Example:**
```python
student = {"name": "Payal", "age": 22}

print(student.keys())
print(student.values())
print(student.items())
```
**Real-World Example:** Extracting employee names, salaries or complete records.

### 59. What is the difference between get() and direct key access?
**Definition:** `get()` returns None or a default value for a missing key; direct access raises KeyError.

**Example:**
```python
data = {"name": "Payal"}
print(data.get("age"))
```
**Real-World Example:** Safely retrieving optional customer information.

### 60. Can a dictionary contain duplicate keys?
**Definition:** No. Dictionary keys are unique; assigning an existing key replaces its previous value.

**Example:**
```python
data = {"name": "Payal", "name": "Riya"}
print(data)
```
**Real-World Example:** Updating an employee record using its unique ID.

---

# 📚 PART 06 – Functions (14 Questions)

### 61. What is a function in Python?
**Definition:** A function is a reusable block of code that performs a specific task.

**Example:**
```python
def greet():
    print("Hello")
```
**Real-World Example:** Reusing a login function across application screens.

### 62. What are the advantages of using functions?
**Definition:** Functions improve code reusability, readability, organization and maintainability.

**Example:**
```python
def add(a, b):
    return a + b
```
**Real-World Example:** Reusing payment calculations across an application.

### 63. What is the difference between built-in and user-defined functions?
**Definition:** Built-in functions are provided by Python; user-defined functions are created by developers.

**Example:**
```python
print(len("Python"))

def greet():
    print("Hello")
```
**Real-World Example:** Using built-in functions for calculations and custom functions for business logic.

### 64. What are parameters and arguments?
**Definition:** Parameters are variables in a function definition; arguments are actual values passed during a function call.

**Example:**
```python
def greet(name):
    print(name)

greet("Payal")
```
**Real-World Example:** Passing customer details to a registration function.

### 65. What is the difference between return and print()?
**Definition:** `return` sends a value back from a function; `print()` displays information.

**Example:**
```python
def add(a, b):
    return a + b
```
**Real-World Example:** Returning a calculated bill amount to another function.

### 66. What are default arguments?
**Definition:** Default arguments are parameters with predefined values used when no argument is supplied.

**Example:**
```python
def greet(name="Guest"):
    print(name)
```
**Real-World Example:** Providing a default language or country setting.

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
**Definition:** Positional arguments assign values to parameters according to their position.

**Example:**
```python
def add(a, b):
    return a + b

add(10, 20)
```
**Real-World Example:** Passing product quantity and price to a billing function.

### 69. What are *args and **kwargs?
**Definition:** `*args` collects extra positional arguments into a tuple; `**kwargs` collects keyword arguments into a dictionary.

**Example:**
```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
```
**Real-World Example:** Creating flexible functions for different inputs and settings.

### 70. What is recursion?
**Definition:** Recursion occurs when a function calls itself until a base condition is reached.

**Example:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
**Real-World Example:** Traversing folders and tree structures.

### 71. What is a lambda function?
**Definition:** A lambda function is a small anonymous function written using the lambda keyword.

**Example:**
```python
square = lambda x: x * x
print(square(5))
```
**Real-World Example:** Sorting records using a short custom expression.

### 72. What is the difference between local and global variables?
**Definition:** Local variables are defined inside a function; global variables are defined outside functions.

**Example:**
```python
x = 10

def demo():
    y = 20
```
**Real-World Example:** Local variables store temporary calculations; global constants store application-wide settings.

### 73. What is the global keyword?
**Definition:** The global keyword allows a function to reassign a variable defined in global scope.

**Example:**
```python
x = 10

def update():
    global x
    x = 20
```
**Real-World Example:** Updating a shared application counter.

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
**Real-World Example:** Developing banking and employee management systems.

### 76. What is a class in Python?
**Definition:** A class is a blueprint for creating objects containing attributes and methods.

**Example:**
```python
class Student:
    name = "Payal"
```
**Real-World Example:** An Employee class defines common employee properties.

### 77. What is an object?
**Definition:** An object is an instance of a class containing data and behavior.

**Example:**
```python
class Student:
    pass

s1 = Student()
```
**Real-World Example:** Individual employee records created from an Employee class.

### 78. What is the difference between a class and an object?
**Definition:** A class is a blueprint; an object is an instance created from it.

**Example:**
```python
class Car:
    pass

car1 = Car()
```
**Real-World Example:** Car is a class; a particular Honda car is an object.

### 79. What is a constructor?
**Definition:** A constructor initializes an object during creation. Python commonly uses `__init__()` for initialization.

**Example:**
```python
class Student:
    def __init__(self, name):
        self.name = name
```
**Real-World Example:** Initializing employee names and IDs.

### 80. What is the __init__() method?
**Definition:** `__init__()` is an initializer automatically called after an object is created.

**Example:**
```python
class Student:
    def __init__(self):
        self.name = "Payal"
```
**Real-World Example:** Setting default values for new customer objects.

### 81. What is the self keyword?
**Definition:** `self` refers to the current instance and accesses its attributes and methods.

**Example:**
```python
class Student:
    def show(self):
        print("Hello")
```
**Real-World Example:** Accessing details of a particular employee object.

### 82. What are the four pillars of OOPs?
**Definition:** The four pillars are inheritance, polymorphism, encapsulation and abstraction.

**Example:** A banking application can use all four concepts.

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
**Real-World Example:** Employee types inherit common details from a base class.

### 84. What are the different types of inheritance?
**Definition:** Python supports single, multiple, multilevel, hierarchical and hybrid inheritance.

**Example:** A child class can inherit from one or multiple parent classes.

**Real-World Example:** Designing classes with shared functionality.

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
**Definition:** Polymorphism allows the same interface or method name to represent different behaviors.

**Example:**
```python
print(len("Python"))
print(len([10, 20, 30]))
```
**Real-World Example:** Different payment methods implement the same pay operation differently.

### 87. What is method overriding?
**Definition:** Method overriding occurs when a child class provides its own implementation of an inherited method.

**Example:**
```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```
**Real-World Example:** Different employee types implement their own salary calculations.

### 88. What is method overloading?
**Definition:** Method overloading uses the same method name with different parameter lists. Python does not directly support traditional compile-time overloading.

**Example:**
```python
def add(a, b=0):
    return a + b
```
**Real-World Example:** Flexible functions accept different numbers of inputs.

### 89. What is encapsulation?
**Definition:** Encapsulation combines data and methods inside a class and controls access to internal details.

**Example:**
```python
class Account:
    def __init__(self):
        self.__balance = 1000
```
**Real-World Example:** Protecting account data from unintended direct modification.

### 90. What is abstraction?
**Definition:** Abstraction hides implementation details and exposes essential functionality.

**Example:**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
```
**Real-World Example:** Driving a car without understanding its internal engine mechanism.

### 91. What is the difference between instance, class and static methods?
**Definition:** Instance methods work with object data, class methods work with class-level data and static methods are utility methods without automatic instance or class arguments.

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
**Real-World Example:** Employee operations, class-level counters and utility calculations.

### 92. What is the difference between super() and self?
**Definition:** `self` refers to the current object; `super()` accesses methods in the next class in the method resolution order.

**Example:**
```python
class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        super().show()
```
**Real-World Example:** Reusing parent-class initialization and functionality.

---

# 📚 PART 08 – Exception Handling (8 Questions)

### 93. What is an exception?
**Definition:** An exception is an event that interrupts the normal flow of a program during execution.

**Example:**
```python
print(10 / 0)
```
**Real-World Example:** A program encounters an exception when invalid data is entered.

### 94. What is exception handling?
**Definition:** Exception handling detects and handles runtime errors without unexpectedly terminating a program.

**Example:**
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```
**Real-World Example:** Handling failed database connections or invalid input.

### 95. What is the difference between an error and an exception?
**Definition:** Errors are program problems; exceptions are runtime events that can often be handled.

**Example:** SyntaxError occurs due to invalid syntax; ZeroDivisionError occurs during execution.

**Real-World Example:** Fixing syntax errors and handling runtime exceptions.

### 96. What is the use of try and except?
**Definition:** `try` contains code that may raise an exception; `except` handles it.

**Example:**
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
```
**Real-World Example:** Validating user input in registration forms.

### 97. What is the purpose of finally?
**Definition:** The finally block executes whether an exception occurs or not and is commonly used for cleanup.

**Example:**
```python
try:
    print("Processing")
finally:
    print("Completed")
```
**Real-World Example:** Closing files and releasing database connections.

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
**Real-World Example:** Processing a payment after successful validation.

### 99. What is the raise keyword?
**Definition:** The raise keyword manually triggers an exception.

**Example:**
```python
age = 15

if age < 18:
    raise ValueError("Not eligible")
```
**Real-World Example:** Rejecting invalid ages or transaction amounts.

### 100. How can you create a custom exception?
**Definition:** A custom exception is a class that inherits from the Exception class.

**Example:**
```python
class InvalidAgeError(Exception):
    pass
```
**Real-World Example:** Creating application-specific errors for invalid employee IDs or payment failures.

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
**Real-World Example:** Iterating over employee or customer records.

### 103. What is a generator?
**Definition:** A generator is a special iterator that produces values one at a time using `yield`.

**Example:**
```python
def numbers():
    yield 1
    yield 2
    yield 3
```
**Real-World Example:** Reading large files without loading everything into memory.

### 104. What is the difference between yield and return?
**Definition:** `return` ends a function and sends back a value; `yield` produces a value and suspends execution.

**Example:**
```python
def demo():
    yield 10
    yield 20
```
**Real-World Example:** Generating records gradually from a large database query.

### 105. What is a decorator?
**Definition:** A decorator modifies or extends another function's behavior without changing its original code.

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
**Definition:** A module is a Python file containing reusable functions, variables and classes.

**Example:**
```python
import math
print(math.sqrt(25))
```
**Real-World Example:** Organizing application functionality into separate Python files.

### 107. What is a package in Python?
**Definition:** A package organizes related Python modules into a directory hierarchy.

**Example:**
```python
import os
```
**Real-World Example:** Organizing authentication, database and payment modules.

### 108. What is the difference between a module and a package?
**Definition:** A module is generally a single Python file; a package organizes multiple modules in a directory structure.

**Example:** `math` is a module; `email` is a standard-library package.

**Real-World Example:** Organizing application code into modules and packages.

### 109. What is the purpose of pip?
**Definition:** pip is Python's package installer for managing third-party packages.

**Example:**
```bash
pip install requests
```
**Real-World Example:** Installing libraries for web development and API integration.

### 110. What is a virtual environment?
**Definition:** A virtual environment is an isolated Python environment with its own installed packages.

**Example:**
```bash
python -m venv myenv
```
**Real-World Example:** Maintaining separate dependencies for different projects.

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
**Definition:** File modes specify access: read (`r`), write (`w`), append (`a`), create (`x`) and binary (`b`).

**Example:**
```python
with open("data.txt", "w") as file:
    file.write("Hello")
```
**Real-World Example:** Writing application logs and reading configuration files.

### 113. What is the difference between read(), readline() and readlines()?
**Definition:** `read()` reads the file or specified characters, `readline()` reads one line and `readlines()` returns all lines as a list.

**Example:**
```python
with open("data.txt", "r") as file:
    print(file.readline())
```
**Real-World Example:** Reading large log files line by line.

### 114. What is the with statement?
**Definition:** The with statement manages resources and ensures proper cleanup when the block exits.

**Example:**
```python
with open("data.txt", "r") as file:
    print(file.read())
```
**Real-World Example:** Automatically closing files and managing database connections.

### 115. What is the purpose of __name__ == "__main__"?
**Definition:** It checks whether a Python file is executed directly rather than imported as a module.

**Example:**
```python
if __name__ == "__main__":
    print("Program Started")
```
**Real-World Example:** Separating application execution code from reusable module code.

### 116. What is shallow copy and deep copy?
**Definition:** A shallow copy creates a new outer object but shares nested references; a deep copy recursively copies nested objects.

**Example:**
```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
c = copy.deepcopy(a)
```
**Real-World Example:** Copying complex customer records without sharing nested data.

### 117. What is garbage collection?
**Definition:** Garbage collection manages and reclaims memory occupied by objects that are no longer needed.

**Example:**
```python
import gc
gc.collect()
```
**Real-World Example:** Managing memory in long-running applications.

### 118. What is the Global Interpreter Lock (GIL)?
**Definition:** In traditional CPython builds, the GIL allows only one thread at a time to execute Python bytecode within a process.

**Example:** Multiple threads can perform I/O operations, but CPU-bound threads may not execute bytecode in parallel under the traditional GIL.

**Real-World Example:** Understanding thread performance in multithreaded applications.

---

<div align="center">

### 🚀 Learn | Understand | Practise | Revise | Succeed

**Strong Concepts + Practical Knowledge = Interview Confidence**

</div>
