324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.


"""
这题比Wiggle Sort I难在相邻的数不能相等，所以相邻交换法行不通，
我们可以sort the nums, then 把有序数组从中间分成两部分，然后从前半段的末尾取一个，
在从后半的末尾取一个，这样保证了第一个数小于第二个数，然后从前半段取倒数第二个，
从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数，以此类推。
O(nlogn), O(n)
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        temp = nums.copy()      # must be a copy
        temp.sort()
        lens = len(temp)
        i, j = (lens - 1) // 2, lens - 1
        k = 0
        while i >= 0 and j > (lens - 1) // 2:
            nums[k] = temp[i]
            k += 1
            i -= 1
            nums[k] = temp[j]
            k += 1
            j -= 1
        while i >= 0:
            nums[k] = temp[i]
            k += 1
            i -= 1
            
            
Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
solution: virtual indexing https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
