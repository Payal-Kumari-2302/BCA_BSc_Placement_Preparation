# C++ – Important Interview Questions & Answers

**Target Companies:** TCS, TCS Ignite, Wipro, Infosys, Accenture, Cognizant, Deloitte & Other IT Companies.

**Target Audience:** BCA Students & Freshers

**Primary Programming Language:** Python


## 1.What is c++
 C++: C++ is a general-purpose, object-oriented programming language developed by Bjarne Stroustrup in 1985
## 📌 Introduction to C++

- **Developed By:** Bjarne Stroustrup
- **Developed At:** Bell Labs
- **First Released:** 1985
- **Originally Named:** C with Classes
- **File Extension:** `.cpp`

### ⭐ Key Features of C++

- Object-Oriented Programming
- Pointers
- Dynamic Memory Allocation
- Function and Operator Overloading
- Multiple Inheritance
- Standard Template Library (STL)
- Fast Execution

## 🔴 Priority 1 – Must Prepare

### 1. ⭐⭐⭐ What is the difference between C and C++?

| C | C++ |
|---|---|
| Procedural programming language. | Supports procedural and object-oriented programming. |
| Does not support classes and objects. | Supports classes and objects. |
| Does not support function overloading. | Supports function overloading. |
| Uses `printf()` and `scanf()`. | Uses `cout` and `cin`. |


```

**Advantages:**
- Memory can be allocated when needed.
- Supports flexible memory management.

**Disadvantages:**
- Memory leaks can occur.
- Requires manual memory management.

### 5. ⭐⭐⭐ What is the difference between `new` and `malloc()`?

| new | malloc() |
|---|---|
| C++ operator. | C library function. |
| Returns a typed pointer. | Returns a `void*` pointer. |
| Calls constructors for objects. | Does not call constructors. |
| Memory is released using `delete`. | Memory is released using `free()`. |

## 🟡 Priority 2 – Important

### 6. ⭐⭐ What is the difference between Structure and Class?

| Structure | Class |
|---|---|
| Members are public by default. | Members are private by default. |
| Uses the `struct` keyword. | Uses the `class` keyword. |

### 7. ⭐⭐ What is the difference between Call by Value and Call by Reference?

| Call by Value | Call by Reference |
|---|---|
| A copy of the value is passed. | The original variable is accessed through a reference. |
| Changes do not affect the original variable. | Changes affect the original variable. |

### 8. ⭐⭐ What is Multiple Inheritance?

**Definition:** Multiple inheritance allows a class to inherit properties and functions from more than one base class.

**Example:** A child class inherits from two parent classes.

### 9. ⭐⭐ What is STL in C++?

**Definition:** STL (Standard Template Library) provides ready-made containers, algorithms and iterators.

**Examples:** Vector, Stack, Queue and Sort.

**Advantages:**
- Saves development time.
- Provides reusable data structures and algorithms.

### 10. ⭐⭐ What is the difference between `delete` and `delete[]`?

- **delete:** Releases memory allocated for a single object.
- **delete[]:** Releases memory allocated for an array.

### 11. ⭐⭐ What is a Reference Variable?

**Definition:** A reference variable is another name (alias) for an existing variable.

**Example:**
```cpp
int a = 10;
int &ref = a;
```

### 12. ⭐⭐ What is the difference between Structure and Union?

| Structure | Union |
|---|---|
| Each member has separate memory. | All members share the same memory. |
| Multiple members can hold values simultaneously. | Only one member's value is meaningfully stored at a time. |
| Size is based on its members and padding. | Size is based on its largest member and alignment. |

### 13. ⭐⭐ What is the difference between `cin` and `cout`?

- **cin:** Used to take input from the user.
- **cout:** Used to display output on the screen.

**Example:**
```cpp
int age;
cin >> age;
cout << age;
```

### 14. ⭐⭐ What is the difference between `break` and `continue`?

- **break:** Terminates the loop.
- **continue:** Skips the current iteration and moves to the next iteration.

## 📌 Preparation Strategy

- ⭐⭐⭐ Prepare all Priority 1 questions thoroughly.
- ⭐⭐ Understand Priority 2 questions with examples.
- Practise basic pointer and array programs.
- Understand dynamic memory allocation and STL basics.
- Revise common OOP concepts separately.

**Goal:** Prepare C++-specific fundamentals without repeating Python and common OOP interview topics.
