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
        if lens == 1:
            return A
        
        res = []
        for j in range(lens - 1, 0, -1):
            # find the max from 0-jth idx
            maxVal, maxIdx = A[0], 0
            for i in range(j + 1):
                if A[i] > maxVal:
                    maxVal = A[i]
                    maxIdx = i
                    
            # do two filps
            self.flip(A, 0, maxIdx)
            res.append(maxIdx + 1)
            self.flip(A, 0, i)
            res.append(i + 1)
            
        return res
            
    def flip(self, A, start, end):
        i, j = start, end
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1        
