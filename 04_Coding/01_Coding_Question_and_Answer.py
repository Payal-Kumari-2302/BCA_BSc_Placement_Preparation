# Python Coding Questions – Priority 1
### 15 Must-Prepare Programs for TCS, Wipro, Cognizant & Accenture

## Q1. Reverse a Number

**Code:**
```python
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)
```

**Input:**
```text
12345
```
**Output:**
```text
Reversed number: 54321
```

## Q2. Check Whether a Number Is Palindrome

**Code:**
```python
n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")
```

**Input:**
```text
121
```
**Output:**
```text
Palindrome Number
```

## Q3. Check Whether a Number Is Prime

**Code:**
```python
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")
```

**Input:**
```text
7
```
**Output:**
```text
Prime Number
```

## Q4. Find the Factorial of a Number

**Code:**
```python
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)
```

**Input:**
```text
5
```
**Output:**
```text
Factorial: 120
```

## Q5. Print the Fibonacci Series

**Code:**
```python
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
```

**Input:**
```text
7
```
**Output:**
```text
0 1 1 2 3 5 8
```

## Q6. Check Whether a Number Is Armstrong

**Code:**
```python
n = int(input("Enter a number: "))
temp = n
power = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** power
    n = n // 10

if temp == total:
    print("Armstrong Number")
else:
    print("Not Armstrong")
```

**Input:**
```text
153
```
**Output:**
```text
Armstrong Number
```

## Q7. Find the Sum of Digits of a Number

**Code:**
```python
n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits:", total)
```

**Input:**
```text
1234
```
**Output:**
```text
Sum of digits: 10
```

## Q8. Count the Digits of a Number

**Code:**
```python
n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n = n // 10

print("Total digits:", count)
```

**Input:**
```text
12345
```
**Output:**
```text
Total digits: 5
```

## Q9. Reverse a String

**Code:**
```python
s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev

print("Reversed string:", rev)
```

**Input:**
```text
Python
```
**Output:**
```text
Reversed string: nohtyP
```

## Q10. Check Whether a String Is Palindrome

**Code:**
```python
s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome String")
else:
    print("Not Palindrome")
```

**Input:**
```text
madam
```
**Output:**
```text
Palindrome String
```

## Q11. Find the Largest and Smallest Element in an Array

**Code:**
```python
arr = [10, 20, 5, 40, 15]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
```

**Input:**
```text
[10, 20, 5, 40, 15]
```
**Output:**
```text
Largest: 40
Smallest: 5
```

## Q12. Find the Second-Largest Element in an Array

**Code:**
```python
arr = [10, 20, 40, 30, 50]

unique = list(set(arr))
unique.sort()

print("Second largest:", unique[-2])
```

**Input:**
```text
[10, 20, 40, 30, 50]
```
**Output:**
```text
Second largest: 40
```

## Q13. Sort an Array

**Code:**
```python
arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Sorted array:", arr)
```

**Input:**
```text
[5, 2, 8, 1, 3]
```
**Output:**
```text
Sorted array: [1, 2, 3, 5, 8]
```

## Q14. Find Duplicate Elements in an Array

**Code:**
```python
arr = [1, 2, 3, 2, 4, 5, 3]
duplicate = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print("Duplicate elements:", duplicate)
```

**Input:**
```text
[1, 2, 3, 2, 4, 5, 3]
```
**Output:**
```text
Duplicate elements: [2, 3]
```

## Q15. Count the Frequency of Each Element in an Array

**Code:**
```python
arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    print(key, "occurs", value, "time(s)")
```

**Input:**
```text
[1, 2, 2, 3, 3, 3, 4]
```
**Output:**
```text
1 occurs 1 time(s)
2 occurs 2 time(s)
3 occurs 3 time(s)
4 occurs 1 time(s)
```

---

### Important Interview Preparation Notes

- Q1–Q8: Number-based programs.
- Q9–Q10: String-based programs.
- Q11–Q15: Array/List-based programs.

**Practice Target:** Try writing all 15 programs without looking at the solutions. Understand the logic instead of memorizing the code.
