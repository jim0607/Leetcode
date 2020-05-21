Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"


cclass Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums, 0, len(nums)-1)
        return "".join(map(str, nums)) if nums[0] != 0 else "0"
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = nums[(start+end)//2]
        
        while left <= right:
            while left <= right and str(nums[left]) + str(pivot) > str(pivot) + str(nums[left]):
                left += 1
            while left <= right and str(nums[right]) + str(pivot) < str(pivot) + str(nums[right]):
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)           
