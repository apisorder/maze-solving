
# Programmer:       Cheng, Jeff
# Last Modified:    07-04-24 09:51PM
# Problem:          Exponent Calculation Iteration and Recursion

def exponentByIteration(a, n):
    if n <= 0:
        return 1
    
    result = 1
    for i in range(n):
        result *= a

    return result

print(exponentByIteration(3, 6))
print(exponentByIteration(10, 3))
print(exponentByIteration(17, 10))

def exponentByRecursion(a, n):
    if n <= 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        result = exponentByRecursion(a, n//2)
        return result * result
    elif n % 2 == 1:
        result = exponentByRecursion(a, n//2)
        return result * result * a

print(exponentByRecursion(3, 6))
print(exponentByRecursion(10, 3))
print(exponentByRecursion(17, 10))

def exponentByPowerRule(a, n):
    if n <= 0:
        return a

    opStack = []
    while n > 1:
        if n % 2 == 0:
            opStack.append('square')
            n //= 2
        elif n % 2 == 1:
            opStack.append('multiply')
            n -= 1

    result = a
    while opStack:
        op = opStack.pop()

        if op == 'multiply':
            result *= a
        elif op == 'square':
            result *= result
        
    return result

print(exponentByPowerRule(3, 6))
print(exponentByPowerRule(10, 3))
print(exponentByPowerRule(17, 10))