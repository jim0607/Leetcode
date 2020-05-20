#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (56.83%)
# Likes:    2719
# Dislikes: 64
# Total Accepted:    462.1K
# Total Submissions: 810.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

"""C(m, n)：m个里面找出n个的组合问题
模板的DFS + back tracking求combination问题
O(N*S), S是solution的个数，这里S=2^N
O(N*S) to generate all subsets and then copy them into output list."""
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.dfs(nums, 0, [], res)
        
        return res
    
    def dfs(self, nums, startIndex, curr, res):
        """递归的定义：从nums中的startIndex位置开始，挑选一些数，放到curr中，然后存入res里面，看输出的数组就可以理解程序的执行顺序了"""
        res.append(curr.copy())                 # has to be a deep copy O(N)
        # 这个for循环里curr一直在重复append和pop，[1, 2] -> [1] -> [1, 3] -> [1] -> [1, 4]......
        # 这就是为什么用back tracking了
        for i in range(startIndex, len(nums)):
            curr.append(nums[i])                # [1] -> [1, 2]
            self.dfs(nums, i + 1, curr, res)    # 从nums中的start位置开始，挑选一些数，放到curr（此时为[1,2]）中，然后存入res里面。这就相当于把所有的以[1, 2]开头的子集都找到，且放进res里面
            curr.pop()                          # [1, 2] -> [1]，然后在进入for循环，然后curr再append 2后面的数 3, curr 变成[1, 3]，然后......周而复始，直至for循环结束。

            
"""
不传入res到dfs的参数里面，用self.res去类似打擂台之类的就可以了。
"""           
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        self.dfs(nums, 0, [])
        
        return self.res
    
    def dfs(self, nums, startIdx, curr):
        self.res.append(curr.copy())
        
        for i in range(startIdx, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, i + 1, curr)
            curr.pop()
        
        
        
        
        
        

            
模板二：花花的模板，更加通用化，可以通过比较输出结果的数组排列顺序直到区别。
上面程序的输出是[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
下面程序的输出是[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""模板的DFS + back tracking求combination问题"""
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for length in range(n + 1):
            self.dfs(nums, length, 0, [], res)
        
        return res

    def dfs(self, nums, length, index, curr, res):
        if len(curr) == length:
            res.append(curr.copy())
            return
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, length, i + 1, curr, res)
            curr.pop()


# @lc code=end

