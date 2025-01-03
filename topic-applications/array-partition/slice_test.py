
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-02-2025 15:43PM
#   Problem:        The Slice Function
#   References:     https://www.geeksforgeeks.org/python-slice-function/
#                   https://stackoverflow.com/questions/509211/how-slicing-in-python-works

#   The key point to remember is that the :stop value represents the first 
#   value that is not in the selected slice. So, the difference between stop 
#   and start is the number of elements selected (if step is 1, the default).

#   a[start:stop]  # items start through stop-1
#   a[start:]      # items start through the rest of the array
#   a[:stop]       # items from the beginning through stop-1
#   a[:]           # a copy of the whole array

#   a[start:stop:step] # start through not past stop, by step

#   The other feature is that start or stop may be a negative number, 
#   which means it counts from the end of the array instead 
#   of the beginning.

#   a[-1]    # last item in the array
#   a[-2:]   # last two items in the array
#   a[:-2]   # everything except the last two items

#   Similarly, step may be a negative number:

#   a[::-1]    # all items in the array, reversed
#   a[1::-1]   # the first two items, reversed
#   a[:-3:-1]  # the last two items, reversed
#   a[-3::-1]  # everything except the last two items,

#   Python is kind to the programmer if there are fewer items than 
#   you ask for. For example, if you ask for a[:-2] and a only contains 
#   one element, you get an empty list instead of an error. 
#   Sometimes you would prefer the error, so you have to be aware 
#   that this may happen.

#   Relationship with the slice object
#   A slice object can represent a slicing operation, i.e.:

#   a[start:stop:step] is equivalent to:
#   a[slice(start, stop, step)]

#   Slice objects also behave slightly differently depending on 
#   the number of arguments, similar to range(), i.e. 
#   both slice(stop) and slice(start, stop[, step]) are supported. 
 
#   To skip specifying a given argument, one might use None, so that 
#   e.g. a[start:] is equivalent to a[slice(start, None)] or 
#   a[::-1] is equivalent to a[slice(None, None, -1)].

#   While the :-based notation is very helpful for simple slicing, 
#   the explicit use of slice() objects simplifies the programmatic 
#   generation of slicing.

#   String slicing
a_string_which_very_next_slice_funcs_call_on_by_default = 'GeeksforGeeks'
slice_obj1 = slice(3)
slice_obj2 = slice(1, 5, 2)

print("String slicing")
print(a_string_which_very_next_slice_funcs_call_on_by_default[slice_obj1])
print(a_string_which_very_next_slice_funcs_call_on_by_default[slice_obj2])

a_list_which_very_next_slice_funcs_call_on_by_default = [1, 2, 3, 4, 5]
slice_obj1 = slice(3)
slice_obj2 = slice(1, 5, 2)

#   List slicing
print("List slicing")
print(a_list_which_very_next_slice_funcs_call_on_by_default[slice_obj1])
print(a_list_which_very_next_slice_funcs_call_on_by_default[slice_obj2])

#   Tuple slicing
a_tuple_which_very_next_slice_funcs_call_on_by_default = (1, 2, 3, 4, 5)
slice_obj1 = slice(3)
slice_obj2 = slice(1, 5, 2)

print("Tuple slicing")
print(a_tuple_which_very_next_slice_funcs_call_on_by_default[slice_obj1])
print(a_tuple_which_very_next_slice_funcs_call_on_by_default[slice_obj2])

#   Negative indexing
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
slice_obj = slice(-2, -6, -1)
print("list slicing:", my_list[slice_obj])


#   Get a sub-string using a negative index with a slice()

my_string = "abcdef"

#   Note: If only one parameter is passed, then the start and step 
#   are considered to be None.
slice_obj = slice(-1)
print("string slicing:", my_string[slice_obj])

#   In the code, slice_obj = slice(-1, -3, -1) creates a slice object 
#   that will slice the tuple starting from the second-to-last element 
#   (index -1), up to (but not including) the fourth-to-last element 
#   (index -3), with a step size of -1. This means that the sliced 
#   tuple will contain the elements [9, 7], in reverse order.
my_tuple = (1, 3, 5, 7, 9)
slice_obj = slice(-1, -3, -1)
print("tuple slicing:", my_tuple[slice_obj])

#   Using indexing syntax for slicing with string

#   We have created a list named slice_str with the value ‘Hello World‘.
#   The first slice is printing the value till the 4 indexes and 
#   the second slice is printing till the 5th index with a hop
#   every 2nd index.

slice_str = 'Hello World'
print(slice_str[0:5]) 
print(slice_str[1:6:2])

#   Using indexing syntax for slicing with list
#   we have created a list named slice_list and we have inserted 
#   these values, ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'], 
#   to our list. The first slice is printing the value till 4 indexes 
#   and the second slice is printing till the 5th index with a hop 
#   of every 2nd index.

slice_list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(slice_list[0:5]) 
print(slice_list[1:6:2])

#   Slicing and modifying a list
#   we have created a list of numbers named slice_numbers which 
#   consists of 5 variables [1,2,3,4,5] in it.Then we are slicing the list 
#   from index 1 to 3 and also modify its value from [1,2,3] to 
#   [10,20,30] and finally, we are printing the slice_numbers list.

slice_numbers = [1, 2, 3, 4, 5]
print("slice_number before slicing and modfication : ",end=' ')
print(slice_numbers) 
slice_numbers[1:4] = [10, 20, 30]
print("slice_number after slicing and modfication : ",end=' ')
print(slice_numbers) 