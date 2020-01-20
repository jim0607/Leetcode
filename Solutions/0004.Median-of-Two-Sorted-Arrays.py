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


#
"""solution 2: binary search, O(log(k)), k = min(m, n)
解法来自 山景城一姐"""
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
