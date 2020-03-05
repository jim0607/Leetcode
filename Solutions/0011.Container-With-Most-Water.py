Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. 
This way we are compromising on the width but we are looking forward to a longer length container."""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lens = len(height)
        maxArea = min(height[0], height[lens - 1]) * (lens - 1)
        
        i, j = 0, lens - 1
        while i < j:
            if height[i] > height[j]:   # meaning that 右边的栅栏更低，所以把右边指针移动一下，希望能用长度去compromise宽度，即寄希望于min(height[i], height[j])会变大，来compromise掉(j - i)的变小
                j -= 1                  # 为什么不移左边指针呢？因为移动左边的话，min(height[i], height[j])不会变大，但是(j - i)一定变小，所以面积一定变小
                
            else:
                i += 1
            
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        
        return maxArea        
