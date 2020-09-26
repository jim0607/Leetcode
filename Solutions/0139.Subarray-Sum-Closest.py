"""
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Example1
Input: 
[-3,1,1,-3,5] 
Output: 
[0,2]
Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
Challenge: O(nlogn) time
"""


class Solution:
    def subarraySumClosest(self, nums):
        pre_sum = [(0, -1)]     # 注意pre_sum里面要把idx信息带上，不然一会儿sort了之后会丢掉
        for i in range(len(nums)):
            pre_sum.append((pre_sum[-1][0] + nums[i], i))
            
        pre_sum.sort(key = lambda x: x[0])   # 按照pre_sum values sort，这样最小的subArrSum就一定来自于相邻的两个prefix sum了
        
        min_diff = float("inf")
        res = [-1, 0]
        for i in range(1, len(pre_sum)):
            if pre_sum[i][0] - pre_sum[i-1][0] < min_diff:
                min_diff = pre_sum[i][0] - pre_sum[i-1][0]
                res = [min(pre_sum[i][1], pre_sum[i-1][1]) + 1, max(pre_sum[i][1], pre_sum[i-1][1])]
        return res
