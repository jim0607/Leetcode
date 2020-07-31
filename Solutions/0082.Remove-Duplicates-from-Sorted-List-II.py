82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3



"""
anchor stays where on it's left there is only distinct numbers
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("inf"))
        dummy.next = head
        anchor, prev, curr = dummy, dummy, head
        while curr:
            if prev.val == curr.val:
                prev = prev.next
                curr = curr.next
            else:                                               # 需要比较prev, curr的val来判断一个数是不是合格的
                if not curr.next or curr.next.val != curr.val:  # 还需要比较curr, curr.next的val来判断一个数是不是合格的
                    anchor.next = curr
                    anchor = anchor.next
                prev = prev.next
                curr = curr.next
                
        anchor.next = None      # 把anchor后面的都断开，因为后面的都是duplicated numbers
        return dummy.next
