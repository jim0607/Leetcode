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
solution 1: O(1) just for this problem.
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
    def isIdealPermutation(self, A: List[int]) -> bool:
        local_cnt = 0
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                local_cnt += 1
        
        self.global_cnt = 0
        self._merge_sort(A)
        
        return local_cnt == self.global_cnt
    
    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
    
        mid = len(arr) // 2
        left_arr = self._merge_sort(arr[:mid])
        right_arr = self._merge_sort(arr[mid:])
        
        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = right_arr[j]
                k += 1
                j += 1
                self.global_cnt += len(left_arr) - i    # 因为left已经sort好了，所以如果left[i]>right[j], 那么i后面的都会>right[j]
                
        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
            
        return arr                
