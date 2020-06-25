478. Generate Random Point in a Circle

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.


import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        
        # **** 注意要取平方根 **** 这是因为random.randrange()取的点在线性范围内是uniform的，但是在2D圆内不是
        # 想想在一个圆内，是不是在半径更大的位置分布的点比半径非常小的位置分布的点要多
        rand_radius = math.sqrt(random.randrange(0, 2**31 + 1) / 2**31) * self.radius  
        
        rand_angle = random.randrange(0, 360)
        rand_angle = rand_angle / 180 * math.pi
        
        rand_x = rand_radius * math.cos(rand_angle) + self.x_center
        rand_y = rand_radius * math.sin(rand_angle) + self.y_center
        
        return [rand_x, rand_y]



"""
solution 2: rejection sampling - O(1) need to call random multiple times
"""
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x * x + y * y <= 1:
                return [x * self.radius + self.x_center, y * self.radius + self.y_center]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
