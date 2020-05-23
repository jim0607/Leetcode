Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


"""山景城一姐de讲解：首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，
因为水会从左边溜走，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作
O(N), O(1)"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # step 1: find the highestBarPos
        highestBar = 0
        highestBarPos = 0
        for i, bar in enumerate(height):
            if bar > highestBar:
                highestBarPos = i
                highestBar = bar
                
        # step 2: scan the left part
        water = 0
        leftHighest = 0
        for i in range(highestBarPos):
            if height[i] > leftHighest:
                leftHighest = height[i]
            else:
                water += leftHighest - height[i]
                
        # step 3: scan the right part
        rightHighest = 0
        for i in range(len(height) - 1, highestBarPos, -1):
            if height[i] > rightHighest:
                rightHighest = height[i]
            else:
                water += rightHighest - height[i]
                
        return water

    
    
    
使用九章算法班中讲过的相向型双指针算法。跟山景城一姐一个意思，稍微好一点。
整个算法的思想是计算每个位置上可以盛放的水，累加起来。

记录如下几个值：

left, right => 左右指针的位置
left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height
每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。
与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：

一种是 left_max > heights[left]，这种情况下，水可以盛放 left_max - heights[left] 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。
一种是 left_max <= heights[left]，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]
left_max >= right_max 的情况类似处理。

时间复杂度：O(n)，空间复杂度 O(1)  
    
class Solution:
    def trap(self, height: List[int]) -> int:
        lens = len(height)
        if lens <= 2:
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0
        while left <= right:    # 注意是小于等于
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
                
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1
                
        return water
