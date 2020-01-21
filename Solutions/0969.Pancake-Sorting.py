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
Find max
flip max to top
flip max to bottom
reduce size
repeat"""
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        lens = len(A)        
        res = []
        for i in range(lens - 1, 0, -1):            # O(N)
            # find max
            max_index = self.findMax(A[:i + 1])     # O(N)
            # flip max to top
            A = self.flip(A[:max_index + 1]) + A[max_index + 1:]            # O(N)
            # flip max to bottom
            A = self.flip(A[:i + 1]) + A[i + 1:]                  # O(N)
            print(A)
            res.append(max_index + 1)
            res.append(i + 1)
            
        return res
           
    # return the index of the max_num position
    def findMax(self, arr):
        max_num = -float("inf")
        max_index = 0
        for j in range(len(arr)):
            if arr[j] >= max_num:
                max_num = arr[j]
                max_index = j
        return max_index
        
    def flip(self, arr):
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
        return arr
        
