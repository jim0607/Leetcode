Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647. 

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


"""二分法是基于起点和终点的，但是由于本题的array size unknown，也就是说终点是不知道的，这时候就需要去终点，这个终点需要是>=target就可以。怎么找呢，当然不能设置成无穷大，不然二分回来时间太长O(log无穷大)，题目要求的是log(k)，k是target在数组中的位置。寻找的方法是很经典很重要的double 的方法（与动态数组dynamic array or array list的实现原理一样）：先从位置1开始，判断如果小于nums[k]，就判断位置2，如果还小于，再判断位置4，再判断位置8，再判断位置16，32，64，2**m次方，直到到了某个位置p满足,nums[p]>=nums[k]，这时候p的位置一定落在k到2k之间，而不会是无穷大的位置了。"""
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if target < reader.get(0):
            return -1
        if target == reader.get(0):
            return 0
        # find the end point
        end = 1
        while reader.get(end) < target:
            end *= 2
        start = end // 2  # since end is in [k,2k], then start doesn't need to start from 0
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= reader.get(mid):   # 带等于号，说明往左逼
                end = mid
            else:
                start = mid
        if reader.get(end) == target:
            return end
        if reader.get(start) == target: 
            return start
        return -1
