# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n = None
        n1 = None
        l1 = list1
        l2 = list2
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        while(l1 is not None and l2 is not None):
            if l1.val >= l2.val:
                value = l2.val
                l2 = l2.next
            elif l1.val < l2.val:
                value = l1.val
                l1 = l1.next
            if n == None:
                n = ListNode(value)
                n1 = n
            else:
                n1.next = ListNode(value)
                n1 = n1.next
        while(l1):
            n1.next = ListNode(l1.val)
            n1 = n1.next
            l1 = l1.next
        while(l2):
            n1.next = ListNode(l2.val)
            n1 = n1.next
            l2 = l2.next
        return n