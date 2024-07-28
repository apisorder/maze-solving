
# Programmer:       Cheng, Jeff
# Last Modified:    07-12-24 10:07PM
# Problem:          Palindrome Two Ends

def palindromeTwoEnds(theString):
    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        #   head = theString[0]
        #   tail = theString[-1]
        #   middle = theString[1:-1]
        return theString[0] == theString[-1] and palindromeTwoEnds(theString[1:-1])
    
text = 'racecar'
print(text + ' is a palindrome : ' + str(palindromeTwoEnds(text)))
text = 'amanaplanacanalpanama'
print(text + ' is a palindrome : ' + str(palindromeTwoEnds(text)))
text = 'tacocat'
print(text + ' is a palindrome : ' + str(palindromeTwoEnds(text)))
text = 'zophie'
print(text + ' is a palindrome : ' + str(palindromeTwoEnds(text)))