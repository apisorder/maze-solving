
#   Programmer:     Cheng, Jeff
#   Last Modified:  05-13-2024 09:53PM
#   Problem:        445. Add Two Numbers II 

#   You are given two non-empty linked lists representing two non-negative integers. 
#   The most significant digit comes first and each of their nodes contains a single digit. 
#   Add the two numbers and return the sum as a linked list.

#   You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#   Example 1:
#   Input: l1 = [7,2,4,3], l2 = [5,6,4]
#   Output: [7,8,0,7]

#   Example 2:
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [8,0,7]

#   Example 3:
#   Input: l1 = [0], l2 = [0]
#   Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def reverse(l):
            previous = None

            while l:
                temp = l.next
                l.next = previous
                previous = l
                l = temp
            return previous

        l1 = reverse(l1)
        l2 = reverse(l2)

        dummyHead = ListNode()
        current = dummyHead

        carry = 0
        while l1 or l2 or carry:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next

        return reverse(dummyHead.next)