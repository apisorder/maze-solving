
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
        def listLength(l):
            length = 0

            while l:
                length += 1
                l = l.next

            return length

        list1_length = listLength(l1)
        list2_length = listLength(l2)

        dummyHead = ListNode()

        while list1_length > 0 and list2_length > 0:
            val = 0
            if list1_length >= list2_length:
                val += l1.val
                l1 = l1.next
                list1_length -= 1
            if list1_length < list2_length:
                val += l2.val
                l2 = l2.next
                list2_length -= 1

            head = ListNode(val, dummyHead)
            dummyHead = head

        current = dummyHead
        dummyHead = None

        carry = 0
        while current:
            val = carry + current.val
            carry = val // 10
            val = val % 10

            head = ListNode(val, dummyHead)
            dummyHead = head

            current = current.next

        if dummyHead.val == 0:
            return dummyHead.next
        else:
            return dummyHead