Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
             
             
"""dp 解法很难懂，令狐冲九章算法的带memo recursion很好懂
https://www.jiuzhang.com/solutions/burst-ballons/#tag-highlight-lang-python"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = [1] + nums + [1]
        lens = len(nums)
        
        return self.memoSearch(nums, 0, lens - 1, {})
    
    def memoSearch(self, nums, i, j, memo):
        """
        return the maxCoins we can get bursting (i, j) not including i and j
        """
        if i == j:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        maxCoins = 0
        for k in range(i + 1, j):
            left = self.memoSearch(nums, i, k, memo)
            right = self.memoSearch(nums, k, j, memo)
            
            # 因为是先burst left and right, 最后conquer, 所以conquer的时候只剩下nums[i] and nums[j], 所以是 nums[i] * nums[k] * nums[j]
            maxCoins = max(maxCoins, left + right + nums[i] * nums[k] * nums[j])
        
        memo[(i, j)] = maxCoins
        
        return maxCoins
