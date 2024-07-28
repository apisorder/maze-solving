
# Programmer:       Cheng, Jeff
# Last Modified:    07-02-24 06:09PM
# Problem:          Factorial Emulate Recursion

#   explict call stack storing framed objects
callStack = []
#   CALL the FACTORIAL function
callStack.append({'returnAddress': 'start', 'number': 3})
returnValue = None

while len(callStack) > 0:
    #   body of the FACTORIAL function

    #   set the number parameter
    number = callStack[-1]['number']
    returnAddress = callStack[-1]['returnAddress']

    if returnAddress == 'start':
        if number == 1:
            #   base case
            returnValue = 1
            #   RETURN from FUNCTION CALL
            
            callStack.pop()

            continue
        else:
            #   recursive case
            callStack[-1]['returnAddress'] = 'after recursive call'

            #   CALL the FACTORIAL FUNCTION
            callStack.append({'returnAddress' : 'start', 'number' : number-1})

            continue
    elif returnAddress == 'after recursive call':

        returnValue = number * returnValue
        #   RETURN FROM FUNCTION CALL

        callStack.pop()
        continue

print(returnValue)
