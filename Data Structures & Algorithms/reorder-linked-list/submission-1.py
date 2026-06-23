# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        # finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now reverse the second half of the list
        prev = slow
        temp = slow.next
        slow.next = None
        
        while temp:
            slow = temp
            temp = temp.next
            slow.next = prev
            prev = slow

        # Now merge the first half to the reversed second half alternately
        list1 = head
        list2 = prev

        temp1 = list1.next
        temp2 = list2.next

        while temp1 and temp2:
            list1.next = list2
            list1 = temp1
            temp1 = temp1.next
            list2.next = list1
            list2 = temp2
            temp2 = temp2.next

            


        

