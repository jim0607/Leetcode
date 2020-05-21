#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (27.98%)
# Likes:    5735
# Dislikes: 859
# Total Accepted:    576K
# Total Submissions: 2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#



"""find the kth smallest element
O(log(M+N)), O(log(M+N))"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens = len(nums1) + len(nums2)
        if lens % 2 == 1:
            return self.kthSmallest(nums1, nums2, lens//2)
        else:
            return ( self.kthSmallest(nums1, nums2, lens//2 - 1) + self.kthSmallest(nums1, nums2, lens//2) ) / 2.0
        
    def kthSmallest(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        midIdx1, midIdx2 = len(nums1)//2, len(nums2)//2
        
        # when k is relatively large, then we can safely drop the first half that are surely smaller than the kth
        # the question is where is the first half that are surely smaller than the kth?
        # by comparing midVal1 and midVal2, we can find it out
        # if midVal1 < midVal2, then all the vals in nums1[:midIdx1] are less than midVal2 
        # also all of those vals are less than kth, we can safely drop all those vals
        if k > midIdx1 + midIdx2:
            if nums1[midIdx1] < nums2[midIdx2]:
                return self.kthSmallest(nums1[midIdx1 + 1:], nums2, k - midIdx1 - 1)
            else:
                return self.kthSmallest(nums1, nums2[midIdx2 + 1:], k - midIdx2 - 1)
            
        # when k is relatively small, then we can safely drop the second half that are surely larger than the kth
        # the question is where is the second half that are surely larger then the kth?
        # by comparing midVal1 and midVal2, we can find it out
        # if midVal1 > midVal2, then all the vals in nums1[midIdx1:] are larger than midVal2
        # also all of those vals are larger than kth, we can safely drop all those vals
        else:
            if nums1[midIdx1] > nums2[midIdx2]:
                return self.kthSmallest(nums1[:midIdx1], nums2, k)
            else:
                return self.kthSmallest(nums1, nums2[:midIdx2], k)
            



"""solution 2: binary search, O(log(min(M, N)), O(1)
看山景城一姐的视频4-7min中，其实只需要找nums1数组中的某个分割线，保证nums1分割线左边的数都是小于nums2分割线右边的数，
同时nums2分割线左边的数都是小于nums1分割线右边的数。我们假设分割线为nums1的分割线为mid1，也就是要保证nums1[mid1] < target, 
这里的target不是一个定值，而是运动的值: nums2[mid2 + 1]，因为mid1+mid2是等于(lens1+lens2+1)//2的，所以mid可以用mid1来表示。
所以这里就是类似的二分查找法来寻找最后一个nums1[mid1] < target, 也就是oooxxx问题了
somehow it is not easy to implement it with binary search的模板"""
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = 0 if not nums1 else len(nums1)
        n = 0 if not nums2 else len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            return (nums2[(n - 1) // 2] + nums2[n // 2]) / 2.0
        
        A_startK, A_endK = 0, m   # 每次binary search的范围
        cutA, cutB = 0, 0       # 分别记录A，B分割线的左边的元素个数

        while A_startK <= A_endK:
            cutA = (A_endK + A_startK) // 2
            cutB = (m + n + 1) // 2 - cutA

            L1 = -float("inf") if cutA == 0 else nums1[cutA - 1]
            L2 = -float("inf") if cutB == 0 else nums2[cutB - 1]
            R1 = float("inf") if cutA == m else nums1[cutA]
            R2 = float("inf") if cutB == n else nums2[cutB]

            # 二分
            if L1 > R2:
                A_endK = cutA - 1 
            elif L2 > R1:
                A_startK = cutA + 1
            else:
                if (m + n) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                else:
                    return max(L1, L2) / 1.0
        
# @lc code=end


"""solution 1: similar with merge two sorted array, trivial solution
O(k), k = (m+n)/2"""
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = 0 if not nums1 else len(nums1)
        n = 0 if not nums2 else len(nums2)
        mid = (m + n) // 2 
        if (m + n) % 2 != 0:
            return self.findKth(nums1, nums2, mid) / 1.0
        else:
            return (self.findKth(nums1, nums2, mid) + self.findKth(nums1, nums2, mid - 1)) / 2.0

    # return the Kth smallest element in nums1 and nums2.  O(k)
    def findKth(self, nums1, nums2, k):
        lens1 = 0 if not nums1 else len(nums1)
        lens2 = 0 if not nums2 else len(nums2)
        i, j = 0, 0
        res = 0
        while k >= 0:
            if (i < lens1 and j < lens2 and nums1[i] < nums2[j]) or j >= lens2:
                res = nums1[i]
                i += 1
            elif (i < lens1 and j < lens2 and nums1[i] >= nums2[j]) or i >= lens1:
                res = nums2[j]
                j += 1
            if k == 0:
                return res
            k -= 1
        
# @lc code=end
