"""
969. Pancake Sorting

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
"""


"""
Find max
flip max to top
flip max to bottom
reduce size
repeat
"""


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if not arr or len(arr) == 1:
            return arr
        
        lens = len(arr)
        res = []
        for i in range(lens-1, 0, -1):
            max_idx = self._find_max(arr, i + 1)
            self._flip(arr, 0, max_idx)
            self._flip(arr, 0, i)
            res.append(max_idx + 1)
            res.append(i + 1)
        return res            
            
    def _find_max(self, arr, end):
        """
        Return the idx of max num in arr[:end]
        """
        max_idx = 0
        max_num = arr[0]
        for i in range(end):
            if arr[i] > max_num:
                max_num = arr[i]
                max_idx = i
        return max_idx
    
    def _flip(self, arr, start, end):
        """
        Flip the arr from start to end - in place
        """
        i, j = start, end
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
