
# Programmer:     Cheng, Jeff
# Last Modified:  07-08-2024 10:07PM
# Problem:        Python Tutorial 6

#   we should write code that anticipates bad things the user may enter to cause a crash 
#   and eliminate them.
#   However, sometimes the user may try to access a database that doesn't exist
#   or simply refuse to follow instructions.
#   And that is where exception handling comes in.
#   Through exception handling, we are going to be able to catch an error that would
#   normally crash our program, and give the user the opportunity to do the right thing.

#   We are asking the user to enter a number

import random
from decimal import Decimal as D
from decimal import *

while True:
    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("You didn't enter a number : ")
    except:
        print("An unkonwn error has occurred : ")
    
print("Thank you for entering a number")

#   guess a number between 1 and 10
#   emulate a do-while loop 

secret_number = random.randint(1, 11)
print("secret_number = ", secret_number)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10 : "))
        #   if guess == secret_number:
        #       print("You guessed it")
        #       break
        if guess <= 10 and guess >= 1 and guess == secret_number:
                break
    except ValueError:
        print("You didn't enter a number : ")
    except guess > 10 or guess < 1:
        print("You did not enter a number between 1 and 10 : ")
    except:
        print("Your guess is incorrect : ")

print("You guessed it.")

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
print("Sum =", sum)

sum_1 = Decimal(0)
sum_1 += Decimal("0.0111111111111111")
sum_1 += Decimal("0.0111111111111111")
print("Sum = ", sum_1)
sum_1 -= Decimal("0.0222222222222222")
print("Sum = ", sum_1)
