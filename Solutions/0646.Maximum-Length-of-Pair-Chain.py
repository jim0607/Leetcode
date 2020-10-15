"""
646. Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. 
Chain of pairs can be formed in this fashion.
Given a set of pairs, find the length longest chain which can be formed. 
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
"""



"""
step 1: sort the interval by end_time or start_time;
step 2: dp. dp[i] = the max lens ended with ith interval.
dp[j] = max(dp[i] + 1 for i < j and intervals[i][1] < intervals[j][0])
O(N^2)
"""
class Solution:
    def findLongestChain(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        n = len(intervals)
        dp = [1 for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if intervals[j][0] > intervals[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
        
        
"""
solution 2: 找到所有overlapped intervals. 用一个last_end指针记录上一个end;
O(NlogN)
"""
class Solution:
    def findLongestChain(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], x[0]))
        last_end = -sys.maxsize
        cnt = 0     # cnt of overlaps
        for start, end in intervals:
            if start > last_end:
                last_end = end
            else:
                cnt += 1
                
        return len(intervals) - cnt
