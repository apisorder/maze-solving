
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-05-2025 09:47PM
#   Problem:        2. Add Two Numbers
#   Complexity:     time -> O(n)
#                   space -> O(1)
#
#   You are given two non-empty linked lists representing two non-negative integers.
#    
#   The digits are stored in reverse order, and each of their nodes contains a single 
#   digit.
#
#   Add the two numbers and return the sum as a linked list.
#
#   You may assume the two numbers do not contain any leading zero, except the number 
#   0 itself.
#
#   Example 1:
#
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [7,0,8]
#
#   Explanation: 342 + 465 = 807.
#
#   Example 2:
#
#   Input: l1 = [0], l2 = [0]
#   Output: [0]
#
#   Example 3:
#
#   Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#   Output: [8,9,9,9,0,0,0,1]

#   Definition for list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#   Now incorporate list node in a singly-linked linked list
class Solution:
    def addTwoNumbers(self, l1, l2):
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

        return dummyHead.next