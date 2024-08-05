
# Programmer:       Cheng, Jeff
# Last Modified:    07-19-24 06:45PM
# Problem:          Zig Zag

import time, sys

#   how many spaces to indent
indent = 0
#   whether the indentation is increasing or not
indentIncreasing = True

try:
    #   the main program loop
    while True:
        print( ' ' * indent, end='' )
        print('*' * indent)
        # print( '********' )
        #   pause for 1/10 of a second
        time.sleep(0.1)

        #   increase the number of spaces
        if indentIncreasing:
            indent += 1

            #   change direction
            if indent == 20:
                indentIncreasing = False

        #   decrease the number of spaces
        else:
            indent -= 1
            
            #   change direction
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
            