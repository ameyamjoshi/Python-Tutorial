# print('"Isn\'t," they said.') # \ skips the special character '

# s = 'First line.\nSecond line.' #\n is new line
# print(s)

#print('C:\some\name') # here \n means newline!

#print(r'C:\some\name')  # note the r before the quote

# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
#Explanation
"""
String literals can span multiple lines. One way is using triple-quotes. End of lines are automatically included
in the string, but it’s possible to prevent this by adding a \ at the end of the line. note that the initial newline is not included
"""

#Strings can be concatenated (glued together) with the + operator, and repeated with *:

#print(3 * 'un' + 'ium')

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

#print('Py' 'thon')

#This only works with two literals though, not with variables or expressions:

# prefix = 'Py'
# print(prefix 'thon')  # can't concatenate a variable and a string literal

#If you want to concatenate variables or a variable and a literal, use +:

# prefix = 'Py'
# print(prefix + 'thon')

#Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is
# simply a string of size one:

# word = 'Python'
# print(word[0])  # character in position 0
# print(word[5])  # character in position 5

#Indices may also be negative numbers, to start counting from the right:
# word='Python'
# print(word[-1])  # last character
# print(word[-2])  # second-last character

#In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters,
# slicing allows you to obtain substring:

# word='Python'
# print(word[0:2]) # characters from position 0 (included) to 2 (excluded)

#Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:

# word='Python'
# print(word[:2] + word[2:])

x=int(input())
#print(x)
print(x*2)