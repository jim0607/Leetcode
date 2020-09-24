"""
713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""



"""
Note that the numbers are positive, so we can use sliding window.
套用at most problem的模板就可以了
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], target: int) -> int:
        prod = 1
        cnt = 0
        i = 0
        for j in range(len(nums)):
            prod *= nums[j]
            
            while i < j and prod >= target:
                prod = prod / nums[i]
                i += 1
                
            if prod < target:
                cnt += j - i + 1
                
        return cnt
