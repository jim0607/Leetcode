719. Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

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
sort the list, then it becomes [1,1,3,4,8,8,9].
let helper function return if there is more than k distance smaller than mid.
we use two pointers to go through the list to check if there is more than k distance smaller than mid.
The algorithm of helper function is sliding window so it's only O(N)
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._has_more(nums, k, mid):
                end = mid
            else:
                start = mid
        return start if self._has_more(nums, k, start) else end
    
    def _has_more(self, nums, k, diff):
        """
        check if there is more than k dist that are smaller than diff
        """
        lens = len(nums)
        i, j = 0, 0
        cnt = 0
        while i < lens and j < lens:
            if j == i:
                j += 1
            while j < lens and nums[j] - nums[i] <= diff:
                cnt += j - i
                j += 1
            i += 1
        return cnt >= k
