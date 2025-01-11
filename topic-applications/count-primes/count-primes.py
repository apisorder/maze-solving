
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-11-2025 12:50PM
#   Problem:        204. Count Primes
#   References:     https://en.wikipedia.org/wiki/Prime_number
#                   A prime number (or a prime) is a natural number greater than 1 
#                   that is not a product of two smaller natural numbers. A natural 
#                   number greater than 1 that is not prime is called a composite 
#                   number. For example, 5 is prime because the only ways of writing 
#                   it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is 
#                   composite because it is a product (2 × 2) in which both numbers 
#                   are smaller than 4. Primes are central in number theory because 
#                   of the fundamental theorem of arithmetic: every natural number 
#                   greater than 1 is either a prime itself or can be factorized as 
#                   a product of primes that is unique up to their order.
#                   
#                   https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#                   In mathematics, the sieve of Eratosthenes is an ancient algorithm 
#                   for finding all prime numbers up to any given limit.
#
#                   It does so by iteratively marking as composite (i.e., not prime) 
#                   the multiples of each prime, starting with the first prime number, 
#                   2. The multiples of a given prime are generated as a sequence of 
#                   numbers starting from that prime, with constant difference between 
#                   them that is equal to that prime.  This is the sieve's key 
#                   distinction from using trial division to sequentially test each 
#                   candidate number for divisibility by each prime.  Once all the 
#                   multiples of each discovered prime have been marked as composites, 
#                   the remaining unmarked numbers are primes.
#
#                   To find all the prime numbers less than or equal to a given integer 
#                   n by Eratosthenes' method:
#
#                   1-Create a list of consecutive integers from 2 through n: (2, 3, 4, 
#                   ..., n).
#                   2-Initially, let p equal 2, the smallest prime number.
#                   3-Enumerate the multiples of p by counting in increments of p from 
#                   2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; 
#                   the p itself should not be marked).
#                   4-Find the smallest number in the list greater than p that is not 
#                   marked. If there was no such number, stop. Otherwise, let p now 
#                   equal this new number (which is the next prime), and repeat from 
#                   step 3.
#                   5-When the algorithm terminates, the numbers remaining not marked 
#                   in the list are all the primes below n.
#
#                   https://leetcode.com/problems/count-primes/solutions/435363/python3-simple-code-how-to-make-your-cod-lx4b/
#                   The code line lst[m * m: n: m] = [0] *((n-m*m-1)//m + 1) is key to 
#                   reduce the run time. You could write a loop like this (but it 
#                   would be very expensive):
#
#                   for i in range(m * m, n,  m):
#                      lst[i] = 0
#
#                   Do not use function sqrt, because it is expensive 
#                   [do not use: m < sqrt(n)]. Instead, use m * m < n                                      
#
#                   https://leetcode.com/problems/count-primes/solutions/473021/time-complexity-ologlogn-explained-by-as-5344/
#                   But how many "cross outs" do we have to do for each prime?
#
#                   Well,
#
#                   For 2, we have to cross out n/2 numbers.
#                   For 3, we have to cross out n/3 numbers.
#                   For 5, we have to cross out n/5 numbers.
#                   ...etc for each prime less than n.
#                   
#                   This means that the time complexity of "crossing out" is 
#                   O(n/2 + n/3 + n/5 + ... + n/(last prime before n)).
#
#                   What can this sum be simplified to in terms of n?
#
#                   = O(n) * O(log(log(n)))
#                   = O(nlog(log(n)))
#
#                   = What about when people say the time complexity is 
#                   O(sqrt(n)log(log(n)))?
#
#   Complexity      time -> O(n log(log n))
#                   space -> O(n)
#   Given an integer n, return the number of prime numbers that are strictly less than n.
#
#   Example 1:
#
#   Input: n = 10
#   Output: 4
#
#   Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#   Example 2:
#
#   Input: n = 0
#   Output: 0
#
#   Example 3:
#
#   Input: n = 1
#   Output: 0

import math

class Solution:
    def countPrimes(self, n):

        #   edge case:  no prime number less than 2
        if n < 2:
            return 0

        allPrimes = [1] * n
        #  no prime number less than 2
        allPrimes[0] = allPrimes[1] = 0
        
        m = 2
        #   we only check a number (m) if its square is less than n
        while m * m < n:
        # for i in range(2, int(math.sqrt(n))+1):
            if allPrimes[m] == 1:
                #   mark all multiples
                allPrimes[m * m : n : m] = [0] * ((n-1 -m*m) // m + 1)

            number += 1

        return sum(allPrimes)