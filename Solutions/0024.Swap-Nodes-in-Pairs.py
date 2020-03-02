#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (47.54%)
# Likes:    1651
# Dislikes: 146
# Total Accepted:    393K
# Total Submissions: 823.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""dummy node is so important in this case"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr:
            curr = self.reverse(curr)
        
        return dummy.next

    # The input is n0 (not None)
    # swap the n0 -> n1 -> n2 -> n3
    # to be n0 -> n2 -> n1 -> n3
    # return n0 for hte next pair, which is n1 for this pair
    def reverse(self, curr: ListNode) -> ListNode:
        if not curr.next or not curr.next.next:
            return None
        
        n0, n1, n2, n3 = curr, curr.next, curr.next.next, curr.next.next.next

        # reverse n1 and n2
        n2.next = n1

        # connect
        n0.next = n2
        n1.next = n3

        # return the n0 for the next pair, which is n1 for this pair
        return n1
