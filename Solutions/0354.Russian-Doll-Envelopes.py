You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


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
