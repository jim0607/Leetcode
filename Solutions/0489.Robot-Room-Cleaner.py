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
    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()    
    
    def cleanRoom(self, robot):
        # (1, 0) 代表facing up, (0, 1)代表facing right，(-1, 0)代表facing down, (0, -1)达标facing left 
        # 注意顺序不能变
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.visited = set()
        self.backtrack(robot, 0, 0, 0)
        
    def backtrack(self, robot, x, y, facing):
        """
        backtrack so that the robot can visit every possible spot in the room
        """
        self.visited.add((x, y))
        robot.clean()
        
        for _ in range(4):
            facing = (facing + 1) % 4
            robot.turnRight()
            
            next_x, next_y = x + self.directions[facing][0], y + self.directions[facing][1]

            if (next_x, next_y) not in self.visited and robot.move():
                self.backtrack(robot, next_x, next_y, facing)
                self.goBack(robot)
