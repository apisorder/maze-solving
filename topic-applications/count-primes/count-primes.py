
#   Programmer:     Cheng, Jeff
#   Last Modified:  05-24-2024 11:20AM
#   Problem:        204. Count Primes

#   Given an integer n, return the number of prime numbers that are strictly less than n.

#   Example 1:
#   Input: n = 10
#   Output: 4
#   Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

#   Example 2:
#   Input: n = 0
#   Output: 0

#   Example 3:
#   Input: n = 1
#   Output: 0

import math

class Solution:
    def countPrimes(self, n):

        if n < 2:
            return 0

        allPrimes = [1] * n
        allPrimes[0] = allPrimes[1] = 0
        
        for i in range(2, int(math.sqrt(n))+1):
            if allPrimes[i] == 1:
                allPrimes[i*i : n : i] = [0] * ((n-1-i*i)//i+1)

        return sum(allPrimes)
