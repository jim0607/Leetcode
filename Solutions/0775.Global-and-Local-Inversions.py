"""
775. Global and Local Inversions

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
"""



"""
solution 1: O(n) just for this problem.
If the number of global inversions is equal to the number of local inversions,
it means that all global inversions in permutations are local inversions.
It also means that we can not find A[i] > A[j] with j > i + 1, cuz that will be globa not local.
In other words, max(A[i]) < A[i+2]
"""
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        curr_max = A[0]
        for i in range(len(A) - 2):
            curr_max = max(curr_max, A[i])
            if curr_max > A[i+2]:
                return False
        return True              


"""
Now solution 1 is pretty.  What if we are asked to find the number of global inversions.
Then it becomes the probem in Coursera Algorithm: Counting inversion.  We have to use mergesort.
"""
"""
When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j.
So in the merging part of merge_sort, we can update cnt if left_arr[i] > right_arr[j].
"""
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        self.local_inversions = 0 
        self.global_inversions = 0
        self._find_local(nums)
        self._find_global(nums)
        return self.local_inversions == self.global_inversions
    
    def _find_local(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                self.local_inversions += 1
    
    def _find_global(self, nums):   # we are actually doing merge sort here - using devide and conquer
        if len(nums) <= 1:
            return nums
        
        # divide
        mid = len(nums) // 2
        left = self._find_global(nums[:mid])
        right = self._find_global(nums[mid:])

        # Everything is exactly the same as merge sort, except that before merge/conquer, we update cnt first
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                self.global_inversions += len(left) - i # 因为left已经sort好了，所以如果left[i]>right[j], 那么i后面的都会>right[j]
                j += 1
            else:
                i += 1
                
        # merge/conquer
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums
