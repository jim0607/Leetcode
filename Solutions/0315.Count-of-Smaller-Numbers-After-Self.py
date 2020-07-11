315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.


"""
Segment Tree solution: O(NlogN) time and O(N) space
"""

class SegmentTree:
    
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = None
        self.right = None
        
    def build(self, start, end):
        if start > end:
            return None
        
        root = SegmentTree(start, end, 0)
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        root.cnt = 0
        
        return root
    
    def update(self, root, num):
        if root.start > num or root.end < num:
            return
        
        if root.start == root.end:
            root.cnt += 1
            return
        
        mid = root.start + (root.end - root.start) // 2     # [start, mid], [mid+1, end]
        if num <= mid:
            self.update(root.left, num)
        elif num >= mid + 1:
            self.update(root.right, num)
            
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
        
        if start <= root.start and end >= root.end:
            return root.cnt
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)

    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]
        
        min_num, max_num = min(nums), max(nums)
        
        segment_tree = SegmentTree(min_num, max_num, 0)
        root = segment_tree.build(min_num, max_num)
        
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            segment_tree.update(root, nums[i])
            cnt_of_smaller = 0
            if nums[i] > min_num:
                cnt_of_smaller = segment_tree.query(root, min_num, nums[i] - 1)
            res[i] = cnt_of_smaller
            
        return res

"""
Follow up:
对于segment tree的解法, update 和 query 都是O(logM), 所以overall time complexity is O(NlogM), N is the lens of nums, M is (max_num - min_num).
对于M很大的情况就很吃亏比如 [2147483647,-2147483647] 在build的时候就需要构建很大的一棵树 - O(max - min) 会导致TLE.
怎样避免呢？
我们可以使用mergesort:
The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. 
So we can do mergesort with added tracking of those right-to-left jumps.
"""
