'''7. Write code to Calculate frequency of characters in a string
This problem asks to calculate the frequency of each character in a given string.

The goal is to determine how many times each character appears in the string.
Example for string “hello”:
‘h’ appears 1 time
‘e’ appears 1 time
‘l’ appears 2 times
‘o’ appears 1 time'''


#Method_1
s = input("Enter any character:->")
freq = {}
for i in s:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
print("Frequecny of character:->")
for i in freq:
    print(i," ", freq[i])

#output

Enter any character:->hello
Frequecny of character:->
h   1
e   1
l   2
o   1


#Method_2
s = input("Enter any string:-> ")
character = input("Enter character: ")
freq = 0
freq = s.count(character)
print(str(freq)+'is the frequency of given character')

#output
Enter any string:-> hello
Enter character: h
1 is the frequency of given character
