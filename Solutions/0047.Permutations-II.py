#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (43.44%)
# Likes:    1476
# Dislikes: 51
# Total Accepted:    299.4K
# Total Submissions: 686.9K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
"""
输入数组中带重复元素的permutation
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()         # !!!!!输入里面有重复，都需要先把数组排序一下
        
        self.res = []
        self.visited = set()
        self.dfs(nums, [])
        
        return self.res
    
    def dfs(self, nums, curr):
        if len(curr) == len(nums):
            self.res.append(curr.copy())
            
        for i in range(len(nums)):
            if i in self.visited:
                continue
            # 如果nums[i]这个数与它前一个数是一样的但是前一个数并没有放进去，那就不要把这个数放进去了，因为我们是优先放前面的那个数。
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in self.visited:
                continue
                
            curr.append(nums[i])
            self.visited.add(i)
            
            self.dfs(nums, curr)
            
            curr.pop()
            self.visited.remove(i)
            
            
            
            
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(nums):
                res.append(curr_comb.copy())
                return
            for next_idx in range(len(nums)):
                if next_idx > 0 and nums[next_idx] == nums[next_idx-1] and next_idx - 1 not in visited:
                    continue
                if next_idx in visited:
                    continue
                visited.add(next_idx)
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_comb)
                curr_comb.pop()
                visited.remove(next_idx)            
        
        res = []
        nums.sort()         # 去重第一步 - sort the list
        visited = set()
        backtrack(0, [])
        return res
