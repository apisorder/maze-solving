
# Programmer:       Cheng, Jeff
# Last Modified:    07-19-24 06:45PM
# Problem:          Zig Zag

import time, sys

#   number of spaces to indent
indent = 0

#   direction of indentation
indentIncreasing = True

#   the main program loop
try:

    while True:
        print(' ' * indent, end="")
        print('*' * indent)

        #   pause for 0.1 sec
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1

            if indent == 65:
                indentIncreasing = False

        else:
            indent -= 1

            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()