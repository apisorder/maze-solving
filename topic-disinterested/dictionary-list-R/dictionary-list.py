
#   Programmer:       Cheng, Jeff
#   Last Modified:    08-17-24 08:41PM
#   Problem:          Dictionary vs List

#   For list comparisons, the order of items matter for determining whether two lists
#   are the same; however, for dictionary comparisons, the order of key-value pairs matter not.

import pprint

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
print('eggs = ' + str(eggs))
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print('ham = ' + str(ham))
print()

print("Is eggs the same as ham, despite different insertion order of same key-value pairs : " + str(eggs == ham))
print()

#   Because dictionaries are not ordered, they can't be sliced like lists.

#   A program for assocating names with birthdays, with no error checking
birthdays = {}

while True:

    #   print all available data
    print("All recorded birthdays = " + str(birthdays))
    
    #   prompt user for input
    print("Enter a name: (blank to quit)")
    name = input()

    #   blank to exit
    if name == '':
        break
    
    #   if name is among the keys of birthdays dictionary
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    #   otherwise, add new data
    else:
        print("I don't have birthday information for " + name)
        print("What is their birthday? ")
        birthday = input()

        #   update dictionary
        birthdays[name] = birthday

        #   acknowledge the update
        print("Birthday database updated.")

#   dictionary items() method returns tuples, not a true list




#   Dictionaries have a get() mehtod that takes two arguments:  the key of the value to retrieve,
#   and a fallback value to return if that key does not exist
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
print('I am bringing ' + str(picnicItems.get('apple pies', 0)) + ' apple pies.')

#   the setdefault method
#   You will often have to set a value in a dictionary for a certain key only if that key
#   does not already have a value.
spam = {'name': 'Pooka', 'age': 5}
print("spam = " + str(spam))

# if 'color' not in spam:
#     spam['color'] = 'black' 
#   The setdefault() method is a nice shortcut to ensure that a key exists. 

#   a short program that counts the number of occurrences of each letter in a string.
message = 'This is the default message.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)

#   pretty printing
print("Using pprint.pprint()....")
pprint.pprint(count)

print("Using print(pprint.pformat()....)")
print(pprint.pformat(count))

#   a simply not-error-checking Tic Tac Toe program

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
#   prompt the user 9 times for each of the 9 squares
for i in range(9):
    printBoard(theBoard)

    print('Turn for ' + turn + '. Move on which space? ')
    move = input()
    theBoard[move] = turn
    
    #   alternate turns
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

#   A program that uses a dictionary that contains other dictionaries of what items guests
#   are bringing to a picnic.

allGuests = {
        'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}
}

#   Inside the totalBrought() function, the for loop iterates over the key-value
#   pairs in guests.  Inside the loop, the string of the guest's name is assigned
#   to k, and the dictionary of picnic items they're bringing is assigned to v.

#   If the item parameter exists as a key in this dictionary, its value (the quantity)
#   is added to numBrought.

#   If it does not exist as a key, the get() method returns 0 to be added to numBrought
def totalBrought(guests, item):
    numBrought = 0

    for guest, belongings in guests.items():
        numBrought = numBrought + belongings.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples              ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes               ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches      ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apples Pies         ' + str(totalBrought(allGuests, 'apple pies')))