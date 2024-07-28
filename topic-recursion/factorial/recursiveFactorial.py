# Programmer:       Cheng, Jeff
# Last Modified:    06-29-24 04:56PM
# Problem:          Recursive Factorial

def recursiveFactorial(number):
    if number == 1:
        return 1
    
    else:
        return number * recursiveFactorial(number-1)
    
print("Factorial(5) = ", recursiveFactorial(5))