
#   Programmer:     Cheng, Jeff
#   Last Modified:  05-24-2024 03:24PM
#   Problem:        233. Number of Digit Ones

#   Given an integer n, count the total number of digit 1 appearing in 
#   all non-negative integers less than or equal to n.

#   Example 1:
#   Input: n = 13
#   Output: 6

#   Example 2:
#   Input: n = 0
#   Output: 0

class Solution:
    def countDigitOne(self, n):
        multi = 1
        numOfOnes = 0
    
        while multi <= n:
            numOfOnes += (n//multi + 8)//10 * multi + (n//multi%10==1)*(n%multi+1)
            multi *= 10

        return numOfOnes