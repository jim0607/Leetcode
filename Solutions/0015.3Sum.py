
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
Solution 1: hash map: O(N^2), O(N), 循环a, b，然后每次判断if -a-b in dict_nums
O(N^2), O(N)
Solution 2: sort, 然后循环a, 在循环里用反向双指针解决b+c = -a的two sum问题。
注意去重的方法。
O(N^2), O(1)

Solution 2 is slightly better.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()     # 双指针法针对的是排序好的数组
        
        lens = len(nums)
        res = []
        for i in range(lens - 2):
            # res里的数组都是以nums[i]开头，第一步可以先将nums[i]去重  
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left, right = i + 1, lens - 1
            self.twoSum(nums, target, left, right, res)
            
        return res
    
    # put all the combinations of [-target, nums[left], nums[right]] into res to fit nums[left] + nums[right] = target, in range of i+1 to lens-1
    def twoSum(self, nums, target, left, right, res):
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                res.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                # 经典的去重方法，参考leetcode 532：前面的3用到了，后面的3就跳过就可以了。
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

                    
                    
"""
以下是3Sum问题的模板！！！要熟记背诵！！！
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        # 接下来是3Sum问题的模板
        # STEP 1: sort the arr
        nums.sort()
        
        res = []
        lens = len(nums)       
        # STEP 2: for循环nums[i]，然后双指针解twoSum问题
        for i in range(lens - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, lens - 1
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
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res
