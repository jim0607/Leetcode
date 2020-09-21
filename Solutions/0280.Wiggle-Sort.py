280. Wiggle Sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]


"""
从左到右扫一遍，不满足条件的交换就好了。
需要证明的是，当我们 交换了 nums[i] 和 nums[i - 1] 以后：

... nums[i - 2], nums[i], nums[i - 1]
nums[i - 2] 不会和 nums[i] 形成逆序（不满足条件的大小关系）

那假如原来是 nums[i - 2] <= nums[i - 1]，那么 nums[i - 1] 和 nums[i] 交换的条件是，nums[i - 1] <= nums[i]。
那我们就推导出此时 nums[i] >= nums[i - 2]，因此交换之后，不会让 nums[i] 和 nums[i - 2] 的大小关系出现变化。

反过来如果 nums[i - 2] >= nums[i - 1] 的情况同理。
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prevShouldBeLessThanCur = True
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i] and prevShouldBeLessThanCur or (nums[i-1] <= nums[i] and not prevShouldBeLessThanCur):
                nums[i-1], nums[i] = nums[i], nums[i-1]
                
            prevShouldBeLessThanCur = not prevShouldBeLessThanCur
