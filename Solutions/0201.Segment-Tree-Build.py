201. Segment Tree Build

The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment / interval.

start and end are both integers, they should be assigned in following rules:

The root's start and end is given by build method.
The left child of node A has start=A.start, end=(A.start + A.end) / 2.
The right child of node A has start=(A.start + A.end) / 2 + 1, end=A.end.
if start equals to end, there will be no children for this node.
Implement a build method with two parameters start and end, so that we can create a corresponding segment tree with every node has the correct start and start value, return the root of this segment tree.

Example
Example 1:

Input：[1,4]
Output："[1,4][1,2][3,4][1,1][2,2][3,3][4,4]"
Explanation：
	               [1,  4]
	             /        \
	      [1,  2]           [3, 4]
	      /     \           /     \
	   [1, 1]  [2, 2]     [3, 3]  [4, 4]
Example 2:

Input：[1,6]
Output："[1,6][1,3][4,6][1,2][3,3][4,5][6,6][1,1][2,2][4,4][5,5]"
Explanation：
	       [1,  6]
             /        \
      [1,  3]           [4,  6]
      /     \           /     \
   [1, 2]  [3,3]     [4, 5]   [6,6]
   /    \           /     \
[1,1]   [2,2]     [4,4]   [5,5]
Clarification
Segment Tree (a.k.a Interval Tree) is an advanced data structure which can support queries like:

which of these intervals contain a given point
which of these points are in a given interval



"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""
"""

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        if start > end:
            return None
            
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
            
        mid = start + (end - start) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        
        return root
