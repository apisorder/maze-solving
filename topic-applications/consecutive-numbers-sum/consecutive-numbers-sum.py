
#   Programmer:     Cheng, Jeff
#   Last Modified:  05-19-2024 03:48PM
#   Problem:        561. Array Partition

#   Given an integer array nums of 2n integers, group these integers into n pairs 
#   (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. 

#   Return the maximized sum.

#   Example 1:
#   Input: nums = [1,4,3,2]
#   Output: 4
#   Explanation: All possible pairings (ignoring the ordering of elements) are:
#   1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
#   2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
#   3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
#   So the maximum possible sum is 4.

#   Example 2:
#   Input: nums = [6,2,6,5,1,2]
#   Output: 9
#   Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

import math

class Solution:
    def consecutiveNumbersSum(self, n):
        answer = 1

        for k in range(2, int(math.sqrt(2*n))+1):
            if (n-(k-1)*k//2)%k == 0:
                answer += 1

        return answer