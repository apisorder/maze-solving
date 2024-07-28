
# Programmer:       Cheng, Jeff
# Last Modified:    07-11-24 09:48PM
# Problem:          Sum Head Tail Recursion

def sumHeadTail(numbers):
    if len(numbers) == 0:
        return 0
    else:
        #   head = numbers[0]
        #   tail = numbers[1:]
        return numbers[0] + sumHeadTail(numbers[1:])


while True:
    try:
        sumUpTo = int(input("Enter a number to sum up to, from 1 (i.e. 5, sums 1+2+3+4+5) [0 to quit]: "))
        if sumUpTo == 0:
            break
        print("Sum  = ", sumHeadTail(range(1, sumUpTo+1)))

    except ValueError:
        print("Please enter a number.")
    except:
        print("An unknown error has taken place.")