"""
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



"""
if we can split the arr to realize s as it's max_sum, then we can spit is to realize > s as it's max_sum. So it is a XXXOOO problem to find the first O.
binary search on the max_sum.
helper function return whether or not the max_sum <= mid.
if yes, drop the right part, else drop the left part
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_possible(nums, mid, k):
                end = mid
            else:
                start = mid
        return start if self.is_possible(nums, start, k) else end
    
    def is_possible(self, nums, max_sum, k):
        """
        return whether or not it is possible to spit the arr, so that the max sum the m subarrays is smaller than max_sum
        greedy: whenever we are about to get a sum larger than s, we stop and split
        """
        sub_cnt = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > max_sum:
                sub_cnt += 1
                curr_sum = 0
            curr_sum += num
        return sub_cnt <= k



"""
If we can divide nums so that the minimum subarray sum is mid, we can also divide nums so that the minimum subarray sum is larger than mid.
So this is a OOXX problem.  The difficult part is to check if mid is valid.
We use greedy algorithm to do that.
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_split(nums, m, mid):
                end = mid
            else:
                start = mid
        return start if self._can_split(nums, m, start) else end
    
    def _can_split(self, nums, m, max_sum):
        """
        Return if we can split nums into m subarrays with with each subarray has sum less than max_sum
        """
        cnt = 0
        i = 0
        while i < len(nums):
            curr_sum = 0
            while i < len(nums) and curr_sum + nums[i] <= max_sum:
                curr_sum += nums[i]
                i += 1
            cnt += 1
        return cnt <= m






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
