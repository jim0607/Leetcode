"""https://coordinate.wang/index.php/archives/2129/"""
"""why time complexity is O(N):
This is using an increasing monotone stack. Every index is pushed and popped once, and processed once.
each height will be only popped one time!!"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # save index in the monoStack, as height may have the same value
        # based on the heights, maintain an increasing stack (相等也可以)
        monoStack = [-1]    
        heights.append(-1)
        res = 0
        
        for idx, val in enumerate(heights):
            while heights[monoStack[-1]] > val:
                height = heights[monoStack.pop()]
                res = max(res, height * (idx - monoStack[-1] - 1))
                
            monoStack.append(idx)
        
        return res
