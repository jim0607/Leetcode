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
        # going clockwise from 0 deg to 270 deg
        self.facing_directions = {
            0: (-1, 0), 
            90: (0, 1), 
            180: (1, 0), 
            270: (0, -1) }

        self.visited = set()
        self.backtrack(robot, 0, 0, 0)
        
    def backtrack(self, robot, x, y, facing_dir):
        self.visited.add((x, y))
        robot.clean()
        
        for i in range(4):  # 这里的for i in range(4)其实就相当于是for going up, right, down, left
            new_facing_dir = (facing_dir + i * 90) % 360  # 这一部分是调整机器人朝向之后对应的下一步是什么？
            next_x, next_y = x + self.facing_directions[new_facing_dir][0], y + self.facing_directions[new_facing_dir][1]

            if (next_x, next_y) not in self.visited and robot.move():
                self.backtrack(robot, next_x, next_y, new_facing_dir)
                self.goBack(robot)

            robot.turnRight()     # 这一步就是调整机器人的朝向，这样他才能换一个方向走。
