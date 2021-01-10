"""
1642. Furthest Building You Can Reach

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
"""


"""
backtrack结束条件: 没有building给你跳了: if curr_idx == len(heights) - 1, 或者没有足够的bricks and ladders: if bricks_left == 0 and ladders_left == 0
constraints for next_candidate: next_idx = curr_idx + 1, if heights[next_idx] > heights[curr_idx], we use bricks or ladder; if heights[next_idx] <= heights[curr_idx], we don't use anything
arguments pass into backtrack function: curr_idx, bricks_left, ladders_left
O(N*2^(B+L)), where N is how many buildings, B is how many bricks, L is how many ladders
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def backtrack(curr_idx, bricks_left, ladders_left):
            if curr_idx == len(heights) - 1:
                self.max_cnt = len(heights) - 1
                return
            
            if bricks_left < heights[curr_idx + 1] - heights[curr_idx] and ladders_left == 0:
                self.max_cnt = max(self.max_cnt, curr_idx)
                return

            if heights[curr_idx + 1] <= heights[curr_idx]:
                backtrack(curr_idx + 1, bricks_left, ladders_left)
            else:
                if bricks_left >= heights[curr_idx + 1] - heights[curr_idx]:
                    backtrack(curr_idx + 1, bricks_left - (heights[curr_idx + 1] - heights[curr_idx]), ladders_left)
                if ladders_left > 0:
                    backtrack(curr_idx + 1, bricks_left, ladders_left - 1)
                    
        
        self.max_cnt = 0
        backtrack(0, bricks, ladders)
        return self.max_cnt
        
        
"""
recursion + memorization: O(NBL)
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def backtrack(curr_idx, bricks_left, ladders_left):
            if curr_idx == len(heights) - 1:
                return 0
            
            if bricks_left < heights[curr_idx + 1] - heights[curr_idx] and ladders_left == 0:
                return 0
            
            if (curr_idx, bricks_left, ladders_left) in memo:
                return memo[(curr_idx, bricks_left, ladders_left)]

            res = 0
            if heights[curr_idx + 1] <= heights[curr_idx]:
                res = max(res, 1 + backtrack(curr_idx + 1, bricks_left, ladders_left))
            else:
                if bricks_left >= heights[curr_idx + 1] - heights[curr_idx]:
                    res = max(res, 1 + backtrack(curr_idx + 1, bricks_left - (heights[curr_idx + 1] - heights[curr_idx]), ladders_left))
                if ladders_left > 0:
                    res = max(res, 1 + backtrack(curr_idx + 1, bricks_left, ladders_left - 1))
                    
            memo[(curr_idx, bricks_left, ladders_left)] = res
            return res
                    
        
        memo = defaultdict(int)     # (curr_idx, curr_bricks_left, ladders_left) --> from (curr_idx, curr_bricks_left, ladders_left), how many more buildings we can get
        return backtrack(0, bricks, ladders)
