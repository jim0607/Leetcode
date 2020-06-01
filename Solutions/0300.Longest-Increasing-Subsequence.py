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
 

# 不用python自带的包
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = the length of LIS ended with ith num
        # if nums[j] > nums[i] for j > i, dp[j] = dp[i] + 1
        
        # 10 20 30 5 6 7 8
        # 1                             [10], res = 1
        # 1  2                          [10 20]
        # 1  2  3
        # 1  2  3  3
        # 1  2  3  3 3
        # 1  2  3  3 3 3
        # 1  2  3  3 3 3 4
        
        # dp[i] = the maintianed array with i as the longest length as far
        # dp should be an orderd array
        # if nums[i] > the last item in dp, then append nums[i] to dp
        # if < the first item in dp, then replacethe first item with nums[i]
        # is in between, then insert the item into the sorted arr
        
        lens = len(nums)
        if lens <= 1:
            return lens
        
        dp = [nums[0]]
        for num in nums:
            if num <= dp[0]:        # 由于第102行的写法，所以这里的<=不能改为<
                dp[0] = num
            elif num > dp[-1]:
                dp.append(num)
            else:
                self.replace(dp, num)
                
        return len(dp)
    
    def replace(self, arr, num):
        """
        replace an item in arr
        the arr is sorted acsendingly, and the arr is not none
        return void
        """
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if num > arr[mid]:      
                start = mid
            else:           # 由于第102行的写法，所以这里必须往左边逼近
                end = mid
                
        arr[end] = num      # 这种写法容易出错，请看下面的写法
        
        
        
     def replace(self, arr, num):
        """
        replace an item in arr
        the arr is sorted acsendingly, and the arr is not none
        return void
        """
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if num > arr[mid]:      
                start = mid
            else:           
                end = mid
                
        # 这里加一句dp[start] == num的判断，由于我们是要将最接近num的数用num取代，所以左边相等的话那就取代左边，其余情况取代右边。
        # 这里的这一句就把上面的79行和97,99行解放出来了，怎么写都不会出错
        if arr[start] == num:
            arr[start ] = num
        arr[end] = num      
