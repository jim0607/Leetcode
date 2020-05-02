674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 


"""给定一个序列，求子序列的最大值问题：典型的坐标型动态规划问题
dp[i]表示以i结尾的最长子序列"""
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
           
        return max(dp)
"""    

"""dp[i] 只与 dp[i - 1]有关，所以可以空间优化成O(1)"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lens = len(nums)
        if lens == 1:
            return lens
        
        curr = 1
        res = 1
        
        for i in range(1, lens):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            
            res = max(res, curr)
                
        return res


"""two pointers, one act as an anchor"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        res, anchor = 1, 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                anchor = i
            res = max(res, i - anchor + 1)
        
        return res
