"""
137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""



"""
可以建立一个 32 位的数字，来统计每一位上1出现的个数，如果某一位上为1的话，那么如果该整数出现了三次，对3取余为0，
这样把每个数的对应位都加起来对3取余，最终剩下来的那个数就是单独的数字。
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            sum_at_i = 0
            for num in nums:
                bit_at_i = num >> i & 1     # num >> i get the bit at ith position
                sum_at_i += bit_at_i
                
            sum_at_i = sum_at_i % 3
            res |= sum_at_i << i
            
        if ( res & (1 << 31) ) == 0:    # if it's a positive number
            return res
        else:                           # handle for negative number
            return -( (res^(0xFFFF_FFFF))+1 )
