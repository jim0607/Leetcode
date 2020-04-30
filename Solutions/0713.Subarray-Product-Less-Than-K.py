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
Note that the numbers are positive, so the prefixProd will be an increasing arr.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        lens = len(nums)
        if k <= 1:
            return 0
        if lens == 1:
            return 1 if k == nums[0] else 0
        
        res = 0
        i = 0
        prod = 1
        for j in range(lens):                       
            prod *= nums[j]
        
            while i <= j and prod >= k:
                prod = prod / nums[i]
                i += 1
                
            if prod < k:
                res += j - i + 1

        return res
