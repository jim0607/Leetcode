"""
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
"""

    

"""
Count "important reverse pairs" while doing mergesort:
When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j.
So in addition to the while loop for do merge/conquer, we use a while loop to compare nums[i] and 2*nums[j] to update cnt.  
This while loop is for every left_sublist and right_sublist.
其实merge sort 才是这道题的正解 - O(nlogn)
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self._merge_sort(nums)
        return self.cnt
    
    def _merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        # divide
        mid = len(nums) // 2
        left = self._merge_sort(nums[:mid])
        right = self._merge_sort(nums[mid:])
        
        # before the conquer while loop, we use another while loop to update our cnt for this sorted left_sublist and right_sublist
        i, j = 0, 0
        while i < len(left) and j < len(right):     
            if left[i] > 2 * right[j]:          # 这里只需要比较数值不需要比较idx是因为left属于nums[:mid], 而right属于num[mid:].
                self.cnt += len(left) - i       # 因为left已经sort好了，所以如果left[i]>2*right[j], 那么i后面的都会>2*right[j]
                j += 1                          # 上面self.cnt用的是i更新的，所以这里j往前挪一位. j 要奔着结束这个if判断条件而去. 
            else:                               # 所以逻辑是我们想更新self.cnt based on j, 所以必须用i去更新, 更新完之后j要往后挪一位, 
                i += 1                          # j又要奔着结束if判断条件去
        
        # now we do conquer/merge for merge sort
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
        
        return nums

    
    

"""
solution 1: segment tree. similar with 315. count of smaller number after itself.
We sweep from left to right, and query range [2*num+1, max_num].
与count number after itself相比，就只有一行代码不同
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
            return
        
        root = SegmentTree(start, end, 0)
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end)
        root.cnt = 0
        
        return root
    
    def update(self, root, num):
        if root.start > num or root.end < num:
            return
        
        if root.start == root.end:
            root.cnt += 1
            return
        
        mid = root.start + (root.end - root.start) // 2
        if num <= mid:
            self.update(root.left, num)
        else:
            self.update(root.right, num)
            
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
        
        elif start <= root.start and end >= root.end:
            return root.cnt
        
        else:
            return self.query(root.left, start, end) + self.query(root.right, start, end)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        
        lens = len(nums)
        min_num, max_num = min(nums), max(nums)
        segment_tree = SegmentTree(min_num, max_num, 0)
        root = segment_tree.build(min_num, max_num)
        
        res = 0
        for i in range(1, len(nums)):
            segment_tree.update(root, nums[i-1])
            res += segment_tree.query(root, 2*nums[i]+1, max_num)   # 与count number after itself相比，就只有这一行代码不同
        
        return res
        

"""
Follow up: what is the time complexity if it is a Spare Segment Tree?
对于segment tree的解法, update 和 query 都是O(logM), 所以overall time complexity is O(NlogM), N is the lens of nums, M is (max_num - min_num).
对于M很大的情况就很吃亏比如 [2147483647,-2147483647] 在build的时候就需要构建很大的一棵树 - O(max - min) 会导致TLE.
怎样避免呢？
我们可以使用mergesort:
The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. 
So we can do mergesort with added tracking of those right-to-left jumps.
"""
