Description

Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Example1
Input: 
[-3,1,1,-3,5] 
Output: 
[0,2]
Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
Challenge: O(nlogn) time


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        
        # key: prefixSum val: index
        prefixSums = [(0, -1)]
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum += num
            prefixSums.append((prefixSum, i))
            
        prefixSums.sort()   # 默认按照第一个value也就是prefixSum来进行sort
        
        closestVal = float("inf")
        res = []
        for i in range(1, len(prefixSums)):
            if prefixSums[i][0] - prefixSums[i - 1][0] < closestVal:
                closestVal = prefixSums[i][0] - prefixSums[i - 1][0]
                # prefixSum[j+1]-prefixSum[i] = sum(i~j 包括i,j)，我们要输出的是i和j,所以left = 较小的index，
                left = min(prefixSums[i][1], prefixSums[i - 1][1])  + 1
                right = max(prefixSums[i][1], prefixSums[i - 1][1])
                res = [left, right]
                
        return res
