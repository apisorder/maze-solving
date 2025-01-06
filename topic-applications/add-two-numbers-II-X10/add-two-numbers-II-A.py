
#   Programmer:     Cheng, Jeff
#   Last Modified:  01-05-2025 09:49PM
#   Problem:        445. Add Two Numbers II (reverse method)
#
#   You are given two non-empty linked lists representing two non-negative integers.
#    
#   The most significant digit comes first (natural order) and each of their nodes 
#   contains a single digit. 
#   
#   Add the two numbers and return the sum as a linked list.
#
#   You may assume the two numbers do not contain any leading zero, except the number 
#   0 itself.
#
#   Example 1:
#
#   Input: l1 = [7,2,4,3], l2 = [5,6,4]
#   Output: [7,8,0,7]
#
#   Example 2:
#
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [8,0,7]
#
#   Example 3:
#
#   Input: l1 = [0], l2 = [0]
#   Output: [0]

#   Definition for list node
class ListNode:
    #   parameters: this, value, next pointer
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#   Now incorporate list node in a singly-linked linked list
class Solution:
    #   parameters:  this, list 1, list 2
    def addTwoNumbers(self, l1, l2):
        #   parameters: list
        def reverse(l):
            #   reversing the list -> original list current node's next points 
            #   to None
            #   therefore, previous needs to point to None
            previous = None

            while l:
                #   save the next pointer
                temp = l.next
                #   set next pointer to point to the previous node
                l.next = previous
                #   update previous to point to the current node
                previous = l
                #   move down to the next node in the original list
                l = temp
            
            #   l would point to None at this point
            return previous

        #   reverse both lists for easier processing
        l1 = reverse(l1)
        l2 = reverse(l2)

        dummyHead = ListNode()
        current = dummyHead

        carry = 0
        while l1 or l2 or carry:
            #   save the carry
            val = carry

            #   if list is present, add the node value, and advance the list
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            val = val % 10
            #   add the node to current list
            current.next = ListNode(val)
            current = current.next

        #   return the head in the original order, i.e. natural order
        return reverse(dummyHead.next)