"""
183. Wood Cut

Given an int array wood representing the length of n pieces of wood and an int k. It is required to cut these pieces of wood such that more or equal to k pieces of the same length len are cut. What is the longest len you can get?

Example 1:

Input: wood = [5, 9, 7], k = 3
Output: 5
Explanation: 
5 -> 5
9 -> 5 + 4
7 -> 5 + 2
Example 2:

Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation: 
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3
Example 3:

Input: wood = [1, 2, 3], k = 7
Output: 0
Explanation: We cannot make it.
Example 4:

Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long, however we can't cut it into 7 pieces if any piece is 115 long.
"""




"""
If we can cut into pieces with lens, then we can also cut into prices with len - 1,
So this is a OOOXXX problem, to find the last O.
"""
class Solution:
    def woodCut(self, L, k):
        lens = len(L)
        if lens == 0 or sum(L) < k:
            return 0
        
        start, end = 0, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isValid(L, k, mid):
                start = mid     # 注意这里是取后一半，因为我们希望长度尽可能长
            else:
                end = mid
                
        if self.isValid(L, k, end):
            return end
        if self.isValid(L, k, start):
            return start
            
    def isValid(self, L, k, mid):
        cnt = 0
        for length in L:
            cnt += length // mid
            
        return cnt >= k
