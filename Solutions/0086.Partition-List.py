86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, pivot: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        left, left_head = dummy1, dummy1        # 注意这里要用两个dummy node, 将左边和右边分开！！！
        right, right_head = dummy2, dummy2
        curr = head
        while curr:
            if curr.val < pivot:
                left.next = curr
                left = left.next
                curr = curr.next
            else:
                right.next = curr
                right = right.next
                curr = curr.next
        
        right.next = None               # 注意这里断开很重要
        left.next = right_head.next     # 注意这里要把两边连起来
            
        return left_head.next
