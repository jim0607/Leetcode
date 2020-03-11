Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6


"""https://yq.aliyun.com/articles/3496
step 1: construct a heights list for each row
step 2: calculate the largestRectangularHistogram of each height using the same method in 84
O(MN), O(M)"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0 for col in range(n)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
                    
            res = max(res, self.largestRectangularHistogram(heights))
            
        return res
    
    def largestRectangularHistogram(self, heights):
        monoStack = [-1]
        heights.append(-1)
        res = 0
        
        for idx, val in enumerate(heights):
            while heights[monoStack[-1]] > val:
                height = heights[monoStack.pop()]
                res = max(res, height * (idx - monoStack[-1] - 1))
                
            monoStack.append(idx)
            
        return res
