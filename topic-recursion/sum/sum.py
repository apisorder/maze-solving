
# Programmer:       Cheng, Jeff
# Last Modified:    07-11-24 09:48PM
# Problem:          Sum Recursion

def sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        #   head = numbers[0]
        #   tail = numbers[1:]
        return numbers[0] + sum(numbers[1:])


while True:
    try:
        numberToSumUpTo = int(input("Enter a number to sum up to, from 1 (i.e. 5, sums 1+2+3+4+5) [0 to quit]: "))
        if numberToSumUpTo == 0:
            break
        #   note that it accepts an array of numbers as an input, hence starting at 1, and ends at sumUpTo+1-1
        print("Sum  = ", sum(range(1, numberToSumUpTo+1)))

    except ValueError:
        print("Please enter a number.")
    except:
        print("An unknown error has taken place.")