
#   Programmer:     Cheng, Jeff
#   Last Modified:  07-26-2024 09:33PM
#   Problem:        1071. Greatest Common Divisor of Strings

#   For two strings s and t, we say "t divides s" if and only if 
#   s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

#   Given two strings str1 and str2, return the largest string x such that 
#   x divides both str1 and str2.

#   Example 1:
#   Input: str1 = "ABCABC", str2 = "ABC"
#   Output: "ABC"

#   Example 2:
#   Input: str1 = "ABABAB", str2 = "ABAB"
#   Output: "AB"

#   Example 3:
#   Input: str1 = "LEET", str2 = "CODE"
#   Output: ""

class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        #   we know str1 >= str2
        len1, len2 = len(str1), len(str2)

        while len2:
            len1, len2 = len2, len1 % len2

        return str1[:len1]
