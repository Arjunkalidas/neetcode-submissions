# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        temp = dummy
        length = 0

        while temp:
            length += 1
            temp = temp.next

        del_node = length - n

        temp = dummy
        i = 0
        while i < del_node-1 and temp:
            temp = temp.next
            i += 1
        
        temp.next = temp.next.next

        return dummy.next
    

            