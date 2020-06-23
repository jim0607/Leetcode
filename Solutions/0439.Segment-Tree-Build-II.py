439. Segment Tree Build II

The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment / interval.

start and end are both integers, they should be assigned in following rules:

The root's start and end is given by build method.
The left child of node A has start=A.left, end=(A.left + A.right) / 2.
The right child of node A has start=(A.left + A.right) / 2 + 1, end=A.right.
if start equals to end, there will be no children for this node.
Implement a build method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.

Example
Input: [3,2,1,4]
Explanation:
The segment tree will be
          [0,3](max=4)
          /          \
       [0,1]         [2,3]    
      (max=3)       (max=4)
      /   \          /    \    
   [0,0]  [1,1]    [2,2]  [3,3]
  (max=3)(max=2)  (max=1)(max=4)
Clarification
Segment Tree (a.k.a Interval Tree) is an advanced data structure which can support queries like:

which of these intervals contain a given point
which of these points are in a given interval



"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, arr):
        return self.build_helper(0, len(arr) - 1, arr)
        
    def build_helper(self, start, end, arr):
        if start > end:
            return None
            
        root = SegmentTreeNode(start, end, arr[start])
        if start == end:
            return root
            
        mid = start + (end - start) // 2
        root.left = self.build_helper(start, mid, arr)
        root.right = self.build_helper(mid + 1, end, arr)
        root.max = max(root.left.max, root.right.max)
        
        return root
