Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        self.quick_sort(arr, 0, len(nums) - 1)
        return "".join(arr) if arr[0] != "0" else "0"
    
    def quick_sort(self, arr, start, end):
        if start >= end:
            return
        
        pivot = arr[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and arr[left] + pivot > pivot + arr[left]:
                left += 1
            while left <= right and arr[right] + pivot < pivot + arr[right]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        self.quick_sort(arr, start, right)
        self.quick_sort(arr, left, end)
