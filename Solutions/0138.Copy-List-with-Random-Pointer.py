#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (31.19%)
# Likes:    2337
# Dislikes: 558
# Total Accepted:    328.1K
# Total Submissions: 1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
# 
# 
# 
# Constraints:
# 
# 
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        myMap = {}
        newHead = Node(head.val)
        myMap[head] = newHead
        curr = head
        newCurr = newHead

        while curr:
            newCurr.random = curr.random
            if curr.next:
                newCurr.next = Node(curr.next.val)
                myMap[curr.next] = newCurr.next
            else:
                newCurr.next = None
            curr = curr.next
            newCurr = newCurr.next

        curr = newHead
        while curr:
            if curr.random:
                curr.random = myMap[curr.random]
            curr = curr.next
        
        return newHead

# @lc code=end

