"""
1095. Find in Mountain Array

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""



"""
step 1: Binary find peak in the mountain - 852. Peak Index in a Mountain Array.
step 2: Binary find the target in strict increasing/left part
step 3: Binary find the target in strict decreasing/right part
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        lens = arr.length()
        peak_idx = self._find_peak(arr)
        peak_num = arr.get(peak_idx)
        if target > peak_num:
            return -1
        if target == peak_num:
            return peak_idx
        
        left_idx = self._binary_search_increasing(target, arr, 0, peak_idx - 1)
        if left_idx != -1:
            return left_idx
        right_idx = self._binary_search_decreasing(target, arr, peak_idx + 1, lens - 1)
        if right_idx != -1:
            return right_idx
        return -1
        
    def _find_peak(self, arr):
        lens = arr.length()
        start, end = 0, lens - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr.get(mid) > arr.get(mid + 1):
                end = mid
            else:
                start = mid
        return start if arr.get(start) > arr.get(end) else end
    
    def _binary_search_increasing(self, target, arr, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_val = arr.get(mid)
            if mid_val > target:
                end = mid
            elif mid_val < target:
                start = mid
            else:
                return mid
        if arr.get(start) == target:
            return start
        if arr.get(end) == target:
            return end
        return -1
    
    def _binary_search_decreasing(self, target, arr, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_val = arr.get(mid)
            if mid_val > target:
                start = mid
            elif mid_val < target:
                end = mid
            else:
                return mid
        if arr.get(start) == target:
            return start
        if arr.get(end) == target:
            return end
        return -1
