Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens==0:
            return 0
        dp = [1]*lens   # longest length ending in nums[i]
        cnt = [1]*lens  # number of longest ending in nums[i]
        for i in range(lens-1):
            for j in range(i+1, lens):
                if nums[j] > nums[i]:
                    if dp[j] <= dp[i]:
                        dp[j] = 1 + dp[i]
                        cnt[j] = cnt[i]
                    else:
                        if dp[i]+1 == dp[j]:   # 说明dp[j]是dp[i]的下一个递增的元素
                            cnt[j] += cnt[i]
        maxLens = max(dp)
        res = 0
        for i, num in enumerate(dp):
            if num == maxLens:
                res += cnt[i]
        return res
