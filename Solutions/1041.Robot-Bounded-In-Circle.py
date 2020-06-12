1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...



class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        facing = 0
        currPos = [0, 0]
        for ch in instructions:
            if ch == "L":
                facing = (facing - 1) % 4
            elif ch == "R":
                facing = (facing + 1) % 4
            elif ch == "G":
                currPos[0] += directions[facing][0]
                currPos[1] += directions[facing][1]
                
        # The robot stays in the circle if (looking at the final vector) 
        # it changes direction (ie. doesn't stay pointing north), or it moves 0
        if facing != 0 or currPos == [0, 0]:
            return True
        
        return False
