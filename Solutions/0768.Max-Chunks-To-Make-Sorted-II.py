"""
768. Max Chunks To Make Sorted II

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, 
the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), 
and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
"""


"""
Maintain two sums, one for arr, one for sorted arr.
for num_1, num_2 in zip(arr, sorted(arr)): if sum_1 == sum_2: cnt += 1.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        sum_1, sum_2 = 0, 0
        for num_1, num_2 in zip(arr, sorted(arr)):
            sum_1 += num_1
            sum_2 += num_2
            if sum_1 == sum_2:
                cnt += 1
        return cnt
