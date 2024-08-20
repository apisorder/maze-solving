
#   Programmer:       Cheng, Jeff
#   Last Modified:    08-17-24 08:41PM
#   Problem:          Dictionary vs List

#   While the order of items matters for determining whether two lists are the same,
#   it does not matter in what order the key-value pairs are typed in a diciontary.

import pprint

spam = ['cats', 'dogs', 'moose']
print("spam = " + str(spam))
bacon = ['dogs', 'moose', 'cats']
print("bacon = " + str(bacon))
print()

print("Is spam the same as bacon : " + str(spam == bacon))
print()

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
print('eggs = ' + str(eggs))
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print('ham = ' + str(ham))
print()

print("Is eggs the same as ham : " + str(eggs == ham))
print()

#   Because dictionaries are not ordered, they cazn't be sliced like lists.

#   Though dictionaries are not ordered, the fact that you can have arbitrary values
#   for the keys allows you to organize your data in powerful ways.

#   Say you wanted your program to store data about your friends' birthdays.
#   You can use a dictionary with the names as keys and the birthdays azs values.
birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print("All birthdays = " + str(birthdays))
    print('Enter a name : (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is th birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday : ')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

#   Notice that the values in the dict_items value returned by the itens() method
#   are tuples of the key and value.
#   If you want a true list form one of these methods, passs its list-like return value
#   to the list() function.

spam = {'color': 'red', 'age': 42}
print("Spam = " + str(spam))
print()
print("Printing spam.values()....")
for v in spam.values():
    print(v)
print("Printing spam.values() in a list....")
print(list(spam.values()))

print()
print("Printing spam.keys()....")
for k in spam.keys():
    print(k)
print("Printing spam.keys() in a list....")
print(list(spam.keys()))

print()
print("Printing spam.items()....")
for i in spam.items():
    print(i)
print("Printing spam.items() in a list....")
print(list(spam.items()))

#   You can also use the multiple assignment trick in a for loop to assign the key
#   and the value to separate variables.
print("Using the multiple assignment trick in a for loop to print the items()....")
for k, v in spam.items():
    print("Key: " + k + " Values: " + str(v))

#   checking whether a key or a value exists in a dictionary
print("checking whether a key or a vlaue exists in a dictionary with 'in' and 'not in'....")
spam = {'name': 'Zophie', 'age': 7}
print("spam = " + str(spam))
print("'name' in spam.keys() : " + str('name' in spam.keys()))
print("'Zophie' in spam.values() : " + str('Zophie' in spam.values()))
print("'color' not spam.keys() : " + str('color' in spam.keys()))
print("'color' not in spam.keys() : " + str('color' not in spam.keys()))
#   notice how 'color' in spam is essentially a shorter version of writing
#   'color' in spam.keys()
#   This si always the case: if you ever want to check whether a value is
#   (or isn't) a key in the dictionary, you can simply use the in (or not in)
#   keyword with the dictionary value itself
print("'color' in spam (spam.keys() shortened) : " + str('color' in spam))

#   it's tedious to check whether a key exists in a dictionary before accessing that
#   key's value.  Fortunately, dictionaries hazve a get() mehtod that takes two arguments:
#   the key of the value to retrieve and a fallback value to return if that key does not exist
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

#   the setdefault method
#   You will often have to set a value in a dictionary for a certain key only if that key
#   does not already have a value.
spam = {'name': 'Pooka', 'age': 5}
print("spam = " + str(spam))
# if 'color' not in spam:
#     spam['color'] = 'black' 

#   the first time setdefault() is called, the dictionary in spam changes to
#   {'color': 'black', 'age': 5, 'name': 'Pooka'}. The method returns the value 'black'
#   because this is now the value set for the key 'color.'
#   When spam.setdefault('color', 'white') is called next, the value for that key is not
#   changed to 'white', because spam already hazs a key named 'color'.
 
#   The setdefault() method is a nice shortcut to ensure that a key exists. 
print("spam.setdefault('color', 'black') : " + str(spam.setdefault('color', 'black')))
print("spam.setdefault('color', 'white') : " + str(spam.setdefault('color', 'white')))

#   a short program that counts the number of occurrences of each letter in a string.
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

#   The setdefault() method call ensures that the key is in the count dictionary(
#   with a default vlaue of 0) so the program does not throw a KeyError when
#   count[character] = count[character] + 1 is executed.
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

#   pretty printing
#   If you import the pprint module into your programs, you'll have access to the pprint()
#   and pformat() functions that will "pretty print" a dictioanry's values.
#   This is helpful when you want a cleaned display of the item in a dictionary than what
#   pritn() provides.
#   The pprint.pprint() function is especially helpful when the dictionary itself contains
#   nested lists or dictionaries.
print("Using pprint.pprint()....")
pprint.pprint(count)

#   If you want to obain the prettified text as a string value instead of displaying it
#   on the screen, call pprint.pformat() instead.

print("Using print(pprint.pformat()....)")
print(pprint.pformat(count))

theBoard = {
    'top-L': ' ', 
    'top-M': ' ',
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' '
    }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space? ')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

#   nested dictionaries and lists
#   modelling a tic-tac-toe board was fairly simple: the board needed only a single
#   dictionary value with nine key-value pairs.

#   As you model more complicated things, you may find that you need dictionaries and lists
#   that contain other dictionaries and lists.

#   Lists are useful to contain an ordered series of values, and dictionaries are useful
#   for assocating keys with values.

#   A program that uses a dictionary that contains other dictionaries of what items guests
#   are bringing to a picnic.

allGuests = {
        'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}
}

#   Inside the totalBrought() function, the for loop iterates over the key-value
#   pairs in guests.  Inside the loop, the string of the guest's nazme is assigned
#   to k, and the dictionary of picnic items they're bringing is assigned to v.

#   If the item parameter exists as a key in this dictionary, its value (the quantity)
#   is added to numBrought.

#   If it does not exist as a key, the get() method returns 0 to be added to numBrought
def totalBrought(guests, item):
    numBrought = 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

#   This may seem like such a simple thing to model that you wouldn't need to bother with
#   writing a program to do it.

#   But realize that this same totalBrought() function could easily handle a dictionary that
#   contains thousands of guests, each bringing thousands of different picnic items.

#   Then, having this information in a data structure along with the totalBrought() function
#   would save you a lot of time!
print('Number of things being brought:')
print(' - Apples              ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes               ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches      ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apples Pies         ' + str(totalBrought(allGuests, 'apple pies')))

#   Lists and dictionaries are vlaues that can contain multiple values, including other lists
#   and dictionaries.

#   Dictionaries are useful because you can map one item (the key) to another (the vlaue),
#   as opposed to lists, which simply contain a series of values in order.

#   Values inside a dictionary are accessed using square brackets just as with lists.

#   Instead of an integer index, dictionaries can have keys of a variety of data types:
#   integers, floats, strings, or tuples.