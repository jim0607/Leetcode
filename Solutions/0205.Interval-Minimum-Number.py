205. Interval Minimum Number

Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the minimum number between index start and end in the given array, return the result list.

Example
Example 1:

Input : array: [1,2,7,8,5], queries :[(1,2),(0,4),(2,4)] .Output: [2,1,5]
Example 2:

Input : array: [4,5,7,1], queries :[(1,2),(1,3)]. Output: [5,1]
Challenge
O(logN) time for each query


class SegmentTree:
    
    def __init__(self, start, end, min_num):
        self.start = start
        self.end = end
        self.min_num = min_num
        self.left = None
        self.right = None
        
    def build(self, start, end, nums):
        if start > end:
            return None
        
        root = SegmentTree(start, end, nums[start])
        if start == end:
            return root
            
        mid = start + (end - start) // 2
        root.left = self.build(start, mid, nums)
        root.right = self.build(mid + 1, end, nums)
        root.min_num = min(root.left.min_num, root.right.min_num)
        
        return root
        
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return float("inf")
            
        if start <= root.start and end >= root.end:
            return root.min_num
            
        return min(self.query(root.left, start, end), self.query(root.right, start, end))
    
    
    
class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, arr, queries):
        segment_tree = SegmentTree(0, len(arr) - 1, float("inf"))
        root = segment_tree.build(0, len(arr) - 1, arr)
        
        res = []
        for query in queries:
            res.append(segment_tree.query(root, query.start, query.end))
            
        return res
