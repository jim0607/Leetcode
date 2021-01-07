"""
769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), 
and individually sort each chunk.  After concatenating them, the result equals the sorted array.

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



"""
similar with 45. Jump Game, define a curr_must_reach and next_must_reach.
if next_must_reach == curr_must_reach, we can cut it.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_must_reach = arr[0]
        next_must_reach = arr[0]
        cnt = 0
        i = 0
        while i < len(arr):
            while i <= curr_must_reach:
                next_must_reach = max(next_must_reach, arr[i])
                i += 1

            if next_must_reach == curr_must_reach:
                cnt += 1
                if i < len(arr):
                    curr_must_reach = arr[i]
                    next_must_reach = arr[i]
                
            else:
                curr_must_reach = next_must_reach
            
        return cnt
