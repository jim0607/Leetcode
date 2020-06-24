248. Count of Smaller Number

Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. 
For each query, give you an integer, return the number of element in the array that are smaller than the given integer.

Example
Example 1:

Input: array =[1,2,7,8,5] queries =[1,8,5]
Output:[0,4,2]
Example 2:

Input: array =[3,4,5,8] queries =[2,4]
Output:[0,1]
Challenge
Could you use three ways to do it.

Just loop
Sort and binary search
Build Segment Tree and Search.


"""
solution 1: binary search, need to sort the arr first which takes O(NlogN)
solution 2: Segment Tree, which takes O(N) to build the tree and O(logN) to query. To find how many numbers are less than num, 
is actually to find how many numbers are there in range [0, num-1], since the minimum number is 0 given by the description of the problem.
since we add num into the tree one by one, each update takes O(logN), so the whole updating takes O(NlogN).
这题的self.start, self.end represent the num, not idx.  sel.cnt is how many numbers are there in range [start, end], and again start, end are not idx, they are actual vals.
"""

class SegmentTree:
    
    def __init__(self, start, end, cnt):
        self.start = start  # self.start represent the num, not idx
        self.end = end
        self.cnt = cnt      # cnt is how many numbers are there in range [start, end], note that start, end are not idx, they are actual vals
        self.left = None 
        self.right = None
        
    def build(self, start, end):
        """
        After building the tree, all the number in range [start, end] are initialized as self.cnt = 0
        """
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
        
    def update(self, root, num):        # O(N)
        """
        update the self.cnt in the tree after adding a num into the tree
        其实就是用二分法(divide and conquer)找到 num 在tree中所在的node, 找到之后node.cnt+=1
        """
        if root.start > num or root.end < num:
            return 
        
        if root.start == root.end:
            root.cnt += 1
            return
        
        mid = root.start + (root.end - root.start) // 2
        if root.start <= num <= mid:
            self.update(root.left, num)
        if mid < num <= root.end:
            self.update(root.right, num)
            
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        """
        We are querying how many numbers are there in range [start, end]
        """
        if root.start == start and root.end == end:
            return root.cnt
            
        mid = root.start + (root.end - root.start) // 2     # 分成[root.start, mid], [mid+1, root.end]两部分 
        if start > mid:
            return self.query(root.right, start, end)
        if end < mid + 1:
            return self.query(root.left, start, end)
        
        return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)


class Solution:
    def countOfSmallerNumber(self, nums, queries):
        segment_tree = SegmentTree(0, 10000, 0)  # self.cnt最开始都初始化为0, 然后再用update函数更新
        root = segment_tree.build(0, 10000)      # 题目规定数字的范围了，
        
        for num in nums:       # put num into the tree one by one, takes O(NlogN) 
            segment_tree.update(root, num)
            
        res = []
        for q in queries:
            cnt = 0
            if q > 0:
                cnt = segment_tree.query(root, 0, q - 1)
            res.append(cnt)
            
        return res
