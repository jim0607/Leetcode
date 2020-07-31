930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


"""
(number of subarrays having sum S) = (number of subarrays having sum at most S) - (number of subarrays having sum at most S-1)
第一种写法是让后面的指针逐渐远离前面的指针 - 非常适合at least problems
"""
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if S == 0:
            return self._at_most(A, S) 
        
        return self._at_most(A, S) - self._at_most(A, S - 1)
    
    def _at_most(self, A, S):
        res = 0
        j = 0
        sums = 0
        for i in range(len(A)):
            while j < len(A) and sums <= S:
                sums += A[j]
                j += 1
            
            if sums <= S:
                res += j - i
            else:
                res += j - i - 1
                
            sums -= A[i]
            
        return res

    
"""
第二种写法是让前面的指针去追后面的指针 - 非常适合at most problems
"""
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if S == 0:
            return self._at_most(A, S) 
        
        return self._at_most(A, S) - self._at_most(A, S - 1)
    
    def _at_most(self, A, S):
        res = 0
        i = 0
        sums = 0
        for j in range(len(A)):
            sums += A[j]        # 先更新后面的指针
            
            while i <= j and sums > S:
                sums -= A[i]    # 再更新前面的指针
                i += 1
            
            res += j - i + 1    # 更新res
            
        return res
