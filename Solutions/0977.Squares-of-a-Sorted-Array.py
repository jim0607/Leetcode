977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i, j, k = 0, len(A) - 1, len(A) - 1
        while i <= j:
            if A[i]**2 > A[j]**2:
                res[k] = A[i]**2
                i += 1
            else:
                res[k] = A[j]**2
                j -= 1
            k -= 1
            
        return res
