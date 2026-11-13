# 💻 C Programming – Interview Preparation

**Target Companies:** TCS, Wipro, Infosys, Accenture, Cognizant, Deloitte & Other IT Companies.

## 1. Introduction to C

**Definition:** C is a general-purpose procedural programming language developed by Dennis Ritchie.

### History
- **1972:** Developed by Dennis Ritchie.
- **Developed At:** Bell Laboratories.
- **Purpose:** UNIX operating system development.

### Features
1. Procedural Programming
2. Pointer Support
3. Low-Level Memory Access
4. Dynamic Memory Allocation
5. Fast Execution
6. Portable
7. Structured Programming

### Advantages
1. Fast execution.
2. Direct memory access through pointers.
3. Efficient system programming.
4. Low-level programming support.

### Disadvantages
1. Manual memory management.
2. No automatic garbage collection.
3. No built-in OOP support.
4. No built-in exception handling.

---

## 2. 🔴 PRIORITY 1 – Most Important C-Specific Questions

### 1. ⭐ What is a Pointer?
**Answer:** A pointer stores the memory address of another variable.

### 2. ⭐ What is Pointer Arithmetic?
**Answer:** Performing arithmetic operations on pointers to navigate memory locations.

### 3. ⭐ What is a NULL Pointer?
**Answer:** A pointer that does not point to a valid object.

### 4. ⭐ What is a Void Pointer?
**Answer:** A generic pointer that can hold the address of any object type.

### 5. ⭐ What is a Dangling Pointer?
**Answer:** A pointer referring to an object whose lifetime has ended.

### 6. ⭐ What is Dynamic Memory Allocation?
**Answer:** Allocating memory at runtime using standard library functions.

**Functions:** `malloc()`, `calloc()`, `realloc()`, `free()`.

### 7. ⭐ Difference between malloc() and calloc()?

| malloc() | calloc() |
|---|---|
| Allocates a memory block. | Allocates memory for multiple elements. |
| Memory is uninitialized. | Memory is initialized to zero. |
| Takes one argument. | Takes two arguments. |

### 8. ⭐ What is a Memory Leak?
**Answer:** A memory leak occurs when dynamically allocated memory is not released after use.

### 9. ⭐ What is a Segmentation Fault?
**Answer:** An error caused by invalid memory access.

### 10. ⭐ What is a Structure?
**Answer:** A structure groups different data types under one name.

### 11. ⭐ What is a Union?
**Answer:** A union allows different members to share the same memory.

### 12. ⭐ Difference between Structure and Union?

| Structure | Union |
|---|---|
| Members have separate storage. | Members share storage. |
| Multiple members can hold values simultaneously. | Only one member's value is meaningful at a time. |
| Size depends on members and padding. | Size depends on the largest member and alignment. |

### 13. ⭐ What is a Function Pointer?
**Answer:** A pointer that stores the address of a function.

### 14. ⭐ What is a Preprocessor?
**Answer:** It processes preprocessing directives before compilation.

### 15. ⭐ What is a Macro?
**Answer:** A macro is defined using `#define` and expanded by the preprocessor.

### 16. ⭐ What is a Header File?
**Answer:** A file containing declarations and macros shared across C programs.

**Examples:** `stdio.h`, `stdlib.h`, `string.h`.

### 17. ⭐ What is a Storage Class?
**Answer:** It defines a variable's scope, lifetime and linkage.

**Types:** `auto`, `register`, `static`, `extern`.

---

## 3. 🟡 PRIORITY 2 – Additional C-Specific Questions

### 18. What is Typedef?
**Answer:** It creates an alternative name for an existing data type.

### 19. What is Enum?
**Answer:** It defines named integer constants.

### 20. What is the Difference between const and #define?
**Answer:**
- `const`: Declares a read-only object.
- `#define`: Defines a preprocessor macro.

### 21. What is a Command-Line Argument?
**Answer:** It passes arguments to a program when execution starts.

**Example:** `int main(int argc, char *argv[])`

### 22. What is File Pointer?
**Answer:** A `FILE` pointer is used to access and manage files in C.

### 23. What is the Difference between Text File and Binary File?
**Answer:**
- Text File: Stores data in readable text format.
- Binary File: Stores data in binary format.

### 24. What is the Difference between fopen() and fclose()?
**Answer:**
- `fopen()`: Opens a file.
- `fclose()`: Closes a file.

### 25. What is the Difference between fgetc() and fgets()?
**Answer:**
- `fgetc()`: Reads one character.
- `fgets()`: Reads a string or line.

### 26. What is the Difference between fprintf() and fscanf()?
**Answer:**
- `fprintf()`: Writes formatted data to a file.
- `fscanf()`: Reads formatted data from a file.

### 27. What is the Difference between fread() and fwrite()?
**Answer:**
- `fread()`: Reads binary data.
- `fwrite()`: Writes binary data.

---

## 4. C-Specific Important Functions

| Function | Purpose |
|---|---|
| `malloc()` | Allocates memory. |
| `calloc()` | Allocates zero-initialized memory. |
| `realloc()` | Changes allocated memory size. |
| `free()` | Releases allocated memory. |
| `sizeof()` | Returns size in bytes. |
| `fopen()` | Opens a file. |
| `fclose()` | Closes a file. |
| `fread()` | Reads binary data. |
| `fwrite()` | Writes binary data. |
| `fseek()` | Changes file position. |
| `ftell()` | Returns current file position. |
| `rewind()` | Moves file position to the beginning. |

---
