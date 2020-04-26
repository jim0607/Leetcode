209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 



class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        
        minSize = float("inf")
        sums = 0
        j = 0
        # 下面是九章的模板
        for i in range(lens):
            while j < lens and sums < s:    # 满足条件 sums < s
                sums += nums[j]             # 更新 j
                j += 1
                
            if sums >= s:                   # 更新 res if 满足条件
                minSize = min(minSize, j - i)
                
            sums -= nums[i]                 # 更新 i
                
        return 0 if minSize == float("inf") else minSize
