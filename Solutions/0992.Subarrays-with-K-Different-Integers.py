992. Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


"""
exactly(K) = atMost(K) - atMost(K-1)
"""
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self._at_most_k(A, K) - self._at_most_k(A, K - 1)
    
    def _at_most_k(self, A, K):
        """
        Exactly the same as 340. Longest Substring with At Most K Distinct Characters
        """
        freq = collections.defaultdict(int)
        j = 0
        res = 0
        for i in range(len(A)):
            while j < len(A) and len(freq) <= K:
                if A[j] not in freq and len(freq) == K:
                    break
                freq[A[j]] += 1
                j += 1
            
            if len(freq) <= K:
                res += j - i
                
            freq[A[i]] -= 1
            if freq[A[i]] == 0:
                del freq[A[i]]
                
        return res
