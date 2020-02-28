#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (44.65%)
# Likes:    1258
# Dislikes: 56
# Total Accepted:    241.5K
# Total Submissions: 539.4K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # 先排序，后面才可以进行比较nums[i] == nums[i-1]去重
        res = [] 
        self.dfs(nums, 0, [], res)
        
        return res
    
    def dfs(self, nums, startIndex, curr, res):
        res.append(curr.copy())
        
        for i in range(startIndex, len(nums)):
            # [1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，
            # 如果不是挨着前面那个2选的，也就是说i != startIndex，那么就不要放后面那个2，
            # 这样会造成重复出现[1,第一个2],[1,第二个2]
            # 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。
            if i != 0 and nums[i] == nums[i-1] and i != startIndex:
                continue
            curr.append(nums[i])
            self.dfs(nums, i + 1, curr, res)
            curr.pop()
      
# @lc code=end


写法二：用花花的写法
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # 先排序，后面才可以进行比较nums[i] == nums[i-1]去重
        res = [] 
        n = len(nums)
        for length in range(n + 1):
            self.dfs(nums, length, 0, [], res)
        
        return res

    def dfs(self, nums, length, startIndex, curr, res):
        if len(curr) == length:
            res.append(curr.copy())
            return
        
        for i in range(startIndex, len(nums)):
            # [1, 2, 2]的遍历中，如果之前的那个2没被放进去（i != startIndex），那么就不要放后面那个2，这样会造成重复。
            if i !=0 and nums[i] == nums[i-1] and i != startIndex:
                continue
            curr.append(nums[i])
            self.dfs(nums, length, i + 1, curr, res)
            curr.pop()

        
# @lc code=end

