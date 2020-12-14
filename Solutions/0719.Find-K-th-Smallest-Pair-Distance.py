"""
719. Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. 
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""



"""
sort the list, then it becomes [1,1,3,4,8,8,9].
let helper function return if there is more than k distance smaller than mid.
we use two pointers to go through the list to check if there is more than k distance smaller than mid.
The algorithm of helper function is sliding window so it's only O(N)
"""
"""
sort the nums
binary search on distance
helper function returns if there are k distances smaller than mid
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()         # sort nums first
        
        start, end = 0, nums[-1] - nums[0]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._there_are_more_than_k(nums, mid, k):
                end = mid
            else:
                start = mid
        
        return start if self._there_are_more_than_k(nums, start, k) else end
    
    def _there_are_more_than_k(self, nums, dist, k):
        """
        return if there are k or more than k distances smaller than of equals mid
        套用at most problem的模板即可 - O(N)
        """
        cnt = 0
        i = 0
        for j in range(1, len(nums)):
            while i < j and nums[j] - nums[i] > dist:
                i += 1
            
            if i < j and nums[j] - nums[i] <= dist:
                cnt += j - i
                
        return cnt >= k
