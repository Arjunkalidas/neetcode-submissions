# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        l1 = list1
        l2 = list2
        head = None

        if l1 and l2 and l1.val <= l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        elif l1 and l2 and l2.val <= l1.val:
            head = ListNode(l2.val)
            l2 = l2.next

        curr = head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next

        while curr and l1:
            curr.next = ListNode(l1.val)
            l1 = l1.next
            curr = curr.next

        while curr and l2:
            curr.next = ListNode(l2.val)
            l2 = l2.next
            curr = curr.next

        return head

