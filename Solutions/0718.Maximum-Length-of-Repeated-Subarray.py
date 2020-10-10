"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
"""


"""
since subarray has to be continuous, we define dp as
dp[i][j] = the max lens of repeated subarray ended with A[i] and B[j]
dp[i][j] = if A[i-1]==B[j-1]: dp[i-1][j-1] + 1; else: 0 cuz has ot be continuous
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len


"""
solution 2: binary search - (m+n)mlogm.
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m > n:
            return self.findLength(B, A)
        
        start, end = 0, m
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._is_valid(A, B, mid):
                start = mid
            else:
                end = mid
                
        return end if self._is_valid(A, B, end) else start
    
    def _is_valid(self, A, B, mid):
        """
        return if there is mid-size window in A that equals a mid-size window in B
        O(m + n)
        """
        window_set = set()
        dq_A = collections.deque()
        for i in range(len(A)):
            dq_A.append(A[i])
            if i >= mid:
                dq_A.popleft()
            if len(dq_A) == mid:
                window_set.add(tuple(dq_A))
            
        dq_B = collections.deque()
        for i in range(len(B)):
            dq_B.append(B[i])
            if i >= mid:
                dq_B.popleft()
            if len(dq_B) == mid and tuple(dq_B) in window_set:      # note that this takes O(mid)
                return True
            
        return False  
    
    


"""方法一：暴力法O(N^3)。实际这道题就是求 Longest Common Substring 的问题了。最暴力的方法就是遍历A中的每个位置，把每个位置都当作是起点进行和B从开头比较，
每次A和B都同时前进一个，假如相等，则计数器会累加1，不相等的话，计数器会重置为0，每次用计数器 cnt 的长度来更新结果 res。"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lensA, lensB = len(A), len(B)
        if lensA == 0 or lensB == 0:
            return 0

        res = 0
        for i in range(lensA):
            for j in range(lensB):
                cnt = 0
                m, n = i, j
                while m < lensA and n < lensB and A[m] == B[n]:
                    m += 1
                    n += 1
                    cnt += 1
                res = max(res, cnt)
        return res
        
        
"""方法二：Use dynamic programming. dp[i][j] will be the answer for inputs A[:i], B[:j]."""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lensA, lensB = len(A), len(B)
        if lensA == 0 or lensB == 0:
            return 0
        dp = [[0]*(lensB+1) for _ in range(lensA+1)]
        res = 0
        for i in range(lensA):
            for j in range(lensB):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1    # 貌似有逻辑漏洞，A[i] == B[j]出现的前后顺序可以不管吗？
                    res = max(res, dp[i+1][j+1])
        return res
