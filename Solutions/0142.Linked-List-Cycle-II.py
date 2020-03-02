#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (34.54%)
# Likes:    1996
# Dislikes: 162
# Total Accepted:    265.5K
# Total Submissions: 763.8K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# Note: Do not modify the linked list.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# Follow-up:
# Can you solve it without using extra space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        # 快慢指针找到相遇的点
        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast or not fast.next:   # if no cycel, return None
                return None
            slow = slow.next
            fast = fast.next.next

        # 定义两根指针分别从head和上面相遇的点出发，然后p1,p2相遇的地方就是环的入口
        p1, p2 = head, slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        
# @lc code=end

