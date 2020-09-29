# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def _go_back(self, robot):      # make robot to face at the correct direction
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
    def cleanRoom(self, robot):
        def backtrack(curr_i, curr_j, facing):
            visited.add((curr_i, curr_j))
            robot.clean()               # 注意每visit一个点就让robot打扫一下
            
            for _ in range(4):          # this is for next_candidates in next_moves
                facing = (facing + 1) % 4     
                robot.turnRight()       # 注意别忘了调整机器人的朝向
                   
                next_i, next_j = curr_i + directions[facing][0], curr_j + directions[facing][1]
                if (next_i, next_j) not in visited and robot.move():
                    backtrack(next_i, next_j, facing)
                    self._go_back(robot)
        
        # (1, 0) 代表facing up, (0, 1)代表facing right，(-1, 0)代表facing down, (0, -1)达标facing left 
        # 注意顺序不能变
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        backtrack(0, 0, 0)
