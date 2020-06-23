247. Segment Tree Query II

For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of elements in the the array which value is between interval start and end. (The array may not fully filled by elements)

Design a query method with three parameters root, start and end, find the number of elements in the in array's interval [start, end] by the given root of value SegmentTree.

Example
Example 1:

Input："[0,3,count=3][0,1,count=1][2,3,count=2][0,0,count=1][1,1,count=0][2,2,count=1][3,3,count=1]",[[1, 1], [1, 2], [2, 3], [0, 2]]
Output：[0,1,2,2]
Explanation：
The corresponding value Segment Tree is:

	                     [0, 3, count=3]
	                     /             \
	          [0,1,count=1]             [2,3,count=2]
	          /         \               /            \
	   [0,0,count=1] [1,1,count=0] [2,2,count=1], [3,3,count=1]

Input : query(1,1), Output: 0

Input : query(1,2), Output: 1

Input : query(2,3), Output: 2

Input : query(0,2), Output: 2
Example 2:

Input："[0,3,count=3][0,1,count=1][2,3,count=2][0,0,count=1][1,1,count=0][2,2,count=0][3,3,count=1]",[[1, 1], [1, 2], [2, 3], [0, 2]]
Output：[0,0,1,1]
Explanation：
The corresponding value Segment Tree is:

	                     [0, 3, count=2]
	                     /             \
	          [0,1,count=1]             [2,3,count=1]
	          /         \               /            \
	   [0,0,count=1] [1,1,count=0] [2,2,count=0], [3,3,count=1]

Input : query(1,1), Output: 0

Input : query(1,2), Output: 0

Input : query(2,3), Output: 1

Input : query(0,2), Output: 1


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        if not root:
            return 0
            
        if start > root.end or end < root.start:
            return 0
        
        if start <= root.start and end >= root.end:
            return root.count
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)
