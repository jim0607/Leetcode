
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1


"""画个图就知道，问题可以转换成寻找第一个小于nums[0]的数，属于OOOXXX问题，OOO表示前面的数都大于nums[0]，XXX表示之后的数都小于nums[0]，找出第一个这样的X"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        if nums[-1] >= nums[0]:  # 如果已经排好序了，那minimum就是第一个数
            return nums[0]
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[0]:   # 寻找第一个X的问题，需要不断丢掉右半部分才能尽量向左逼近，所以先判断丢掉有半部分的语句，注意是<=
                end = mid
            else:
                start = mid
        if nums[end] < nums[0]:
            return nums[end]
        if nums[start] < nums[0]:  # # 寻找第一个X的问题，需要返回尽量小的值，所以需要把小的值start放在后面判断，这样如果nums[end]和nums[start]都小于nums[0]的话，就应该取较小的start。
            return nums[start]

        
"""为了更好的去解follow up questions: 154. Find Minimum in Rotated Sorted Array II（存在重复的数）,我们采用下面的方法，
instead of comapring nums[mid] and nums[0], we compare nums[mid] and nums[end]. 
It should be noted that end is always on the right of the minimum point, and start is alwyas on the left, that is why the algorithm works."""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        if nums[-1] >= nums[0]:  # 如果已经排好序了，那minimum就是第一个数
            return nums[0]
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
        return min(nums[start], nums[end])
