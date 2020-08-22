#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (51.40%)
# Likes:    2814
# Dislikes: 208
# Total Accepted:    505.3K
# Total Submissions: 974.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
"""use quick select method
Python quick select (use partition) average time O(N) and worst O(N^2)"""



"""  Celia's template for partition  """
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return None

        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]      # 一定要心里记着partition function return的是什么

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]



"""solution 2: heap
time: O(NlogK), N 来自于for循环，logK来自于heap的长度是K，heap 的push 和pop都是logK
heapq适合做第K大，第K小，前K大，前K小问题"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        
        numsHeapq = []
        
        for num in nums:
            heapq.heappush(numsHeapq, num)
            if len(numsHeapq) > k:
                heapq.heappop(numsHeapq)    # python默认是最小堆, 每次都是pop出最小值, 于是留下来的就是最大值了
                
        return numsHeapq[0]

    
    
"""下面是另一种写法"""
"""
maintain a min heap with k size
"""
from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [-num for num in nums]
        heapify(hq)
        for _ in range(k - 1):
            heappop(hq)
        return -heappop(hq)
