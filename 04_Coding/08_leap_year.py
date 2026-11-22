'''11. Write to code to check whether a given year is leap year or not.
A leap year is a year that is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

This code checks whether a given year is a leap year based on this rule.
Example:
2020 is a leap year (divisible by 4).
1900 is not a leap year (divisible by 100 but not 400).
2000 is a leap year (divisible by 400).'''

year = int(input("Enter any year:-> "))
if(( year % 400 == 0) or (year % 4 ==0 and year % 100 != 0)):
    print("Leap year")
else:
    print("Not leap year")




#output
Enter any year:-> 2002
Not leap year

Enter any year:-> 2004
leap year
