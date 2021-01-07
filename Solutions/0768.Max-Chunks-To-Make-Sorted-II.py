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
O(N) solution: pre-calculation of left_max and right_min
Assume we have an array A of length n. The objective is to split A into as many chunks as possible, 
such that when we sort all these chunks and concatenate them, the result will be a fully sorted array in ascending order.
Notice that as we traverse A, we can split A at index i into A[:i+1] and A[i+1:] if and only if max(A[:i+1]) <= min(A[i+1:]). 
This to maintain the invariant that sorted(A[:i+1]) + sorted(A[i+1:]) == sorted(A).
Therefore, all we need to do is iterate over the array, and every time we encounter max(A[:i+1]) <= min(A[i+1:]), we split the array.
Now, suppose I split at some index i (where 0 <= i < n-1, and then save this index as begin := i. 
You may be thinking, on the next iteration, I should be comparing max(A[begin : i+1] with min(A[i+1:]) instead of max(A[:i+1]) with min(A[i+1]:).
However, notice that both max_val and min_val must be sorted in ascending order (just look at how they're created). 
So, by definition max(A[begin : i+1]) = max(A[:i+1]), for all begin <= i < n. So, we don't even need the begin pointer, 
we just compare max(A[:i+1]) with min(A[i+1:]) on every iteration.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        left_max = [num for num in arr]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
            
        right_min = [num for num in arr]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])
            
        cnt = 0
        for i in range(n - 1):
            if left_max[i] <= right_min[i+1]:
                cnt += 1
        return cnt + 1








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
