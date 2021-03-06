"""
1099. Two Sum Less Than K

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
"""



"""
Solution 1: sort the array and then use two pointers to do the two sum problem
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], target: int) -> int:
        max_sum = float("-inf")
        nums.sort()       # O(nlogn)
        i, j = 0, len(nums) - 1
        while i < j:
            sums = nums[i] + nums[j]
            if sums < target:
                max_sum = max(max_sum, sums)
                i += 1
            else:
                j -= 1
        return max_sum if max_sum != float("-inf") else -1
