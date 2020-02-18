Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""经典dp LIS 问题 O(N^2)"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lens = len(nums)
        dp = [1] * lens # dp[i] means the longest increasing subsequence ending with nums[i]
        
        res = 1
        for j in range(1, lens):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
            res = max(res, dp[j])
            
        return res
    
    
"""NlogN的算法，还是网上的高人讲得好。https://www.youtube.com/watch?v=YoeWZ3ELMEk"""

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)    # dp[i]中的i是指最长上升子序列长度，好难讲dp[i]代表什么，看视频吧！
        maxLen = 0
        
        for num in nums:
            insertIndex = bisect.bisect_left(dp, num, 0, maxLen)    # 用binary search找到num应该放入的位置，以保证dp这个数组是递增的
            dp[insertIndex] = num       # 将该位置的值改为num
            
            if insertIndex == maxLen:     # 如果num比dp中的数都大，则说明num放入的位置是整个递增数组的最右端，所以maxLen需要加1
                maxLen += 1
                
        return maxLen
    
    
"""方法一：暴力法
时间复杂度：O(2^n)递归树的大小将为 2^n
算法：
最简单的方法是找到所有增加的子序列，然后返回最长增加的子序列的最大长度。为了做到这一点，我们使用递归函数 \text length of lislengthoflis 返回从当前元素（对应于 curposcurpos）开始可能的 lis 长度（包括当前元素）。在每个函数调用中，我们考虑两种情况：
当前元素大于包含在 lis 中的前一个元素。在这种情况下，我们可以在 lis 中包含当前元素。因此，我们通过将其包含在内，得出了 lis 的长度。此外，我们还通过不在 lis 中包含当前元素来找出 lis 的长度。因此，当前函数调用返回的值是两个长度中的最大值。
当前元素小于包含在 lis 中的前一个元素。在这种情况下，我们不能在 lis 中包含当前元素。因此，我们只通过不在 lis 中包含当前元素（由当前函数调用返回）来确定 lis 的长度。"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self._lengthOfLIS_Helper(nums, -float("inf"), 0)
    
    def _lengthOfLIS_Helper(self, nums: List[int], prevVal: int, curr: int) -> int:
        if curr == len(nums):
            return 0
        taken, noTaken = 0, 0
        if nums[curr] > prevVal:
            taken = 1 + self._lengthOfLIS_Helper(nums, nums[curr], curr+1)
        # 注意把noTaken放在else里面是错的，因为即使nums[curr]>prevVal也可以选择不take，不take当前那个数说不定更好，eg:[1,2,9,3,4,5],这里如果take 9，那最长的长度是3，不take 9的话最长的长度可以是5
        noTaken = self._lengthOfLIS_Helper(nums, prevVal, curr+1)

        return max(taken, noTaken)
        
        
"""方法二：带记忆的递归 O(N^2); O(N^2)
算法：在前面的方法中，许多递归调用必须使用相同的参数进行一次又一次的调用。通过将为特定调用获得的结果存储在二维记忆数组 memo 中，可以消除这种冗余。memo[i][j] 表示使用 nums[i] 作为上一个被认为包含/不包含在 lis 中的元素的 lis 可能的长度，其中 nums[j] 作为当前被认为包含/不包含在 lis 中的元素。这里，nums 表示给定的数组。"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lens = len(nums)
        memo = [[0]*(lens) for _ in range(lens)]
        return self._lengthOfLIS_Helper(nums, -1, 0, memo)

    def _lengthOfLIS_Helper(self, nums: List[int], prev: int, curr: int, memo: List[int]) -> int:
        if curr == len(nums):
            return 0
        taken, noTaken = 0, 0
        if memo[prev+1][curr] > 0:
            return memo[prev+1][curr]   # 这里判断只要memo[prev+1][curr]只要计算过，就直接调用不再计算了，从而降低了运算的复杂度。
        if prev < 0 or nums[curr] > nums[prev]:
            taken = 1 + self._lengthOfLIS_Helper(nums, curr, curr+1, memo)
        noTaken = self._lengthOfLIS_Helper(nums, prev, curr+1, memo)
        memo[prev+1][curr] = max(taken, noTaken)
        return memo[prev+1][curr]
        
        
"""方法三：动态规划  时间复杂度：O(n^2)。有两个 n 的循环。空间复杂度：O(n)，用了大小为 n 的矩阵 dp。
算法：dp[i]表示到第i个数据为止最大的长度
递推关系：if j>i and nums[j]>nums[i]: dp[j]=max[dp[j], dp[i]+1]
初始条件：dp[0] = 1"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        dp = [1]*lens
        for i in range(lens-1):
            for j in range(i+1, lens):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)
"""方法四：将dp的方法优化，使用二分查找。时间复杂度 O(NlogN) ： 遍历 nums 列表需 O(N)，在每个 nums[i]n 二分法需 O(logN)。
空间复杂度 O(N) ： dp 列表占用线性大小额外空间。"""
