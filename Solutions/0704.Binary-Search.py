"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9

Output: 4
Explanation: 9 exists in nums and its index is 4
"""



# 二分法模板：九章算法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        start, end = 0, lens-1
        while start + 1 < end:
            mid = start + (end-start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

// C# version
public class Solution {
    public int Search(int[] nums, int target) {
        int start = 0;
        int end = nums.Length - 1;
        while (start + 1 < end) { 
            int mid = start + (end - start) / 2;
            if (nums[mid] >= target) { 
                end = mid;
            } else {
                start = mid;
            }
        }
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
}
