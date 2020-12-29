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
for [4,7,9,10], how many number are missing between 4 and 10?
there should be 10-4-1 = 5 numbers between 4 and 10 if nothing is missing,
however, now there are only 3-0-1 = 2 numbers between 4 and 10.
so the total number that are missing between 4 and 10 is 5-2 = 3.
total number missing between i and j is (nums[j] - nums[i]) - (j - i).

how do we determine to drop left or to drop right in binary search?
if the total_number_missing_between_mid_and_0 is more than k, so we drop right.
else we drop left.
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        missing_cnt_from_end_to_start = (nums[n-1] - nums[0]) - (n - 1)     # if k is too very large
        if k > missing_cnt_from_end_to_start:
            return nums[n-1] + k - missing_cnt_from_end_to_start
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] - nums[0] - mid >= k:
                end = mid
            else:
                start = mid
        
        return nums[start] + k - (nums[start] - nums[0] - start)
