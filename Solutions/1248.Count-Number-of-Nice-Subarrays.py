1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


"""
This problem will be a very typical sliding window,
if it asks the number of subarrays with at most K distinct elements.
Just need one more step to reach the folloing equation:
exactly(K) = atMost(K) - atMost(K-1); 
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self._at_most_k(nums, k) - self._at_most_k(nums, k - 1)
        
    def _at_most_k(self, nums, k):
        res = 0
        cnt_odd = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:        # always update the pointer in the front first
                cnt_odd += 1
                
            while i <= j and cnt_odd > k:
                if nums[i] % 2 == 1:        
                    cnt_odd -= 1
                i += 1
            
            # 更新res - at most k
            if cnt_odd <= k:
                res += j - i
                
        return res
