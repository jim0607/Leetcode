Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"


class Solution:    
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        
        lens = len(nums)
        numsStr = []
        for num in nums:
            numsStr.append(str(num))
        
        self.quickSort(numsStr, 0, len(numsStr) - 1)
        
        return "".join(numsStr) if "".join(numsStr)[0] != "0" else "0"
    
    def compare(self, s1, s2):
        if s1 + s2 <= s2 + s1:
            return True     # return True if s1 < s2
        else:
            return False
    
    def partition(self, arr, i, j):
        pivotVal = arr[i]
        while i < j:
            while i < j and self.compare(arr[j], pivotVal):
                j -= 1
            arr[i] = arr[j]
            while i < j and self.compare(pivotVal, arr[i]):
                i += 1
            arr[j] = arr[i]
            
        arr[i] = pivotVal
        
        return i
    
    def quickSort(self, arr, start, end):
        if start >= end:
            return 
        
        pivotPos = self.partition(arr, start, end)
        self.quickSort(arr, start, pivotPos)
        self.quickSort(arr, pivotPos + 1, end)
