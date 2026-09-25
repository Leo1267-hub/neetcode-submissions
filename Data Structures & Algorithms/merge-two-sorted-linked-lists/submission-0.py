# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur_res = dummy_node
        cur1,cur2 = list1,list2
        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur_res.next = cur2
                cur2 = cur2.next
            else:
                cur_res.next = cur1
                cur1 = cur1.next

            cur_res = cur_res.next
        
        if cur1:
            cur_res.next = cur1
        elif cur2:
            cur_res.next = cur2            

        return dummy_node.next