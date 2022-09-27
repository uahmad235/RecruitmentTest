# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """remove nth item from end of the linked list"""
        leading_tmp = head
        trailing_tmp = head
        for curr_idx in range(n):
             
            # linked-list is exhauseted i.e., len(linked_list) < n
            if not leading_tmp.next:
                # len(linked_list) == n
                if curr_idx == n - 1:
                    head = head.next
                return head
            leading_tmp = leading_tmp.next
         
        # exhaust leading pointer until trailing pointer catches up to len(linked-list) - n
        while leading_tmp.next:
            leading_tmp = leading_tmp.next
            trailing_tmp = trailing_tmp.next
        
        # trailing-node = len(linked_list) - n - 1
        trailing_tmp.next = trailing_tmp.next.next
