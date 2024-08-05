
# Programmer:     Cheng, Jeff
# Last Modified:  05-31-2024 08:48AM
# Problem:        Python Tutorial 1

import sys

my_age = 43
my_name = "maze solver"

print("Hello", my_age)

#   This is a one-line comment
'''
This is a multi-line comment
'''

#   'This is a string'
#   "This is a string also"
#   '''This is another string'''
#   \backslash is used to escape (escape sequence) and allows you to use a string within a string
#   \n (newline)
#   \\ (backslash)
#   \' (single quote)
#   \b (backspace)
#   \t (tab)

str_1 = "\"This is a quote\""
print(str_1)

print("sys.maxsize", sys.maxsize)
print("sys.float_info.max", sys.float_info.max)

f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f1, "f1 +", f2, "f2 = ", f3)

can_vote = True

print("Cast type(int(5.4)) = ", type(int(5.4)))

print("Cast2 type(str(5.4)) = ", type(str(5.4)))
#   convert a UniCode character to a string; there are no character types in Python

print("chr(number) => correspondng character")
print("chr(97) = ", chr(97))
print("Cast2 type(str(5.4)) = ", type(str(5.4)))

print("Cast3 type(chr(97)) = ", type(chr(97)))

#   convert a character to a UniCode character; there are no character types in Python
print("ord(character) => corresponding number")
print("ord('a') =  ", ord('a'))
print("Cast3 type(chr(97)) = ", type(chr(97)))

print("Cast4 type(ord('a')) = ", type(ord('a')))

print("Cast5 type(float(2)) = ", type(float(2)))

num_1 = "1"
num_2 = "2"
print("\"1\" + \"2\" = ", (int(num_1)+int(num_2)))