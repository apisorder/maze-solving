
# Programmer:       Cheng, Jeff
# Last Modified:    07-18-24 08:38PM
# Problem:          Truthy and Falsey Values

name = ''

while not name:
#   while not name != '':
    print(' Enter your name : ')
    name = input()

print( ' How many guests would you have? ')
numOfGuests = int(input())

if numOfGuests:
#   numOfGuests != 0
    print(' Be sure to have enough room for all your guests. ')

print('Done')