'''3. Write code of Greatest Common Divisor 
This problem asks to find the Greatest Common Divisor (GCD) of two given numbers. The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

The Euclidean algorithm is a popular method for efficiently computing the GCD.
Example: Find GCD of 36 and 60:
The common divisors of 36 and 60 are 1, 2, 3, 4, 6, 9, 12, 18, 36 and 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.
The largest common divisor is 12.'''

#Method_1(Direct Method)
a = 12
b = 36
gcd = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f"GCD of two number is: {gcd} ")


#output
GCD of two number is: 12 


#Method_2(User input)
a = int(input("Enter 1st number:-> "))
b = int(input("Enter 2nd number:-> "))
gcd = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f"GCD of two number is: {gcd} ")


#output
Enter 1st number:-> 12
Enter 2nd number:-> 36
GCD of two number is: 12 

