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
def findKthLargest(self, nums: List[int], k: int) -> int:
    if not nums or k < 1 or k > len(nums):
        return None

    return self._quick_select(nums, 0, len(nums) - 1, len(nums) - k)

def _quick_select(self, nums, start, end, k):
    if start == end:    # 模板注意点1
        return nums[k]

    left, right = start, end
    pivot = nums[(start + end) // 2]
    while left <= right:    # 模板注意点2
        while left <= right and nums[left] < pivot:    # 模板注意点3
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1 
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    if k <= right:      # 模板注意点4
        return self._quick_select(nums, start, right, k)
    elif k >= left:     # 模板注意点5
        return self._quick_select(nums, left, end, k)
    else:
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
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = nums
        heapify(hq)
        
        while len(hq) > k:
            heappop(hq)
            
        return hq[0]
