# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse_list(h):
            cur = h
            prev = None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        new_head = reverse_list(head)
        if n == 1:
            new_head = new_head.next
            return reverse_list(new_head)
        cur = new_head
        counter = 1
        prev = None
        while counter < n:
            prev = cur
            cur = cur.next
            counter += 1
        prev.next = cur.next
        return reverse_list(new_head)
