#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.40%)
# Likes:    939
# Dislikes: 1305
# Total Accepted:    94.8K
# Total Submissions: 388.1K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
# 
# 
# Example 2:
# 
# 
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
# 
# 
# 
# 
# Note:
# 
# 
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
# 
# 
#

# @lc code=start
"""
solution 3: prefixSum + hashmap
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)
        pre_sum_dict[0] = -1      # pre_sum --> idx, 注意initial position should be -1
        
        if k == 0:      # k = 0 和 k!= 0 分开讨论
            for i, num in enumerate(nums):
                pre_sum += num
                
                # if pre_sum in pre_sum_dict is same as pre_sum_j - pre_sum_i = 0
                # if i - pre_sum_dict[pre_sum - k] >= 2 is to make sure the subarray size is at least 2
                if pre_sum - k in pre_sum_dict and i - pre_sum_dict[pre_sum - k] >= 2:
                    return True
                if pre_sum not in pre_sum_dict:     # 注意这里只有在pre_sum不在pre_sum_dict才更新pre_sum_dict[pre_sum], 
                    pre_sum_dict[pre_sum] = i       # 否则不更新，这是为了保证pre_sum_dict[pre_sum]尽可能小，来满足i - pre_sum_dict[pre_sum - k] >= 2
        
        else:
            for i, num in enumerate(nums):
                pre_sum += num
                pre_sum = pre_sum % k       # (a-b)%x = a%x - b%x
                
                # if pre_sum in pre_sum_dict is same as pre_sum_j % k - pre_sum_i % k = 0
                if (pre_sum - k) % k in pre_sum_dict and i - pre_sum_dict[(pre_sum - k) % k] >= 2:
                    return True
                if pre_sum not in pre_sum_dict:
                    pre_sum_dict[pre_sum] = i
           
        return False


    


"""
"""solution 1: brutal force: O(N^3), O(1)"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lens = len(nums)
        if lens < 2:
            return False
        
        for j in range(1, lens + 1):
            for i in range(j - 1):
                if k == 0:
                    if sum(nums[i:j]) == 0:
                        return True
                else:
                    if sum(nums[i:j+1]) % k == 0:
                        return True
        return False"""

 

# @lc code=start
"""solution 2: prefixSum"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lens = len(nums)
        if lens < 2:
            return False
        
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        for j in range(1, len(prefixSum) - 1):
            for i in range(j):
                subArrSum = prefixSum[j+1] - prefixSum[i]   # (i~j包括i,j)的subArr的subArrSum是prefixSum[j+1] - prefixSum[i]
                if k == 0:
                    if subArrSum == 0:
                        return True
                else:
                    if subArrSum % k  == 0:
                        return True 
        
        return False


