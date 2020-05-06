"""https://coordinate.wang/index.php/archives/2129/"""
"""why time complexity is O(N):
This is using an increasing monotone stack. Every index is pushed and popped once, and processed once.
each height will be only popped one time!! so the maximum teim complexity is O(2N)"""

"""
非单调栈算法：从左向右遍历数组，然后每遍历到一个高度h，向左边找第一个比自己小的的高度在位置i，向右边找第一个比自己小的的高度在位置j，
那此时的面积就是h*(j-i). 这个算法需要向左向右找第一个比自己小的元素，这类问题就要想到用monostack
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # save index in the monoStack, as height may have the same value
        # based on the heights, maintain an increasing stack (相等也可以)
        monoStack = [-1]        # 最左边放一个dummy height
        heights.append(-1)
        res = 0
        
        for idx, val in enumerate(heights):
            while heights[monoStack[-1]] > val:
                height = heights[monoStack.pop()]
                res = max(res, height * (idx - monoStack[-1] - 1))
                
            monoStack.append(idx)
        
        return res
    
    
class Solution {
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length == 0) return 0;
            
        Stack<Integer> monoStack = new Stack<Integer>();    // 维护单调递增
        int maxArea = 0;
        
        """注意heights.add(-1) 是不行的，在java中arr的size是不能改变的。"""
        for (int i = 0; i <= heights.length; i++) {
            int height = (i == heights.length) ? -1 : heights[i];
            while (!monoStack.isEmpty() && heights[monoStack.peek()] >= height) { //如果栈顶高度大于当前高度
                int h = heights[monoStack.pop()];       //保存栈顶元素信息
                int w = monoStack.isEmpty() ? i : i - monoStack.peek() - 1;   //如果栈已经为空，宽度为i，否则i-s.top()-1
                maxArea = Math.max(maxArea, h * w);
            }
            
            monoStack.push(i);  //如果栈顶高度小于当前高度, then push into stack
        }
        
        return maxArea;
    }
}
