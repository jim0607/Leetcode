"""
698. Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""



"""
套backtrack模板即可，backtrack里面需要传入(curr_sum, curr_idx, curr_cnt).
结束条件是已有curr_cnt=k段满足条件了. 
Time complexity: we basically iterate over nums and for each element either use it or drop it, 
which is O(2^n). We are doing the same for each subset. Total subsets are k. 
So Time Complexity becomes O(k*(2^n))
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(curr_idx, curr_sum, curr_cnt):
            if curr_cnt == k:       # 结束条件是已有curr_cnt=k段满足条件了
                return True
            if curr_cnt > k:        # 提前return False - strong pruning
                return False
            
            if curr_sum == target:  # 拼出一段之后，从头开始去拼下一段
                return backtrack(-1, 0, curr_cnt + 1)
            if curr_sum > target:   
                return False

            for next_idx in range(curr_idx + 1, len(nums)):   # 去后面找数来拼凑 - O(2^N)
                if next_idx in visited: # 正因为拼出一段之后，需要从"头!!"开始去拼下一段，所以需要visited
                    continue
                    
                visited.add(next_idx)
                if backtrack(next_idx, curr_sum + nums[next_idx], curr_cnt):
                    return True
                visited.remove(next_idx)
            
            return False       
            
            
        if k == 1:
            return True
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        if max(nums) > target:
            return False
        
        visited = set()
        return backtrack(-1, 0, 0)
