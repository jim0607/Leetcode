Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lens = len(nums)
        dp = [1] * lens     # 以i为结尾的最大的长度
        cnt = [1] * lens    # 以i为结尾的最大的长度的个数
        
        for j in range(1, lens):
            for i in range(j):
                if nums[j] > nums[i]:   # 如果包括等于的话，那么[2,2,2]的输出就是错的
                    if dp[j] <= dp[i]:  # meaning this is the first time renewing dp[j], or the first time dp[j]遇到了一个非常大的dp[i]
                        dp[j] = dp[i] + 1
                        cnt[j] = cnt[i]
                        
                    elif dp[j] == dp[i] + 1:    # meaning dp[j]是dp[i]的下一个递增元素
                        cnt[j] += cnt[i]
                        
        print(dp)
        print(cnt)
        maxLen = max(dp)
        res = 0
        for i, length in enumerate(dp):
            if length == maxLen:
                res += cnt[i]
        
        return res
    
    
"""    
Solution 2: segment tree - O(nlogn)   
Suppose we knew for each length L-1, the number of sequences with length L-1 ending in x. 
Then when considering the next element of nums, updating our knowledge hinges on knowing the number of sequences with length L-1 ending in x < y. 
This type of query over an interval is a natural fit for using some sort of tree.
"""
