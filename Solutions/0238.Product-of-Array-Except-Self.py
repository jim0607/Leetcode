238. Product of Array Except Self

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

O(N), O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        fwd = [1] * lens
        bwd = [1] * lens
        
        for i in range(1, lens):
            fwd[i] = fwd[i - 1] * nums[i - 1]   # fwd[i]=product before ith num
            
        for i in range(lens - 2, -1, -1):
            bwd[i] = bwd[i + 1] * nums[i + 1]   # bwd[i]=product after ith num
            
        res = [1] * lens
        for i in range(lens):
            res[i] = fwd[i] * bwd[i]
            
        return res
        

O(N), O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        
        res = [1] * lens
        for i in range(1, lens):
            res[i] = res[i - 1] * nums[i - 1]   # res[i]=product before ith num
            
        right = 1
        for i in range(lens - 1, -1, -1):
            res[i] *= right                     # right = the product on the right so far
            right *= nums[i]
            
        return res
        
