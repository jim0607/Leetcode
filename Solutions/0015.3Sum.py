
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


                    
                    
"""
以下是3Sum问题的模板！！！要熟记背诵！！！
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()   # STEP 1: sort the arr
        
        res = []
        lens = len(nums) 
        
        # STEP 2: for循环nums[i]，然后双指针解twoSum问题
        for i in range(lens - 2):
            if i > 0 and nums[i] == nums[i - 1]:        # 注意点一：对i去重
                continue
            
            left, right = i + 1, lens - 1               # 注意点二：left 和 right 的初始值
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:    # 注意点三：对 left 和 right 去重
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res



"""
Solution 1: hash map: O(N^2), O(N), 循环a, b，然后每次判断if -a-b in dict_nums
O(N^2), O(N)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lens = len(nums)
        if lens <= 2:
            return []
        
        # sort is neccessary, otherwise [-1, 1, 0] and [-1, 0, 1] will appear in the res, 
        # and unfortunately, remove duplicates algorithm doesn't think these two answers are duplicates
        nums.sort()     
        
        res = []
        for i in range(lens - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # now let's do two sum problem, the target of the two sum problem is -nums[i]
            sumSet = set()
            for j in range(i + 1, lens):
                if -nums[i] - nums[j] in sumSet:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                sumSet.add(nums[j])
                
        # next, let's remove duplicates
        anchor, curr = 0, 0
        while curr < len(res):
            if res[curr] != res[anchor]:
                anchor += 1
                res[anchor] = res[curr]
            curr += 1
            
        return res[:anchor+1]   # anchor keeps all non-duplicates on it's left
