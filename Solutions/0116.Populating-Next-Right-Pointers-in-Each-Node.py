116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        while q:
            prev = q.popleft()
            lens = len(q)
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            for _ in range(lens):
                curr = q.popleft()
                prev.next = curr
                prev = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            prev.next = None
                
        return root
        
        
        
        
        
"""
Follow up: what if only use constant extra space?
我们可以设立两个指针，一根leftmost一直往下走，一根head在一层之中一直往右走，边走边连
"""
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        leftmost = root
        while leftmost.left:        #从上往下一层一层遍历
            head = leftmost
            while head:     # 从leftmost node开始从左往右连接
                head.left.next = head.right     # 连接head.left和head.right
                if head.next:                   # 连接head.right和head.next.left
                    head.right.next = head.next.left
                head = head.next                # head往右挪一步
                
            leftmost = leftmost.left            # head往下走一步
            
        return root
