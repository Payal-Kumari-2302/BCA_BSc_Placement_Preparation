'''5. Write code to Check if two strings are Anagram or not
Two strings are called anagrams if they contain the same characters in the same frequencies, but possibly in different orders.

This code checks whether two given strings are anagrams of each other.
Example: Are “listen” and “silent” anagrams?
Sort both:
“listen” → “eilnst”

“silent” → “eilnst”
Both are the same, so “listen” and “silent” are anagrams.'''

#Method_1(direct_Method)
s1 = "silent"
s2 = "listen"
if sorted(s1) == sorted(s2):
       print("Anagram string")
else:
    print("Not Anagram String")

 
#Output
Anagram string


#Method_2(User input method)
s1 = input("Enter 1st number:-> ")
s2 = input("Enter 2nd number:-> ")
if sorted(s1) == sorted(s2):
    print("Anagram string")
else:
    print("Not Anagram String")


#Output
Enter 1st number:-> listen
Enter 2nd number:-> silent
Anagram string



