1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.



"""
sliding window solution: finding the maximum lens with at most K 0s.
"""
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        max_lens = 0
        j = 0
        cnt = 0
        for i in range(len(A)):
            while j < len(A) and cnt <= K:
                if A[j] == 0:       # 更新带有j的信息
                    cnt += 1
                j += 1
            
            # 更新res
            if cnt <= K:    # if cnt <= K, that means j == len(A)
                max_lens = max(max_lens, j - i)
            else:
                max_lens = max(max_lens, j - i - 1)
                
            if A[i] == 0:           # 更新带有j的信息
                cnt -= 1
                
        return max_lens
