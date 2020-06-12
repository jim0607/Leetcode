874. Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)



"""
[4 -1 3]
[4, 0]
facing right
[4 3]

[4 -1 4 -2 4], [[4, 2]]
[4 0] - [4 0]
facing right
[1 4]
facing up
[1, 8]
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # (1, 0) 代表facing up, (0, 1)代表facing right，(-1, 0)代表facing down, (0, -1)达标facing left 
        # 注意顺序不能变
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  
        
        obstacleSet = set()
        for obstacle in obstacles:
            obstacleSet.add((obstacle[1], obstacle[0]))     # 实在看不惯题目用坐标轴表示方位，强行改成用行列坐标表示方位
        
        currPos = [0, 0]
        facing = 0    # 初始位置directions[0] - 代表facing up
        res = 0
        
        for cmd in commands:
            if cmd == -2:
                facing = (facing - 1) % 4   # 注意这里要取mod，这是机器人问题常用的手法
            elif cmd == -1:
                facing = (facing + 1) % 4
            else:
                for step in range(cmd):     # check在cmd的步数内有没有obstacle
                    # 如果发现前面有obstacle, 就直接停在currPos不要往前走
                    if (currPos[0] + directions[facing][0], currPos[1] + directions[facing][1]) in obstacleSet:    
                        break
                    currPos[0] += directions[facing][0]
                    currPos[1] += directions[facing][1]
                    res = max(res, currPos[0]**2 + currPos[1]**2)
                        
        return res
