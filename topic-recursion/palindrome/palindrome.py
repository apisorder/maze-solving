
# Programmer:       Cheng, Jeff
# Last Modified:    07-12-24 10:07PM
# Problem:          Palindrome

def palindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        #   head = theString[0]
        #   tail = theString[-1]
        #   middle = theString[1:-1]
        #   note how the slicing ends just before -1
        return theString[0] == theString[-1] and palindrome(theString[1:-1])
    
text = 'racecar'
print(text + ' is a palindrome : ' + str(palindrome(text)))
text = 'amanaplanacanalpanama'
print(text + ' is a palindrome : ' + str(palindrome(text)))
text = 'tacocat'
print(text + ' is a palindrome : ' + str(palindrome(text)))
text = 'zophie'
print(text + ' is a palindrome : ' + str(palindrome(text)))