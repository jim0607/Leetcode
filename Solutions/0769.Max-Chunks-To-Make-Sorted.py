769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


"""
Iterate the array, if the max(A[0] ~ A[i]) = i, then we can cut it at this index.,
so that it the chunk ended with i.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        curr_max = arr[0]
        for i, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if curr_max == i:
                cnt += 1
                
        return cnt
