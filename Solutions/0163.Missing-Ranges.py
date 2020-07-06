163. Missing Ranges

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        
        lens = len(nums)
        res = []
        for i in range(1, lens):
            if nums[i] == nums[i-1] + 2:
                res.append(str(nums[i-1] + 1))
            if nums[i] > nums[i-1] + 2:
                res.append(str(nums[i-1] + 1) + "->" + str(nums[i] - 1))
                
        return res
