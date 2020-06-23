202. Segment Tree Query

For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.

Example
Example 1:

Input："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",1,2
Output：4
Explanation：
For array [1, 4, 2, 3], the corresponding Segment Tree is :

	                  [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
	   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
The maximum value of [1,2] interval is 4
Example 2:

Input："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",2,3
Output：3
Explanation：
For array [1, 4, 2, 3], the corresponding Segment Tree is :

	                  [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
	   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
The maximum value of [2,3] interval is 3



"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return -float("inf")
            
        if start <= root.start and end >= root.end:
            return root.max
            
        return max(self.query(root.left, start, end), self.query(root.right, start, end))
