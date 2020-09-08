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
方法：两个for loop在nums中取两个数nums[i] and nums[j]. 算出nums[i] and nums[j]这两个数加减乘除可能得到的数，
将这些可能得到的数放进next_nums里面进行递归。递归的结束条件是len(nums)==1即无法再跟其他书加减乘除了。
如果len(nums)==1 and nums[0]==24, then return True
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1 and abs(nums[0] - 24) < 10**(-4):
            return True
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                calculated = []     # 存nums[i] and nums[j]这两个数加减乘除可能得到的数
                calculated.append(nums[i] + nums[j])
                calculated.append(nums[i] - nums[j])
                calculated.append(-nums[i] + nums[j])
                calculated.append(nums[i] * nums[j])
                if nums[i] != 0:
                    calculated.append(nums[j] / nums[i])
                if nums[j] != 0:
                    calculated.append(nums[i] / nums[j])
                
                for cal in calculated:
                    # 把calculated的数放进next_nums, 同时把nums[i], nums[j]移除next_nums
                    next_nums = nums[:i] + nums[i+1:j] + nums[j+1:] + [cal]  
                    if self.judgePoint24(next_nums):
                        return True
                    
        return False
