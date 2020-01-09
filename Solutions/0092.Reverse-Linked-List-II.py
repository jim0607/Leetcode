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

# @lc code=start
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

        # start from the one before m
        node_m_minus, node_n = dummy, dummy

        for i in range(m-1):
            node_m_minus = node_m_minus.next
        for i in range(n):
            node_n = node_n.next
        
        node_m = node_m_minus.next
        node_n_plus = node_n.next

        # step 1: reverse
        prev, curr = None, node_m
        while curr != node_n_plus:
            print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # step 2: connect
        node_m_minus.next = node_n
        node_m.next = node_n_plus
        
        return dummy.next
        
# @lc code=end

