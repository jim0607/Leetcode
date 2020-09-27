"""
1306. Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""

"""
simple dfs
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(curr_idx):
            if arr[curr_idx] == 0:
                return True
            
            for next_idx in [curr_idx - arr[curr_idx], curr_idx + arr[curr_idx]]:
                if 0 <= next_idx < len(arr):
                    if next_idx not in visited:
                        visited.add(next_idx)
                        if dfs(next_idx):
                            return True
            return False
        
            
        visited = set()
        visited.add(start)
        return dfs(start)
 
 
"""
simple bfs
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        while len(q) > 0:
            curr_idx = q.popleft()
            if arr[curr_idx] == 0:
                return True
            for next_idx in [curr_idx + arr[curr_idx], curr_idx - arr[curr_idx]]:
                if 0 <= next_idx < len(arr):
                    if next_idx not in visited:
                        q.append(next_idx)
                        visited.add(next_idx)
        return False
