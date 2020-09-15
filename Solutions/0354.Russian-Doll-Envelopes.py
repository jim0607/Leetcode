"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""



"""similiar with 300. LIS; here we not only compare nums[j]>nums[i], but instead both the width and height;
TLE, should learn how to do 300. LIS using DP+binary search, O(NlogN)"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        lens = len(envelopes)
        dp = [1] * lens
        
        envelopes.sort(key = lambda x: (x[0], x[1]))
        
        res = 1
        for j in range(1, lens):
            for i in range(j):
                if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    res = max(dp[j], res)
                    
        return res

    

    
"""
O(nlogn)：Consider an input [[1, 3], [1, 4], [1, 5], [2, 3]]. If we simply sort and extract the second dimension we get [3, 4, 5, 3], 
which implies that we can fit three envelopes (3, 4, 5). The problem is that we can only fit one envelope, since envelopes that are equal in the first dimension can't be put into each other.
In order fix this, we don't just sort increasing in the first dimension - we also sort decreasing on the second dimension, 
so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.
Now when we sort and extract the second element from the input we get [5, 4, 3, 3], which correctly reflects an LIS of one.
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        lens = len(envelopes)
        if lens <= 1: return lens
        
        # sort width ascendingly以保证后面的width肯定能fit进前面的width, 
        # while sort length descendingly以保证相同的width不同的length不能相互fit进去
        envelopes.sort(key = lambda x: (x[0], -x[1]))   # 这一步的sort很tricky
        
        # now below we are just doing LIS problem using the length, which is exactly the same as 300
        dp = [envelopes[0][1]]      # 用length来做300. LIS
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                idx = bisect.bisect_left(dp, envelopes[i][1])
                dp[idx] = envelopes[i][1]
                
        return len(dp)
