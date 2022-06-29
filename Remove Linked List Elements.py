# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeElements(self, head, val):
        result = None

        while (head):
            if not result and head.val != val:
                result = head
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return result