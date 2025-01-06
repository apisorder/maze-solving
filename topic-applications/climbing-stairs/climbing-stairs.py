
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-05-2025 09:55PM
#   Problem:        70. Climbing Stairs
#
#   You are climbing a staircase. It takes n steps to reach the top.
#
#   Each time you can either climb 1 or 2 steps. In how many distinct ways can 
#   you climb to the top?
#
#   Example 1:
#
#   Input: n = 2
#   Output: 2
#
#   Explanation: There are two ways to climb to the top.
#   1. 1 step + 1 step
#   2. 2 steps
#
#   Example 2:
#
#   Input: n = 3
#   Output: 3
#
#   Explanation: There are three ways to climb to the top.
#   1. 1 step + 1 step + 1 step
#   2. 1 step + 2 steps
#   3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n):

        numOfSteps = [0] * (n+1)
        numOfSteps[0] = numOfSteps[1] = 1

        for i in range(2, n+1):
            numOfSteps[i] = numOfSteps[i-1] + numOfSteps[i-2]

        return numOfSteps[n]
        