487. Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.



"""
sliding window solution: find the longest subarray with at most one 0.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_lens = 0
        j = 0
        cnt = 0
        for i in range(len(nums)):
            while j < len(nums) and cnt <= 1:
                if nums[j] == 0:    # 更新带有j的信息
                    cnt += 1
                j += 1
                
            # 更新res if 满足条件
            if cnt <= 1:
                max_lens = max(max_lens, j - i)     # 更新res
            else:
                max_lens = max(max_lens, j - i - 1)
                
            # 更新带有i的信息
            if nums[i] == 0:
                cnt -= 1          
                
        return max_lens
        
        

"""
Follow up:
What if the input numbers come in one by one as an infinite stream? 
In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. 
Could you solve it efficiently?
"""
"""
In answering the follow up question, sliding window solution is not ideal, we use solution 2 which is quite smart!
"""
"""
solution 2: record prev_lens and curr_lens for the previous lens of consecutive 1s and curr lens of consecutive 1s.
update them we there is a new 0 coming, otherwise curr_lens += 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_lens, curr_lens = -1, 0        # note that prev_lens is initialized to -1, meaning that we haven't seen any 0 yet
        max_lens = 0
        for num in nums:
            if num == 1:
                curr_lens += 1
            else:
                prev_lens, curr_lens = curr_lens, 0
            max_lens = max(max_lens, prev_lens + 1 + curr_lens)
        return max_lens
