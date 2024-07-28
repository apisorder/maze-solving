
# Programmer:       Cheng, Jeff
# Last Modified:    06-30-24 04:49PM
# Problem:          Recursive Fibonacci

def recursiveFibonacci(nth_number):

    print('fibonacci called(%s)' % (nth_number))

    if nth_number == 1 or nth_number == 2:
        print('Call to fibonacci(%s) returning 1' % (nth_number))
        return 1
    else:
        print('Calling fibonacci(%s) and fibonacci(%s)' % (nth_number-1, nth_number-2))

        result = recursiveFibonacci(nth_number-1) + recursiveFibonacci(nth_number-2)

        print('Call to fibonacci(%s) returning %s' % (nth_number, result))

        return result

print(recursiveFibonacci(10))