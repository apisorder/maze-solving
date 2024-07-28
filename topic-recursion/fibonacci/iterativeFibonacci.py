
# Programmer:       Cheng, Jeff
# Last Modified:    06-30-24 04:42PM
# Problem:          Iterative Fibonacci

def iterativeFibonacci(nth_number):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))

    for i in range(2, nth_number+1):
        #   get the next Fibonacci number
        a, b = b, a+b
        print('a = %s, b = %s' % (a, b))

    return a

print(iterativeFibonacci(10))