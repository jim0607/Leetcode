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

"""
solution 1: recursion
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        nextNode = head.next
        swappedNode = self.swapPairs(nextNode.next)

        head.next = swappedNode
        nextNode.next = head
        
        return nextNode     # return已处理好的头部给上一级



"""dummy node is so important in this case"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        swap nodes and return the new head
        """
        if not head or not head.next:
            return head
        
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr = dummyNode
        
        while curr and curr.next:
            self.reverse(curr)
            curr = curr.next.next
            
        return dummyNode.next
    
    def reverse(self, curr):
        """
        reverse 0->1->2->3 to be 0->2->1->3
        """
        if not curr or not curr.next or not curr.next.next:
            return
        
        firstNode = curr.next
        secondNode = firstNode.next
        thirdNode = secondNode.next
        
        curr.next = secondNode
        secondNode.next = firstNode
        firstNode.next = thirdNode
