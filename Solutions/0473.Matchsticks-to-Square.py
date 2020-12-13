"""
473. Matchsticks to Square

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
"""



class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        def backtrack(curr_idx, curr_sum, curr_cnt):
            if curr_cnt == 4:       # 如果拼出了四段target, 那说明就成功了
                return True
            
            if curr_sum > target:   # 提前return False - strong pruning
                return False
            
            if curr_sum == target:  # 拼出一段之后，从头开始去拼下一段
                return backtrack(-1, 0, curr_cnt + 1)   # 拼出一段之后，从头开始去拼下一段
            
            if curr_sum < target:
                for next_idx in range(curr_idx + 1, len(nums)): # 去后面找数来拼凑 - O(2^N)
                    if next_idx in visited:
                        continue
                    visited.add(next_idx)
                    if backtrack(next_idx, curr_sum + nums[next_idx], curr_cnt):
                        return True
                    visited.remove(next_idx)
                    
            return False
        
        
        sums = sum(nums)
        if len(nums) < 4 or sums % 4 != 0:
            return False
        target = sums // 4
        
        visited = set()
        return backtrack(-1, 0, 0)
