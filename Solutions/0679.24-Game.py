679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.


"""
recursively 'glue' 2 numbers as a new number, and try to make 24 with the new nums list.
at the end, when len(nums) = 1, check if it is 24 (due to division some precision loss should be expected, here set as 1e-4).
Time complexity is number of possible combinations - O(9216)
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True if abs(nums[0] - 24) < 10**(-4) else False
        
        # 选两个数做运算
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                candidates = []         # 把两个数运算所能产生的结果放到一个List中
                candidates.append(nums[i]+nums[j])
                candidates.append(nums[i]*nums[j])
                candidates.append(nums[i]-nums[j])
                candidates.append(nums[j]-nums[i])
                if nums[i] != 0:
                    candidates.append(nums[j]/nums[i])
                if nums[j] != 0:
                    candidates.append(nums[i]/nums[j])
                    
                # backtrack for neighbors
                for candidate in candidates:
                    # remove nums[i] and nums[j] in the next_nums, and put candidate in next_nums
                    next_nums = [candidate] + nums[:i] + nums[i+1:j] + nums[j+1:]   
                    if self.judgePoint24(next_nums):
                        return True
                    
        return False
