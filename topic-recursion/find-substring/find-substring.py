
# Programmer:       Cheng, Jeff
# Last Modified:    07-03-24 07:31PM
# Problem:          Find Substring Iterative and Recursive

def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i : i + len(needle)] == needle:
            return i
        i = i + 1
    return -1

def findSubstringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1
    if haystack[i : i + len(needle)] == needle:
        return i
    else:
        return findSubstringRecursive(needle, haystack, i+1)

print(findSubstringIterative('cat', 'My cat Zophie'))
print(findSubstringRecursive('cat', 'My cat Zophie'))