31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """"
        Do not return anything, modify nums in-place instead.
        """
        # step 1: sweeping from right to left, find the first decreasing element
        i = len(nums) - 2
        while i > 0 and nums[i + 1] <= nums[i]:
            i -= 1
            
        # if the number is 54321, then we reverse it
        if i == 0 and nums[i + 1] < nums[i]:
            self.reverse(nums, 0)
            
        # Step 2: if not, we sweep from right to left, find the first element larger just than nums[i], then swap nums[i] and nums[j], then swap all the items starting from i+1
        else:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            
            self.reverse(nums, i + 1)
            
    def reverse(self, nums, startIdx):
        i, j = startIdx, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

            
            
"""
1 3 2 5 4 2  -  1 3 4 2 2 5
the first decreasing is 2
the right list after 2 is [5, 4, 2], the num just larger than 2 is 4;
swap 2 and 4 [1 3 4 5 2 2]. sort the right list - 1 3 4   2 2 5 
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        first_dec_num, first_dec_idx = float("inf"), len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                first_dec_num = nums[i-1]
                first_dec_idx = i - 1
                break
                
        if first_dec_num == float("inf") and i-1 == 0:
            self.reverse(nums, 0)
            
        else:
            just_larger_num, just_larger_idx = i, nums[i]
            for j in range(i, len(nums)):
                if nums[j] > first_dec_num:
                    just_larger_num = nums[j]
                    just_larger_idx = j

            nums[first_dec_idx], nums[just_larger_idx] = nums[just_larger_idx], nums[first_dec_idx]
            self.reverse(nums, first_dec_idx + 1)
            
            
    def reverse(self, nums, start_idx):
        p, q = start_idx, len(nums) - 1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
