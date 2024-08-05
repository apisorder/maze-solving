
# Programmer:       Cheng, Jeff
# Last Modified:    07-03-24 07:31PM
# Problem:          Find Substring

def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        #   notice where the slicing ends: i + len(needle)
        if haystack[i : i + len(needle)] == needle:
            return i
        i = i + 1
    return -1

# def findSubstringIterativeII(needle, haystack):
#     for i in range(len(haystack)):
#         if haystack[i:i+len(needle)] == needle:
#             return i
#     return -1

def findSubstringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1
    if haystack[i : i + len(needle)] == needle:
        return i
    else:
        return findSubstringRecursive(needle, haystack, i+1)

print(findSubstringIterative('cat', 'My cat Zophie'))
print(findSubstringIterative('cat', 'My Kat Zophie'))
print(findSubstringIterativeII('cat', 'My cat Zophie'))
print(findSubstringIterativeII('cat', 'My Kat Zophie'))
print(findSubstringRecursive('cat', 'My cat Zophie'))
print(findSubstringRecursive('cat', 'My Kat Zophie'))