# Programmer:       Cheng, Jeff
# Last Modified:    06-29-24 04:56PM
# Problem:          Iterative Factorial

#   iterative factorial = 1 * 2 * ... * number-1 * number

def iterativeFactorial(number):
    product = 1
    
    for i in range(1, number+1):
        product *= i

    return product

print("Factorial(5) = ", iterativeFactorial(5))