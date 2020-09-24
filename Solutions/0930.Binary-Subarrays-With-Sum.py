"""
930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""


"""
(number of subarrays having sum S) = (number of subarrays having sum at most S) - (number of subarrays having sum at most S-1)
at most problem让前面的指针去追后面的指针
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], target: int) -> int:
        return self._at_most(nums, target) - self._at_most(nums, target - 1)
    
    def _at_most(self, nums, target):
        cnt = 0
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums += nums[j]         # 不管是哪种模板，都是先更新后面的指针
            
            while i <= j and sums > target:     # 用 i < j 也可以
                sums -= nums[i]     # 再更新前面的指针
                i += 1
            
            if sums <= target:      # 更新res
                cnt += j - i + 1
            
        return cnt
