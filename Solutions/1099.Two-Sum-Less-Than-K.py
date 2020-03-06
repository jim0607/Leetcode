1099. Two Sum Less Than K

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.

Solution 1: sort the array and then use two pointers to do the two sum problem
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        
        A.sort()        # 容易漏掉
        
        lens = len(A)
        i, j = 0, lens - 1
        max_num = -1
        while i < j:
            twoSum = A[i] + A[j]
            
            if twoSum >= K:
                j -= 1
            else:
                max_num = max(max_num, twoSum)
                i += 1
        
        return max_num
