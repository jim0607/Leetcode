"""
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""



"""
Count while doing mergesort:
When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j.
So in addition to the while loop for do merge/conquer, we use a while loop to compare nums[i] and nums[j] to update cnt.  
This while loop is for every left_sublist and right_sublist.
没想到merge sort还能这么出题，看来熟练掌握理解各种基础sort的方法很有用呀！
"""

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res = [0 for _ in range(len(nums))]
        nums = [(num, i) for i, num in enumerate(nums)]     # 注意因为self.res是要更新没有个idx的cnt, 所以要把idx带在nums里面去sort nums
        nums = self._merge_sort(nums)
        return self.res
    
    def _merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        # divide
        mid = len(nums) // 2
        left = self._merge_sort(nums[:mid])
        right = self._merge_sort(nums[mid:])
        
        # before conquer, we update our res
        i, j = len(left) - 1, len(right) - 1
        while i >= 0 and j >= 0:
            if left[i][0] > right[j][0]:        # 这里只需要比较数值不需要比较idx是因为left属于nums[:mid], 而right属于num[mid:]   
                self.res[left[i][1]] += j + 1   # 因为right已经sort好了，所以如果left[i]>right[j], 那么left[i]>所有j和它前面的数
                i -= 1                          # 上面self.cnt用的是j更新的，所以这里i往前挪一位. i 要奔着结束这个if判断条件而去，这就是为什么i, j要从右往左走 
            else:                               # 所以逻辑是我们想更新self.res[i], 所以必须用j去更新, 更新完之后i要往后挪一位, i又要奔着结束if判断条件去 
                j -= 1
        
        # conquer
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
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
            j += 1
            k += 1
        
        return nums



"""
也可以按照从大到小sort
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(nums_tuple):
            if len(nums_tuple) <= 1:
                return nums_tuple
            
            # divide
            mid = len(nums_tuple) // 2
            left = merge_sort(nums_tuple[:mid])
            right = merge_sort(nums_tuple[mid:])
            
            # conquer
            # before conquer, we need to update res for this sorted left_sublist and right_sublist
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:            # 这里只需要比较数值不需要比较idx是因为left属于nums[:mid], 而right属于num[mid:]
                    self.res[left[i][1]] += len(right) - j   # 因为right已经sort好了，所以如果left[i]>right[j], 那么left[i]>所有j后面的数
                    i += 1      # 注意这里是i+=1
                else:
                    j += 1
                    
            # conquer/merge - 这里merge要逆序排列
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:    # 逆序排列
                    nums_tuple[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums_tuple[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                nums_tuple[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums_tuple[k] = right[j]
                j += 1
                k += 1
                
            return nums_tuple
        
        self.res = [0 for _ in range(len(nums))]
        nums_tuple = [(num, i) for i, num in enumerate(nums)]
        merge_sort(nums_tuple)      # 这里把idx传进去的原因是为了update self.res的时候能通过left[i][1]]找到需要update的位置
        
        return self.res




"""
Segment Tree solution: O(NlogN) time and O(N) space
"""
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
