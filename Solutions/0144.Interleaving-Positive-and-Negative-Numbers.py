"""
144. Interleaving Positive and Negative Numbers

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Example
Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
Challenge: Do it in-place and without extra memory.
"""


"""
STEP 1: 反向双指针（也可以同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]
STEP 2: 再来进行正负正负正负安插
"""
class Solution:
    def rerange(self, A):
        i, j = 0, len(A) - 1
        temp = A[i]
        while i < j:
            while i < j and A[j] > 0:
                j -= 1
            A[i] = A[j]
            
            while i < j and A[i] < 0:
                i += 1
            A[j] = A[i]
            
        A[i] = temp
        
        if len(A) % 2 == 0:
            self.swapEven(A)
        else:
            if A[len(A) // 2] < 0:
                self.swapOdd1(A)
            else:
                self.swapOdd2(A)
            
    def swapEven(self, A):      # 不需要return, 因为题目要求edit in place
        """swap, no return"""
        i, j = 0, len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
            
    def swapOdd1(self, A):
        """swap, no return"""
        i, j = 1, len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
            
    def swapOdd2(self, A):
        """swap, no return"""
        i, j = 0, len(A) - 2
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
