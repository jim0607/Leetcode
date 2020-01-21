18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""for循环nums[i]，然后for循环nums[j]，在用双指针解决twoSum问题
O(N^3), O(1)"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        
        res = []
        lens = len(nums)
        for i in range(lens - 3):
            if i > 0 and nums[i] == nums[i - 1]:        # 去重
                continue
            
            if nums[i] * 4 > target:        # 优化
                break
                
            for j in range(i + 1, lens - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:        # 去重
                    continue
                    
                left, right = j + 1, lens - 1
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:        # 去重
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:      # 去重
                            right -= 1
                            
        return res

      
Solution 2: O(N^2 to N^4), O(N^2)
用一个hashmap 保存a + b
for a:
  for b:
    hashmap.add(a+b)
for c:
  for d:
    -(c + d) in hashmap?   # 注意这里-(c + d) in hashmap?不是O(1)，因为可能a+b有很多种组合都得到同一个a+b的值，因为还要输出a和b，所以要关注有多少种组合，最坏的情况有O(N^2)种组合，最好的情况有O(1)种。
