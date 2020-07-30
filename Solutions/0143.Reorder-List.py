143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


"""
step 1: cut the list into two halves;
step 2: reverse the 2nd half;
step 3: connect the 1st and 2nd half
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        # step 1: cut the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None        # 断开左右两边
        
        # step 2: reverse the 2nd half
        prev, curr = None, right_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        right_head = prev

        # step 3: connect the 1st and 2nd half
        left, right = head, right_head
        while left and right:
            temp_left = left.next
            temp_right = right.next
            left.next = right
            right.next = temp_left
            
            left = temp_left
            right = temp_right            
