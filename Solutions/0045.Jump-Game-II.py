"""
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""



"""
算法：第一步可以跳到比如位置10，也就是说0-10我们都可以一步跳到，那我们就在0-10这些位置中，
选一个位置i跳第二步，看看第二步能跳到最远的地方是哪里，比如是最远的是从位置6跳到位置28，那么就说明两步可以跳到位置28，
也就是说11-28我们可以通过两步跳到，那我们就继续在11-28这些位置中，选一个位置i跳第三步.........
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1
        
        i = 0
        curr_coverage = nums[0]     # 记录第一步能跳到的最远的地方
        cnt = 1
        while i < len(nums):
            next_coverage = curr_coverage
            for j in range(i, curr_coverage + 1):   # 在0-10这些位置中，选一个位置i跳第二步，看看第二步能跳到最远的地方是哪里
                next_coverage = max(next_coverage, j + nums[j])
            
            cnt += 1
            if next_coverage >= len(nums) - 1:      # check if reached destination already
                return cnt
            
            i = curr_coverage + 1
            curr_coverage = next_coverage
