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



"""
dp[j] = the max number of envs we can Russian doll ended with j.
dp[j] = max(1 + dp[i] for i < j if env[i] can fit in env[j])
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        
        n = len(envelopes)
        dp = [1 for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if (envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]):
                    dp[j] = max(dp[j], 1 + dp[i])
                    
        return max(dp)

    

    
"""
O(nlogn)：Consider an input [[1, 3], [1, 4], [1, 5], [2, 3]]. If we simply sort and extract the second dimension we get [3, 4, 5, 3], 
which implies that we can fit three envelopes (3, 4, 5). 
The problem is that we can only fit one envelope, since envelopes that are equal in the first dimension can't be put into each other.
In order fix this, we don't just sort increasing in the first dimension - we also sort decreasing on the second dimension, 
so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.
Now when we sort and extract the second element from the input we get [5, 4, 3, 3], which correctly reflects an LIS of one.
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort width ascendingly以保证后面的width肯定能fit进前面的width, 
        # while sort length descendingly以保证相同的width不同的length不能相互fit进去
        # 这样一来，只要后面来的envelope[j]的length比前面的envelope[i]的length大，那j一定能套住i
        # 这样我们只需要对length做300. Longest Increasing Subsequence就可以了
        envelopes.sort(key=lambda x: (x[0], -x[1]))     # !!!!这一步的sort很tricky
        nums = [lens for width, lens in envelopes]      # sort完之后只需要对length做300. LIS
        
        # below is exactly the same as 300. LIS
        dp = []
        for num in nums:
            if len(dp) == 0 or num > dp[-1]:
                dp.append(num)
            else:
                idx = bisect.bisect_left(dp, num)
                dp[idx] = num
                    
        return len(dp)
