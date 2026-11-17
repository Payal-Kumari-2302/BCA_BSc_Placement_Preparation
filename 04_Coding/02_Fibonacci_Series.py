'''2. Write the code to find the Fibonacci series upto the nth term.
This problem asks to generate the Fibonacci sequence up to the nth term. In this sequence, each number is the sum of the two preceding ones, starting from 0 and 1.

The goal is to calculate and display all Fibonacci numbers from the 0th to the nth term.
Example for n = 10:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34   
(Writing: Start with 0 and 1 → 0+1=1 → 1+1=2 → 1+2=3 → 2+3=5 → and so on.)'''

#Method_1(Direct Method)

n = 10
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c


#Output
0 1 1 2 3 5 8 13 21 34

# Method_2(User input)

n = int(input("Enter any number:-> "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c


#Output
Enter any number:-> 10
0 1 1 2 3 5 8 13 21 34 
