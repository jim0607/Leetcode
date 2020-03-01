#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (36.78%)
# Likes:    1714
# Dislikes: 114
# Total Accepted:    233.2K
# Total Submissions: 632.1K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        if m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # find node_m_minus and mode_m
        node_m_minus, node_n = dummy, dummy
        for _ in range(m - 1):
            node_m_minus = node_m_minus.next
        node_m = node_m_minus.next
        
        # find node_n and node_n_plus
        for _ in range(n):
            node_n = node_n.next
        node_n_plus = node_n.next
        
        # reverse m to n
        prev, curr = node_m, node_m.next
        while curr != node_n_plus:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        
        # hook up node_m_minus with node_n, and node_m with node_n_plus
        node_m_minus.next = node_n
        node_m.next = node_n_plus
        
        return dummy.next
