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
We binary search on the answer二分答案. Let P[i] = A[0] + A[1] + ... + A[i-1], the i-th prefix sum under A.
Let's focus our attention on possible(x), a function that is true if it is possible to have an average of at least x. 
Consider the elements B = [a-x for a in A] with corresponding prefix sum Q[i] = P[i] - i*x under B.
We want to know if there is some >= K length subarray in B with average at least zero. 
ee, to check if Q[j+1] - Q[i] > 0 for any j, and any i <= j - K + 1, we should check whether Q[j+1] >= min_{i <= j-K+1} Q[i]. 
Keeping a running minimum m of this array Q, we can check this in linear time.
初始化 left 为原数组的最小值，right 为原数组的最大值 - O(Nlog(max-min))
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = min(nums), max(nums)       # start, end不是idx,而是avg数值
        while start + 10**(-5) < end:
            mid = start + (end - start) / 2     # 注意这题二分答案可能是小数，所以不要用整除号
            if self._is_possible(mid, nums, k):       # 判断是否有比mid更大的avg
                start = mid
            else:
                end = mid
        return end if self._is_possible(end, nums, k) else start
    
    def _is_possible(self, avg, nums, k):
        """
        if 有比avg number更大的avg, return True - O(N)
        algorithm is similar with 121. Best Time to Buy and Sell Stock
        """
        diff_nums = [num - avg for num in nums]
        prefix_diff_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefix_diff_sum[i + 1] = prefix_diff_sum[i] + diff_nums[i]
            
        # next is to check if in diff_nums there is an avg with at least K length that is larger than 0
        # or to check if there is in diff_nums a sum with at least K length that is larger than 0
        min_sum = 0     # keep a min_sum and use it for compare, similar with 121. Best Time to Buy and Sell Stock
        for i in range(len(prefix_diff_sum) - k):
            min_sum = min(min_sum, prefix_diff_sum[i])
            if prefix_diff_sum[i + k] - min_sum >= 0:   # 保证prefix_diff_sum[i + k]与min_sum之间至少有k个数
                return True
        return False
