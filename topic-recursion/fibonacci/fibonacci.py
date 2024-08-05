
# Programmer:       Cheng, Jeff
# Last Modified:    06-30-24 04:42PM
# Problem:          Iterative Fibonacci

def iterativeFibonacci(nth_number):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))

    #   range stops at nth_number+1-1 == nth_number
    for i in range(2, nth_number+1):
        #   get the next Fibonacci number
        a, b = b, a+b

        print('a = %s, b = %s' % (a, b))

    return a

def recursiveFibonacci(nth_number):
    if nth_number == 1 or nth_number == 2:
        return 1
    return recursiveFibonacci(nth_number-1) + recursiveFibonacci(nth_number-2)

print("iterativeFibonacci(10) = " + str(iterativeFibonacci(10)))
print("recursiveFibonacci(10) = " + str(recursiveFibonacci(10)))