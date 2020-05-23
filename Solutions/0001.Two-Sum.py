1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Solution 1: brutal force O(N^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        
        lens = len(nums)
        for i in range(lens):
            for j in range(i + 1, lens):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return None

九章算法：对于求 2 个变量如何组合的问题可以循环其中一个变量，然后研究另外一个变量如何变化
普世的方法是：for循环一个变量a，然后看另外一个变量target-a是不是在一个hashmap中。
Solution 2: hash map  O(N), O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in numsDict:
                return (numsDict[target - num], i)
            
            numsDict[num] = i
