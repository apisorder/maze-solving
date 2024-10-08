
# Programmer:       Cheng, Jeff
# Last Modified:    07-12-24 09:50PM
# Problem:          Rev Recursion

def rev(strings):
    if len(strings) == 0:
        return ""
    else:
        #   head = strings[0]
        #   tail = strings[1:]
        return rev(strings[1:]) + strings[0]

strings = []
while True:
    try:
        addThisString = input("Enter the strings to reverse, one at a time [enter nothing to quit]: ")
        if addThisString == '':
            break
        strings.append(addThisString)
    except ValueError:
        print("Please enter a string.")
    except:
        print("An unknown error has taken place.")

print("Reversed strings = " + rev(strings))
print("Reversed string where string = Hello => " +rev("Hello"))