1060. Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


"""
binary search: 这是google 7月份的面试题，这个题说明做过和没做过还是很不一样的，
最好还是多做一些题，刷到900是最好的状态！
"""
"""
[4,7,9,10]
     \
how many numbers are missing before position 2?
missing[idx] = 9 - 4 - 2 = 3 = nums[idx] - nums[0] - idx

定义一个function missing(idx) to find the number of number missing before idx. so that we can compare missing(mid) with k. 
Google真的把binary search 玩出花了！
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lens = len(nums)
        if k > self._missing(nums, (lens - 1)):
            return nums[-1] + (k - self._missing(nums, lens - 1))
        
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._missing(nums, mid) >= k:    # there are more than k numbers missing before mid idx
                end = mid
            else:
                start = mid

        # after the while loop, k should be between start and end
        return nums[start] + (k - self._missing(nums, start))  # 由于是往左逼，所以可以保证self._missing(start) <= k
        
        
    def _missing(slef, nums, idx):      # calculate how many numbers are missing before idx
        return nums[idx] - nums[0] - idx
