"""
992. Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) 
subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""




"""
exactly(K) = atMost(K) - atMost(K-1)
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._at_most(nums, k) - self._at_most(nums, k - 1)
    
    def _at_most(self, nums, k):
        num_to_cnt = collections.defaultdict(int)
        res = 0
        i = 0
        for j in range(len(nums)):
            num_to_cnt[nums[j]] += 1
            
            while i <= j and len(num_to_cnt) > k:
                num_to_cnt[nums[i]] -= 1
                if num_to_cnt[nums[i]] == 0:
                    del num_to_cnt[nums[i]]
                i += 1
                
            if len(num_to_cnt) <= k:
                res += j - i + 1
        
        return res
