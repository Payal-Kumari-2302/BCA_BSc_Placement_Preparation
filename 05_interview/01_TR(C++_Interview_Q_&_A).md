# ⚡ C++ – Important Interview Questions & Answers

**Target Companies:** TCS, TCS Ignite, Wipro, Infosys, Accenture, Cognizant, Deloitte & Other IT Companies.

**Target Audience:** BCA Students & Freshers

---

## 1. Introduction to C++

**Definition:** C++ is a general-purpose programming language that supports procedural and object-oriented programming.

### History of C++

- **Developed By:** Bjarne Stroustrup
- **Developed At:** Bell Labs
- **First Released:** 1985
- **Originally Named:** C with Classes
- **File Extension:** `.cpp`

### ⭐ Key Features of C++

1. Object-Oriented Programming
2. Function Overloading
3. Operator Overloading
4. Multiple Inheritance
5. Templates
6. Standard Template Library (STL)
7. Exception Handling
8. Fast Execution

### Advantages

1. Supports code reusability.
2. Provides powerful STL.
3. Supports operator overloading.
4. Suitable for high-performance applications.
5. Supports multiple inheritance.

### Disadvantages

1. Complex syntax.
2. Manual memory management can cause errors.
3. No automatic garbage collection.
4. Difficult to debug large programs.

---

## 2. 🔴 PRIORITY 1 – Must Prepare

### 1. ⭐⭐⭐ What is the difference between C and C++?

| C                                      | C++                                                  |
| -------------------------------------- | ---------------------------------------------------- |
| Procedural programming language.       | Supports procedural and object-oriented programming. |
| Does not support classes and objects.  | Supports classes and objects.                        |
| Does not support function overloading. | Supports function overloading.                       |
| Uses `printf()` and `scanf()`.         | Uses `cout` and `cin`.                               |
| Does not support templates.            | Supports templates.                                  |

### 2. ⭐⭐⭐ What is Dynamic Memory Allocation in C++?

**Answer:** C++ uses `new` and `delete` operators to allocate and release memory dynamically.

**Advantages:**

- Allocates memory when needed.
- Supports object creation at runtime.

**Disadvantages:**

- Memory leaks can occur.
- Requires proper memory management.

### 5. ⭐⭐⭐ Difference between `new` and `malloc()`?

| `new`                              | `malloc()`                         |
| ---------------------------------- | ---------------------------------- |
| C++ operator.                      | C library function.                |
| Returns a typed pointer.           | Returns a `void*` pointer.         |
| Calls constructors for objects.    | Does not call constructors.        |
| Memory is released using `delete`. | Memory is released using `free()`. |

### 6. ⭐⭐⭐ What is STL in C++?

**Answer:** STL (Standard Template Library) provides ready-made containers, algorithms and iterators.

**Examples:** Vector, Stack, Queue, Map and Sort.

**Advantages:**

- Saves development time.
- Provides reusable data structures and algorithms.

### 7. ⭐⭐⭐ What are Templates in C++?

**Answer:** Templates allow writing generic functions and classes that work with different data types.

**Types:**

- Function Template
- Class Template

### 8. ⭐⭐⭐ What is the difference between `delete` and `delete[]`?

- `delete`: Releases memory allocated for a single object.
- `delete[]`: Releases memory allocated for an array.

---

## 3. 🟡 PRIORITY 2 – Additional Important Questions

###

|   |   |
| - | - |
|   |   |
|   |   |

### 10. ⭐⭐ What is Multiple Inheritance?

**Answer:** Multiple inheritance allows a class to inherit from more than one base class.

### 11. ⭐⭐ What is a Reference Variable?

**Answer:** A reference variable is another name (alias) for an existing variable.

**Example:**

```cpp
int a = 10;
int &ref = a;
```

### 12. ⭐⭐ What is the difference between `cin` and `cout`?

- `cin`: Takes input from the user.
- `cout`: Displays output on the screen.

**Example:**

```cpp
int age;
cin >> age;
cout << age;
```

### 13. ⭐⭐ What is a Namespace?

**Answer:** A namespace organizes code and prevents naming conflicts.

**Example:** `std`

### 14. ⭐⭐ What is a Friend Function?

**Answer:** A friend function can access the private and protected members of a class.

### 15. ⭐⭐ What is an Inline Function?

**Answer:** An inline function suggests that the compiler replace a function call with its function body.

### 17. ⭐⭐ What is a Virtual Function?

**Answer:** A virtual function enables runtime polymorphism through base-class pointers or references.

### 18. What is a Pure Virtual Function?

**Answer:** A pure virtual function is declared using `= 0` and makes its class abstract.

**Example:**

```cpp
virtual void display() = 0;
```

---

## 4. Important C++-Specific Keywords

| Keyword     | Use                                             |
| ----------- | ----------------------------------------------- |
| `new`       | Allocates memory dynamically.                   |
| `delete`    | Releases dynamically allocated memory.          |
| `virtual`   | Supports runtime polymorphism.                  |
| `friend`    | Allows access to private and protected members. |
| `inline`    | Suggests inline function expansion.             |
| `namespace` | Organizes code and prevents naming conflicts.   |
| `template`  | Creates generic functions and classes.          |
| `this`      | Refers to the current object.                   |
| `throw`     | Throws an exception.                            |
| `catch`     | Handles an exception.                           |

---

## 5. Preparation Strategy

**Priority 1:**

- C vs C++.
- Function Overloading.
- Operator Overloading.
- `new` vs `malloc()`.
- STL.
- Templates.
- `delete` vs `delete[]`.

**Priority 2:**

- Structure vs Class.
- Multiple Inheritance.
- Reference Variables.
- `cin` and `cout`.
- Namespace.
- Friend Function.
- Inline Function.
- Exception Handling.
- Virtual and Pure Virtual Functions.

---

**Goal:** Prepare C++-specific interview concepts without repeating C programming and basic Python OOP concepts.
