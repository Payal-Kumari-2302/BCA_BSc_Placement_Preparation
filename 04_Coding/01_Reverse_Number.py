'''1. Write a code to reverse a number
To reverse a number, you need to take the digits of the number and rearrange them in the opposite order.

Start by converting the number to a string, reverse that string, and then convert it back to an integer. This will give you the reversed version of the original number.
Example: If the number is 908701, take digits from last → 1, 0, 7, 8, 0, 9 → and make it 107809.'''


#Direct Method

n = 908701
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 +digit
    n = n //10
print(rev)


#Output
107809


#Method_2(User input)

n = int(input("Enter any number:->"))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 +digit
    n = n // 10
print(f"The reverse number is: {rev}")


#Output
Enter any number:-> 908701
The reverse number is: 107809
