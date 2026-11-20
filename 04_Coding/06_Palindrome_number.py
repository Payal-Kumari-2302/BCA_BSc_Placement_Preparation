'''6. Write code Check if the given string is Palindrome or not
A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

This code checks if a given string is a palindrome.
Example for a palindrome:
“madam” — reads the same backward as forward'''

#Method_1(Direct method)
s1 = "madam"
s2 = s1[::-1]
if s1 == s2:
    print("Palindrome String")
else:
    print("Not Palindrome string")

#Output
Palindrome Stringmad


#Method_2(User input)
s1 = input(" Enter any string:-> ")
s2 = s1[::-1]
if s1 == s2:
    print("Palindrome String")
else:
    print("Not Palindrome string")


#Output
Enter any string:-> madam
Palindrome String
