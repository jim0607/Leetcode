144. Interleaving Positive and Negative Numbers

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Example
Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
Challenge: Do it in-place and without extra memory.

"""STEP 1: 反向双指针（也可以同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]
STEP 2: 再来进行正负正负正负安插"""
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        if not A:
            return A
            
        # STEP 1
        lens = len(A)
        i, j = 0, lens - 1
        temp = A[0]
        while i < j:
            while i < j and A[j] > 0 :
                j -= 1
            A[i] = A[j]
            while i < j and A[i] < 0:
                i += 1
            A[j] = A[i]
            
        A[i] = temp
        
        print(A)
        
        # STEP 2
        if lens % 2 == 0:
            self.swap(A)

        else:     # somehow 这种情况提交不成功
            if A[lens // 2] > 0:
                self.swap(A[:lens - 1])
            else:
                self.swap(A[1:])
                
        return A
            
    def swap(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
