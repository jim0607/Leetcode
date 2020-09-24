259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?


"""这里输出的是index，所以不存在去重的问题，相比leetcode 15, 还是比较简单的
参考lintcode 609"""
"""模板写法，要牢记理解
O(N^2), O(1)"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()     # 老是忘了sort
        
        lens = len(nums)
        cnt = 0
        for i in range(lens - 2):
            # 属于本题的独特优化
            if nums[i] * 3 >= target:
                break
                
            left, right = i + 1, lens - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]  
                if threeSum >= target:
                    right -= 1
                else:
                    cnt += right - left    # 注意这里是 cnt += j - i 表示nums[i] 加上 i 到 j之间的任何数，一定也是小于等于target的
                    left += 1
        
        return cnt





class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        cnt = 0
        if not nums:
            return cnt
        
        nums.sort()     #双指针法求2sum的问题针对的都是排好序的数组
        
        for i in range(len(nums) - 2):
            # 重大优化
            if nums[i] * 3 >= target:
                break
                
            target_2 = target - nums[i]
            left, right = i + 1, len(nums) - 1
            cnt += self.twoSum(nums, target_2, left, right, 0)
            
        return cnt
    
    def twoSum(self, nums, target_2, left, right, cnt):
        while left < right:
            if nums[left] + nums[right] >= target_2:
                right -= 1
            else:
                cnt += right - left     # 注意这里是 cnt += j - i 表示nums[i] 加上 i 到 j之间的任何数，一定也是小于等于target的
                left += 1
                
        return cnt
