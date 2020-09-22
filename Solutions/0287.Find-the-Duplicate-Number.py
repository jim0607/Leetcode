"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


"""
可以把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。
那么如果存在重复的num，那就表示有两个不同node都指向了同一个node，也就是成环的地点。这么想这个题目就和142一样了
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # step 1: 快慢指针找到相遇的点
        slowNum, fastNum = 0, 0
        while True:
            slowNum = nums[slowNum]
            fastNum = nums[nums[fastNum]]
            if slowNum == fastNum:
                break
            
        # step 2: 重新定义两个指针p1, p2分别从head和上面相遇的点出发，p1, p2相遇的点就是环的入口
        currNum = 0
        while True:
            currNum = nums[currNum]
            slowNum = nums[slowNum]
            if currNum == slowNum:
                return currNum
