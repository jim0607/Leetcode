206. Interval Sum

Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the sum number between index start and end in the given array, return the result list.

Example
Example 1:

Input: array = [1,2,7,8,5],  queries = [(0,4),(1,2),(2,4)]
Output: [23,9,20]
Example 2:

Input: array = [4,3,1,2],  queries = [(1,2),(0,2)]
Output: [4,8]
Challenge
O(logN) time for each query



class SegmentTree:
    
    def __init__(self, start, end, range_sum):
        self.start = start
        self.end = end
        self.range_sum = range_sum
        self.left = None
        self.right = None
        
    def build(self, start, end, nums):
        """
        Return the root of the built tree
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
        
    def query(self, root, start, end):
        """
        Return the sum in range [start, end]
        """
        if start > root.end or end < root.start:
            return 0
            
        if start <= root.start and end >= root.end:
            return root.range_sum
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)
    
    
class Solution:
    def intervalSum(self, arr, queries):
        segment_tree = SegmentTree(0, len(arr) - 1, 0)
        root = segment_tree.build(0, len(arr) - 1, arr)
        
        res = []
        for q in queries:
            res.append(segment_tree.query(root, q.start, q.end))
            
        return res
