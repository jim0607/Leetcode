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
        heights = [0 for _ in range(n)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
                    
            res = max(res, self.largestRectangularHistogram(heights))
            
        return res
      
      
      
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0 for _ in range(n)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                heights[j] = 0 if matrix[i][j] == "0" else heights[j] + 1
            
            max_area = max(max_area, self.max_area(heights))
            
        return max_area
    
    def max_area(self, heights):
        n = len(heights)
        left_idx = [-1 for _ in range(n)]
        st = []     # store (h, idx)
        for i, h in enumerate(heights): 
            while len(st) > 0 and st[-1][0] >= h:
                st.pop()
            
            if len(st) > 0:
                left_idx[i] = st[-1][1]
            
            st.append((h, i))
            
        right_idx = [n for _ in range(n)]
        st = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while len(st) > 0 and st[-1][0] >= h:
                st.pop()
                
            if len(st) > 0:
                right_idx[i] = st[-1][1]
                
            st.append((h, i))
            
        max_area = 0
        for i, h in enumerate(heights):
            area = h * (right_idx[i] - left_idx[i] - 1)
            max_area = max(max_area, area)
        return max_area
