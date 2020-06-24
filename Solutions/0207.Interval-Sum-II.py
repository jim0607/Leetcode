207. Interval Sum II

Given an integer array in the construct method, implement two methods query(start, end) and modify(index, value):

For query(start, end), return the sum from index start to index end in the given array.
For modify(index, value), modify the number in the given index to value
Example
Example 1

Input:
[1,2,7,8,5]
[query(0,2),modify(0,4),query(0,1),modify(2,1),query(2,4)]
Output: [10,6,14]
Explanation:
Given array A = [1,2,7,8,5].
After query(0, 2), 1 + 2 + 7 = 10,
After modify(0, 4), change A[0] from 1 to 4, A = [4,2,7,8,5].
After query(0, 1), 4 + 2 = 6.
After modify(2, 1), change A[2] from 7 to 1，A = [4,2,1,8,5].
After query(2, 4), 1 + 8 + 5 = 14.
Example 2

Input:
[1,2,3,4,5]
[query(0,0),query(1,2),quert(3,4)]
Output: [1,5,9]
Explantion:
1 = 1
2 + 3 = 5
4 + 5 = 9
Challenge
O(logN) time for query and modify.


"""
O(1) update and O(N) range sum is trival.  We need to update the arr and query range sum frequently
So we better come up with a way to realize O(logN) update and O(logN) range sum query
"""
"""

class SegmentTree:
    
    def __init__(self, start, end, range_sum):  
        """
        initialize a segment tree, a segment tree node has start idx of the arr, end idx of the arr, 
        range sum from start to end (inclussive), left node, right node
        """
        self.start = start 
        self.end = end
        self.range_sum = range_sum
        self.left = None
        self.right = None
        
    def build(self, start, end, nums):
        """
        build the segment tree, return the root of the tre - O(N)
        """
        if start > end:
            return None
            
        root = SegmentTree(start, end, nums[start])
        if start == end:
            return root

        mid = start + (end - start) // 2
        root.left = self.build(start, mid, nums)
        root.right = self.build(mid + 1, end, nums)
        root.range_sum = root.left.range_sum + root.right.range_sum
        
        return root
    
    def update(self, root, idx, val):
        """
        update the segment tree when there is an update in nums (change to val at idx) - O(logN)
        update 函数其实就是update range_sum
        """
        if not root:
            return
        
        if root.start == root.end:
            root.range_sum = val
            return
        
        if root.left.end >= idx:
            self.update(root.left, idx, val)
        else:
            self.update(root.right, idx, val)
            
        root.range_sum = root.left.range_sum + root.right.range_sum
        
    def query(self, root, start, end):
        """
        given a range, return the range sum covered by the range - O(logN)
        """
        if end < root.start or start > root.end:
            return 0
            
        if start <= root.start and end >= root.end:
            return root.range_sum
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)


class Solution:

    def __init__(self, arr):
        self.segment_tree = SegmentTree(0, len(arr) - 1, 0)             # instantiate a segment tree
        self.root = self.segment_tree.build(0, len(arr) - 1, arr)       # build a segment tree using the input arr

    def query(self, start, end):
        return self.segment_tree.query(self.root, start, end)

    def modify(self, index, value):
        self.segment_tree.update(self.root, index, value)
