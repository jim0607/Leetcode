#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (58.52%)
# Likes:    3314
# Dislikes: 78
# Total Accepted:    783.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
solution 1: iterative
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
    
        return prev
        

"""
solution 2: recursion
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        return the new head of the reversed list (the reversed list is headed as head)
        """
        if not head or not head.next:
            return head
        
        nextNode = head.next
        reversedHead = self.reverseList(nextNode)   # 这一部分执行完了之后nextNode已经变成了后面一大坨已经翻                            转好的List的tail了
        nextNode.next = head
        head.next = None
        
        return reversedHead
