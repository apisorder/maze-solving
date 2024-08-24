
# Programmer:     Cheng, Jeff
# Last Modified:  05-31-2024 08:48AM
# Problem:        Python Tutorial 1

import sys

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

print("maximum size for integer = sys.maxsize : ", sys.maxsize)
print("maximum size for floating pointing numbers = sys.float_info.max : ", sys.float_info.max)
print("sys.float_info.max", sys.float_info.max)

f1 = 1.1111111111111111
f2 = 1.1111111111111111
print("Floating point error : where f1 = ", f1, "and f2 = ", f2, " f1 + f2 = ", f1 + f2)

can_vote = True

#   convert a UniCode character to a string; there are no character types in Python
print("chr(number) => correspondng character : chr(97) = ", chr(97), )
print("i.e. type(chr(97)) = ", type(chr(97)))

#   convert a character to a UniCode character; there are no character types in Python
print("ord(character) => corresponding number : ord('a') =  ", ord('a')) 
print("i.e. type(ord('a')) = ", type(ord('a')))