"""
1218. Longest Arithmetic Subsequence of Given Difference

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr 
which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
 
Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4
"""


"""
O(N^2) - TLE
dp[i] = the LAS ended with arr[i].
dp[j] = dp[i] + 1 for i < j and arr[j] - arr[i] == diff.
"""
class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = [1 for _ in range(len(arr))]
        for j in range(1, len(arr)):
            for i in range(j):     # need to explore all the nums[i] before nums[j]
                if arr[j] - arr[i] == diff:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
        
        
"""
solution 1 needs to explore all the nums[i] before nums[j]. 
How about pre-find which i satisfies nums[j] - nums[i] == diff?
pre-calculation: O(N)
"""
class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        # step 1: pre-find the mapping for num --> idx corresponds to num
        mapping = defaultdict(list)     # num --> idx corresponds to num
        for i, num in enumerate(arr):
            mapping[num].append(i)
            
        # dp[i] = the LAS ended with ith 
        dp = [1 for _ in range(len(arr))]
        for j in range(1, len(arr)):
            for i in mapping[arr[j] - diff]: 
                if i < j:    # only explore the idx that satisfy nums[j] - nums[i] == diff
                    dp[j] = max(dp[j], 1 + dp[i])
        return max(dp)
         
        
"""
O(N)
use hashmap, like two sum problem.
"""
class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = defaultdict(lambda: 1)     # arr[i] --> LAC
        dp[arr[0]] = 1
        for j in range(1, len(arr)):
            if arr[j] - diff in dp:
                dp[arr[j]] = dp[arr[j] - diff] + 1
            else:
                dp[arr[j]] = 1
        return max(dp.values())
                
"""
Follow up: what if diff is not fixed, and we can choose whatever diff?
Then it is 1027.Longest-Arithmetic-Sequence. 
In 1027, diff is not fixed, so we need to put diff as key in the dp hashmap.
dp = [collections.defaultdict(lambda: 1) for _ in range(lens)].
"""
