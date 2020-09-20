"""
644. Maximum Average Subarray II

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""


"""
The Most important concept here is, given any array and an average window of "k", it is possible to find whether there exists a subarray whose average value is bigger than "x", and find it in O(n) time.
How to check whether an average bigger than "mid" exists in O(n) time?

1. Minus all elements in the array by "mid".
2. After that, if we see any subarray that has sum>=0 means the average of this subarray is bigger than "mid".
3. To find a subarray bigger than "0", We can use prefix sum to find subarray of any target value. 
   Now we only need to find two index i and j to satisfy pre_sum[j]-pre_sum[i] >= 0.
   The algorithm is similar with 121. Best Time to Buy and Sell Stock, where we want to find the maximum diff of two numbers in an arr.
   We only need to remember the smallest pre_sum before current. The current prefix sum minus the smallest prefix sum is the biggest subarray so far.
With this very important algorithm, we can use binary search between the smallest and biggest average "value" of the array to find final result.
初始化 left 为原数组的最小值，right 为原数组的最大值 - O(Nlog(max-min))
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = min(nums), max(nums)       # 二分答案: start, end不是idx,而是avg数值
        while start + 10**(-5) < end:       
            mid = start + (end - start) / 2     # 注意这题二分答案可能是小数，所以不要用整除号
            if self._is_possible(nums, mid, k): # 判断是否有比mid更大的avg
                start = mid
            else:
                end = mid
        return end if self._is_possible(nums, start, k) else start
    
    def _is_possible(self, nums, target_avg, k):
        """
        Return if there is an k-window avg that is larger than the target_avg
        """
        pre_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            pre_sum[i+1] = pre_sum[i] + nums[i] - target_avg    # 这里减去target_avg就只需要比较max_avg是不是大于零就可以了
            
        # next is similar with 121. Best Time to Buy and Sell Stock, to find the max_diff in pre_sum arr
        curr_min = nums[0]      # keep a curr_min and use it for compare
        for i in range(len(pre_sum) - k):
            curr_min = min(curr_min, pre_sum[i])
            max_diff = pre_sum[i + k] - curr_min       # pre_sum[i + k]与min_sum之间至少有k个数, 这一点与121有点区别
            if max_diff >= 0:
                return True
        return False
