"""
1240. Tiling a Rectangle with the Fewest Squares

Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

Example 1:

Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:

Input: n = 5, m = 8
Output: 5
Example 3:

Input: n = 11, m = 13
Output: 6
"""



"""
The basic idea is to fill the entire block bottom up. 
In every step, find the lowest unfilled square first, and select a square with different possible sizes to fill it. 
What is the nodes in the graph? It is a height array (skyline) height_arr!!!!! 
The start_node is height_arr = [0, 0, 0...], the end_node is height_arr = [m, m, m...].
Pruning:
1. When the current cnt has exceeded the value of the current global optimal solution, then no need to move forward.
2. Try largest square possible first (improves time by a lot).
"""
class Solution:
    def tilingRectangle(self, m: int, n: int) -> int:
        def backtrack(curr_height, curr_cnt):
            if all(h == m for h in curr_height):
                self.min_cnt = min(self.min_cnt, curr_cnt)
                return
            
            if curr_cnt >= self.min_cnt:    # pruning 1
                return
            
            # 套模板is to find next candidate. what is the next candidate? It's the lowest unfilled area
            # below is to find the lowest unfilled area
            min_h = min(curr_height)
            left_idx = curr_height.index(min_h)     # the left idx of the min_h
            right_idx = left_idx                    
            while right_idx + 1 < n and curr_height[right_idx+1] == min_h:  # get the right_idx of the min_h
                right_idx += 1
            width = right_idx - left_idx + 1     # now we have found the width and height of the lowest unfilled area,
            height = m - min_h                   # we need to put our next square into the area
            
            for side_lens in range(min(width, height), 0, -1):   # 注意我们需要遍历所有可能的side_lens for the square. 逆序遍历is pruning 2
                next_height = [h for h in curr_height]      # 注意has to be a deep copy. Otherwise curr_height will be changed
                for lens in range(side_lens):
                    next_height[left_idx + lens] += side_lens
                backtrack(next_height, curr_cnt + 1)            
            
        
        self.min_cnt = m * n
        backtrack([0 for _ in range(n)], 0)
        return self.min_cnt
