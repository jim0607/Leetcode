410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.


"""
If we can divide nums so that the minimum subarray sum is mid, we can also divide nums so that the minimum subarray sum is larger than mid.
So this is a OOXX problem.  The difficult part is to check if mid is valid.
We use greedy algorithm to do that.
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = 0, sum(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._is_valid(nums, mid, m):
                end = mid
            else:
                start = mid
            
        return start if self._is_valid(nums, start, m) else end
    
    def _is_valid(self, nums, max_sum, m):
        cnt = 1     # how many pieces we should cut in order to make sure every subarray sum less than max_sum
        curr_sum = 0
        for num in nums:
            if num > max_sum:
                return False
            
            curr_sum += num
            if curr_sum > max_sum:
                cnt += 1
                curr_sum = num
                
        return cnt <= m
