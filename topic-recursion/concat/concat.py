
# Programmer:       Cheng, Jeff
# Last Modified:    07-11-24 09:56PM
# Problem:          Concat Recursion

def concat(strings):
    if len(strings) == 0:
        return ""
    else:
        #   head = strings[0]
        #   tail = strings[1:]
        return strings[0] + concat(strings[1:])

strings = []
while True:
    try:
        addThisString = input("Enter strings to concat, one at a time [enter nothing to quit]: ")
        if addThisString == '':
            break
        strings.append(addThisString)
    except ValueError:
        print("Please enter a string.")
    except:
        print("An unknown error has taken place.")

print("Concating strings = " + concat(strings))