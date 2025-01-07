
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-06-2025 05:46PM
#   Problem:        829. Consecutive Numbers Sum
#   Reference:      https://leetcode.com/problems/consecutive-numbers-sum/solutions/129015/5-lines-c-solution-with-detailed-mathematical-explanation/
#   Complexity:     time -> O(sqrt(n))
#                   space -> O(1)
#
#   Given an integer n, return the number of ways you can write n as the sum 
#   of consecutive positive integers.
#
#   Example 1:
#   
#   Input: n = 5
#   Output: 2
#
#   Explanation: 
#   5 = 5
#   5 = 2 + 3
#
#   Example 2:
#
#   Input: n = 9
#   Output: 3
#   
#   Explanation: 
#   9 = 4 + 5 
#   9 = 2 + 3 + 4 
#   9 = 9
#
#   Example 3:
#
#   Input: n = 15
#   Output: 4
#
#   Explanation: 
#   15 = 8 + 7 
#   15 = 4 + 5 + 6 
#   15 = 1 + 2 + 3 + 4 + 5
#   15 = 15
# 
#   Constraints:
#   1 <= n <= 109

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        #   N = x + x+1 + x+2 + x+3 + ... + x+k-1
        #   N = kx + k(k-1)/2
        #   kx = N - k(k-1)/2
        #   -> if N - k(k-1)/2 is a multiple of k
        #   another x exists, i.e. another solution
        #   since kx > 0, N - k(k-1)/2 > 0
        #   N > k(k-1)/2
        #   2N > k(k-1)
        #   -> k < sqrt(2n)

        import math 
        num_of_solutions = 1

        #   note how we must cast to int, and how we must add 1
        for k in range(2, int(math.sqrt(2*n))+1):
            if ((n - k*(k-1)//2) % k) == 0:
                num_of_solutions += 1

        return num_of_solutions