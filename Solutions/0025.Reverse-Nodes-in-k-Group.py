#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (38.91%)
# Likes:    1610
# Dislikes: 317
# Total Accepted:    225.9K
# Total Submissions: 578.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # dummy.next is always head of the Linked List
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr:
            curr = self.reverse(curr, k)

        return dummy.next
    
    # reverse n1 -> n2 -> ..... -> nk
    # head -> n1 -> n2 -> ..... -> nk -> nk+1
    # after reverse shoule be : head -> nk -> ....n1 -> nk+1
    # return head
    def reverse(self, head: ListNode, k: int) -> ListNode:
        n1 = head.next
        nk = head
        for i in range(k):
            nk = nk.next
            if not nk:
                return None

        # reverse
        nkplus = nk.next
        prev, curr = None, n1
        while curr != nkplus:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # connect
        head.next = nk
        n1.next = nkplus

        return n1

# @lc code=end

