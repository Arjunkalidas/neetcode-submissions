# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        left = right = temp = head

        while right.next:
            right = right.next

        while left != right:
            temp = left.next
            left.next = right
            right.next = temp

            left = temp
            while temp and temp.next != right:
                temp = temp.next
            right = temp
        right.next = None

