"""
430. Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:


After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""




"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""



"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
            else:
                next_node = curr.next
                child_head = self.flatten(curr.child)   # 递归
                child_tail = self._find_tail(child_head)
                curr.next = child_head
                child_head.prev = curr
                child_tail.next = next_node
                if next_node:
                    next_node.prev = child_tail                
                curr.child = None       # return head之前别忘了把head.child设置成None
        return head
    
    def _find_tail(self, head):
        curr = head
        while curr and curr.next:
            curr = curr.next
        return curr




class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if not head.next and not head.child:
            return head
        if not head.child:
            next_flattend_head = self.flatten(head.next)
            head.next = next_flattend_head
            next_flattend_head.prev = head
            return head
        if not head.next:
            child_flattened_head = self.flatten(head.child)
            head.next = child_flattened_head
            child_flattened_head.prev = head
            head.child = None     # return head之前别忘了把head.child设置成None
            return head
        
        next_flattened_head = self.flatten(head.next)
        child_flattend_head = self.flatten(head.child)
        child_flattend_tail = self._find_tail(child_flattend_head)
        
        head.next = child_flattend_head
        child_flattend_head.prev = head
        child_flattend_tail.next = next_flattened_head
        next_flattened_head.prev = child_flattend_tail

        head.child = None         # return head之前别忘了把head.child设置成None
        return head
    
    def _find_tail(self, node):
        while node.next:
            node = node.next
        return node





"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        dummy = Node(-1, None, None, None)
        dummy.next = head
        head.prev = dummy
        prev_node, curr_node = dummy, head
        self._dfs(prev_node, curr_node)
        
        # detach the dummy node with head
        dummy.next.prev = None
        return dummy.next
        
    def _dfs(self, prev_node, curr_node):
        """
        dfs return the tail of the curr_node-->child_node
        """
        if not curr_node:
            return prev_node
        
        curr_node.prev = prev_node
        prev_node.next = curr_node
        
        temp = curr_node.next
        tail = self._dfs(curr_node, curr_node.child)
        curr_node.child = None      # remove the child node from curr_node
            
        return self._dfs(tail, temp)
