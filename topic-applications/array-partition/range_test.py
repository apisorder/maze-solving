
#   Programmer:     Cheng, Jeff
#   Last Modified:  12-31-2024 11:21AM
#   Problem:        The Range Function
#   References:     https://www.geeksforgeeks.org/python-range-function/
number_to_start = 5
number_to_end_but_excluded = 20
step_aka_stride = 7

#   Incrementing the range using a positive step 
for i in range(number_to_start, number_to_end_but_excluded, step_aka_stride):
    #   to prevent each number being printed on a new line
    print(i, end=" ")
#   to end the line
print()
#   5 12 19

#   Decrementing a range using a negative step
#
#   Note how the results is different from 
#   for i in range(number_to_start, number_to_end_but_excluded, step_aka_stride):
for j in range(number_to_end_but_excluded, number_to_start, -step_aka_stride):
    print(j, end= " ")
print()
#   20 13 6

#   Accessing range() with an index value
#
#   A sequence of numbers is returned by the range() function as 
#   its object that can be accessed by its index value. 
#   
#   Both positive and negative indexing is supported by its object.
ranged_numbers = range(10)[0]
print("First element:", ranged_numbers)

ranged_numbers = range(10)[-1]
print("\nLast element:", ranged_numbers)

ranged_numbers = range(10)[4]
print("\nFifth element:", ranged_numbers)

#   range() function with list in Python
fruits = ["apple", "banana", "cherry", "date"]

for i in range(len(fruits)):
    print(fruits[i])

#   The step value must not be zero. If a step is zero, Python raises 
#   a ValueError exception.

#   How to generate a list using range():

#   list converts a range object into a list
numbers = list(range(number_to_start, number_to_end_but_excluded, step_aka_stride))
print(numbers)