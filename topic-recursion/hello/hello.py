
# Programmer:       Cheng, Jeff
# Last Modified:    07-03-24 07:06PM
# Problem:          Hello Using Loop and Recursive Function

print('Code in a loop : ')
i = 0
while i < 5:
    print(i, 'Hello, world!')
    i = i + 1

print('Code in a function : ')
def hello(i=0):
    print(i, 'Hello, world!')
    i = i + 1

    if i < 5:
        hello(i)
    else:
        return

hello()