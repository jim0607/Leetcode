327. Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.


"""
Solution 1: prefix_sum + hashmap.  construct a prefix_sum. Then do the LC 0001. Two Sum problem.
The presum_dict stores (presum --> how many times the presum occurs).
O(NW), where N is len(nums) and W is the width of the range we want to query.
"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presums = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presums[i+1] = presums[i] + nums[i]
        
        presum_dict = collections.defaultdict(int)   # key is presum, val is how many times the presum occurs
        cnt = 0
        for presum in presums:
            for target in range(lower, upper + 1):
                cnt += presum_dict[presum - target]
            presum_dict[presum] += 1
            
        return cnt
            
            
"""
面试第一反应就应该是solution 1, 如果面试官说[lower, upper] range is very large much larger than N, 
then we might consider the following solution prefix_sum + merge_sort.
"""
            
"""
solution 2: prefix_sum + merge_sort
在conquer 的 while loop之前，我们用一个while loop to compare lower <= (right[j] - left[i]) <= upper to update self.res
"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        
        self.cnt = 0
        self.lower = lower
        self.upper = upper
        self._merge_sort(presum)
        return self.cnt
    
    def _merge_sort(self, presum):
        if len(presum) == 0:
            return presum
        if len(presum) == 1:
            return presum
        
        # divide
        mid = len(presum) // 2
        left = self._merge_sort(presum[:mid])
        right = self._merge_sort(presum[mid:])
        
        # conquer 之前用一个while loop去更新res
        # 由于我们想要 right[j] - left[i] 在一个范围内，i 和 j 都在变的话就不太好比较, 我们固定i, 移动j来看多少right[j] - left[i]落在想要的范围内
        for i in range(len(left)):
            for j in range(len(right)):
                self.cnt += 1 if self.lower <= right[j] - left[i] <= self.upper else 0
        
        # conquer
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                presum[k] = left[i]
                i += 1
                k += 1
            else:
                presum[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            presum[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            presum[k] = right[j]
            j += 1
            k +=1
            
        return presum
            
          

"""
跟solution 2一样，我们把update cnt的函数优化成sliding window, 这样更快一些
"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        
        self.cnt = 0
        self.lower = lower
        self.upper = upper
        self._merge_sort(presum)
        return self.cnt
    
    def _merge_sort(self, presum):
        if len(presum) == 0:
            return presum
        if len(presum) == 1:
            return presum
        
        # divide
        mid = len(presum) // 2
        left = self._merge_sort(presum[:mid])
        right = self._merge_sort(presum[mid:])
        
        # conquer 之前用一个while loop去更新res
        # 由于我们想要 right[j] - left[i] 在一个范围内，i 和 j 都在变的话就不太好比较
        # 我们固定i, 移动j来看多少right[j] - left[i]落在想要的范围内
        p, q = 0, 0
        for i in range(len(left)):
            # 我们固定i, 移动两根指针p, q来形成sliding window
            while p < len(right) and right[p] - left[i] < self.lower:
                p += 1
            while q < len(right) and right[q] - left[i] <= self.upper:
                q += 1
            self.cnt += q - p
        
        # conquer
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                presum[k] = left[i]
                i += 1
                k += 1
            else:
                presum[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            presum[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            presum[k] = right[j]
            j += 1
            k +=1
            
        return presum




"""
solution 3: prefix_sum + segment_tree
Firstly, create a list to store all the prefix sum; then sort the prefix sum list
Secondly, use the sorted prefix sum list to build a segment tree, the tree node has an attribute self.cnt representing the cnt
of how many prefix sums are in a certain range. 
Finally, we traverse the prefix sum list and query how many prefix sums are there in range [prefix-upper, prefix-lower].
eg if there is one prefix_1 in range [prefix-upper, prefix-lower], then prefix - prefix_1 is in range [lower, upper]
"""
class SegmentTree:
    
    def __init__(self, start, end):
        self.start = start  # start is actual number
        self.end = end
        self.cnt = 0     # cnt is how many numbers are there in range [start, end]
        self.left = None
        self.right = None
        
    def build(self, start_idx, end_idx, arr):
        """
        我去，这里debug了两个小时，最后发现过不了的case是[2147323,-2147433,-1,0]，这是因为数字很大，所以只能用prefix_sums_sorted的idx来build tree,
        而不能像0248.Count-of-Smaller-Number那样用实际value去build一个tree, 不然tree会非常大，导致TLE, MLE.
        """
        if start_idx > end_idx:
            return None
        
        root = SegmentTree(arr[start_idx], arr[end_idx])
        if start_idx == end_idx:
            return root
        
        mid_idx = start_idx + (end_idx - start_idx) // 2
        root.left = self.build(start_idx, mid_idx, arr)
        root.right = self.build(mid_idx + 1, end_idx, arr)
        
        return root
    
    def update(self, root, num):
        if not root:
            return 
        
        if num < root.start or num > root.end:
            return

        if root.start <= num <= root.end:
            root.cnt += 1
            self.update(root.left, num)
            self.update(root.right, num)
            
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
        
        if start <= root.start and end >= root.end:
            return root.cnt
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)
    
    
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        
        # step 1: create a list to store the prefix sums, and then sort the list
        lens = len(nums)
        prefix_sums = [0] * (lens + 1)
        for i in range(1, lens + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        
        prefix_sums_sorted = sorted(list(set(prefix_sums)))  # 不但必须sort, 而且还必须转换成set去重
        
        # step 2: build a segment tree for the prefix_sums
        segment_tree = SegmentTree(prefix_sums_sorted[0], prefix_sums_sorted[-1])
        root = segment_tree.build(0, len(prefix_sums_sorted) - 1, prefix_sums_sorted)
        
        # step 3: update the segment tree by putting the prefix sum into the tree one by one, 
        # and do query are the same time  -  O(NlogN)
        res = 0
        for prefix in prefix_sums:     # 注意这里不能用去重排序的prefix_sums_sorted！
            res += segment_tree.query(root, prefix - upper, prefix - lower)        
            segment_tree.update(root, prefix)       # should do query first, then do update
            
        return res
