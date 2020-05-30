1263. Minimum Moves to Move a Box to Their Target Location

Storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by a grid of size m x n, where each element is a wall, floor, or a box.

Your task is move the box 'B' to the target position 'T' under the following rules:

Player is represented by character 'S' and can move up, down, left, right in the grid if it is a floor (empy cell).
Floor is represented by character '.' that means free cell to walk.
Wall is represented by character '#' that means obstacle  (impossible to walk there). 
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:



Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.
Example 4:

Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 20
1 <= n <= 20
grid contains only characters '.', '#',  'S' , 'T', or 'B'.
There is only one character 'S', 'B' and 'T' in the grid.







"""
思路：这个题是从源节点到目标节点的最短路径问题，所以想到用bfs, 源节点是对boxPos, 目标节点是targetPos, 从源节点出发做带层序遍历的bfs_1, return 层数即可。
注意在判断nextBoxPos是否可以append到q的时候需要兼顾考虑到player能不能到nextBoxPos的相反方向去推box, 
所以需要找到从currPlayerPos到oppositeNextBoxPos的可能路径，这是一个从源节点到目标节点的问题，源节点是对currPlayerPos, 目标节点是oppositeNextBoxPos, 需要做bfs_2, 如果能到就返回true. 
总体思路就是上述了，需要注意的是bfs_1中由于box每移动一下boxPos会变playerPos也会变，所以要把boxPos和playerPos都入队列。
另外易错点：visited里面只装boxPos. 这是不对的, 因为box从不同的方向被推到同一个地方是允许的，因此visited里面应该装入(boxPos, the pos where the boxPos comes from)
"""

class Solution:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def minPushBox(self, grid: List[List[str]]) -> int:
        # step 1: find the playerPos, boxPos, and TargetPos
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "S": playerPos = (i, j)
                if grid[i][j] == "B": boxPos = (i, j)
                if grid[i][j] == "T": targetPos = (i, j)
        
        # step 2: level order bfs to find the shortest steps from boxPos to targetPos
        q = collections.deque()
        visited = set()
        q.append((boxPos, playerPos))   # 把boxPos和playerPos都入队列，因为由于box每移动一下boxPos会变playerPos也会变
        # visited.add(boxPos)       # 易错点：visited里面只装boxPos. 这是不对的, 因为box从不同的方向被推到同一个地方是允许的，因此visited里面应该装入(boxPos, the pos where the boxPos comes from)
        steps = -1
        while q:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                currBoxPos, currPlayerPos = q.popleft()
                if currBoxPos == targetPos:
                    return steps
                
                for move in self.MOVES:
                    nextBoxPos_x, nextBoxPos_y = currBoxPos[0] + move[0], currBoxPos[1] + move[1]
                    oppositeNextBoxPos_x, oppositeNextBoxPos_y = currBoxPos[0] - move[0], currBoxPos[1] - move[1]
                    nextBoxPos = (nextBoxPos_x, nextBoxPos_y)
                    oppositeNextBoxPos = (oppositeNextBoxPos_x, oppositeNextBoxPos_y)
                    if nextBoxPos_x < 0 or nextBoxPos_x >= m or nextBoxPos_y < 0 or nextBoxPos_y >= n:
                        continue
                    if grid[nextBoxPos_x][nextBoxPos_y] == "#":
                        continue
                    if (nextBoxPos, currBoxPos) in visited:
                        continue
                    if not self.playerCanReach(grid, currPlayerPos, oppositeNextBoxPos, currBoxPos):
                        continue
                    q.append((nextBoxPos, currBoxPos))   # box move to the nextBoxPos, while player move to currBoxPos
                    visited.add((nextBoxPos, currBoxPos))   # visited里面应该装入(boxPos, the pos where the boxPos comes from)
                    
        return -1
                    
    def playerCanReach(self, grid, startPos, endPos, boxPos):
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        q.append(startPos)
        visited.add(startPos)
        while q:
            currPos = q.popleft()
            if currPos == endPos:
                return True
            for move in self.MOVES:
                nextPos_x, nextPos_y = currPos[0] + move[0], currPos[1] + move[1]
                nextPos = (nextPos_x, nextPos_y)
                if nextPos_x < 0 or nextPos_x >= m or nextPos_y < 0 or nextPos_y >= n:
                    continue
                if grid[nextPos_x][nextPos_y] == "#" or nextPos == boxPos:      # 易错点2: 遇到box的话也不能前进
                    continue
                if nextPos in visited:
                    continue
                q.append(nextPos)
                visited.add(nextPos)
                
        return False
