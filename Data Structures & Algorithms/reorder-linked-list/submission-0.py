# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #[0, n-1, 1, n-2, 2, n-3, 3]
        #l, r = 0, len(linkedlist)-1
        #push l and r in new list

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse the second half
        second = slow.next
        prev = slow.next = None
            
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first, second =head, prev 
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
