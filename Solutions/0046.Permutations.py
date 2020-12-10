#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (59.12%)
# Likes:    2843
# Dislikes: 90
# Total Accepted:    488.6K
# Total Submissions: 823.4K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
"""
permutation的模板：
首先判断这题题目是顺序相关的，所以是不需要startIndex的Subsets问题了。
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(nums):
                res.append(curr_comb.copy())
                return
            
            for next_idx in range(len(nums)):
                if next_idx not in visited:
                    visited.add(next_idx)
                    curr_comb.append(nums[next_idx])
                    backtrack(next_idx, curr_comb)
                    curr_comb.pop()
                    visited.remove(next_idx)
            
            
        res = []
        visited = set()
        backtrack(0, [])
        return res





class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        
        self.dfs(nums, [], res)     # 与combination相比少了一个startIndex参数

        return res

    def dfs(self, nums: List[int], curr: List[int], res: List[List[int]]):
        # 2. 递归的出口
        if len(curr) == len(nums):
            res.append(curr.copy())     # deep copy
            return

        for i in range(len(nums)):      # O(N)
            # 与combination相比多了这个if判断，这是因为在combination中有startIndex限制其职能从i+1后面找
            # 这里没有startIndex，每次都是从0开始找，可以找到自己，最后可能会输出[1,1,1]或[1,1,2]，显然不是[1,2,3]的permutation
            # 所以这个if是为了限制一个数只出现一次。
            if nums[i] in curr:         # O(N), so overall O(N*S), S=solution=N!
                continue
            curr.append(nums[i])
            self.dfs(nums, curr, res)
            curr.pop()
          
# @lc code=end


写法二：将时间复杂度降为O(S)，方法是将if nums[i] in curr这个判断语句降为O(1),用一个hashmap标记已经visited的元素，这样就不会让同一个元素被用到两次了。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.visited = set()    # 与combination相比加入visited用于防止重复出现
        self.dfs(nums, [])      # 与combination相比少了一个startIndex参数
        return self.res
    
    def dfs(self, nums, curr):
        if len(curr) == len(nums):
            self.res.append(curr.copy())    # deep copy
            return
        
        for i in range(len(nums)):
            # 与combination相比多了这个if判断，这是因为在combination中有startIndex限制其职能从i+1后面找
            # 这里没有startIndex，每次都是从0开始找，可以找到自己，最后可能会输出[1,1,1]或[1,1,2]，显然不是[1,2,3]的permutation
            # 所以这个if是为了限制一个数只出现一次。
            if i in self.visited:       # O(1), so overall O(S), S=solution=N!
                continue
                
            curr.append(nums[i])        # append之后需要将i add到visited中
            self.visited.add(i)
            
            self.dfs(nums, curr)
            
            curr.pop()
            self.visited.remove(i)      # pop出来之后将i从visited中remove走
