"""
1515. Best Position for a Service Centre

A delivery company wants to build a new service centre in a new city. 
The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position 
such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, 
return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:

Answers within 10^-5 of the actual value will be accepted.

Example 1:

Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, 
the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:

Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
Example 3:

Input: positions = [[1,1]]
Output: 0.00000
Example 4:

Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, 
but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
Example 5:

Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
 
Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100
"""



"""
gradient descent
"""
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        prediction = [0, 0]
        alpha = 1
        eps = 1e-9
        while alpha > eps:
            gradient = self.calculate_gradient(prediction, positions)
            prediction[0] -= alpha * gradient[0]
            prediction[1] -= alpha * gradient[1]
            alpha *= 0.996
        return self.cost_func(prediction, positions)            
            
    def cost_func(self, pos, positions):       # the cost_func is actually defined as distance
        cost = 0
        for position in positions:
            cost += sqrt((pos[0] - position[0])**2 + (pos[1] - position[1])**2)
        return cost
            
    def calculate_gradient(self, prediction, positions):
        """
        gradient = d(cost_func)/dx
        """
        gradient = [0, 0]
        cost = self.cost_func(prediction, positions)
        for x, y in positions:
            dx = prediction[0] - x
            dy = prediction[1] - y
            r = sqrt(dx**2 + dy**2)
            gradient[0] += (prediction[0] - x) / (r + 1e-9)      # 加上1e-9是为了防止divide by zero
            gradient[1] += (prediction[1] - y) / (r + 1e-9)      
        return gradient
        
        
"""
上面的naive gradient descent takes 6000ms. Below 我们对learning rate做优化 - takes olny 200ms
"""
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        prediction = [0, 0]
        alpha = 1
        eps = 1e-9
        while alpha > eps:
            gradient = self.calculate_gradient(prediction, positions)
            new_x = prediction[0] - alpha * gradient[0] 
            new_y = prediction[1] - alpha * gradient[1] 
            if self.cost_func([new_x, new_y], positions) < self.cost_func(prediction, positions):   # 如果新的位置离minimum更近了，
                prediction = [new_x, new_y]       # 那就说明在往正确的方向走，我们就更新prediction的位置为新的位置，且保持step不变，依然大步往前走
            else:       # 如果新的位置离minimum更远了，那说明已经滑过minimum point且开始发散了，我们就不更新prediction的位置，而是将step变小一些重新再算一次
                alpha *= 0.1
        return self.cost_func(prediction, positions)            
            
    def cost_func(self, pos, positions):       # the cost_func is actually defined as distance
        cost = 0
        for position in positions:
            cost += sqrt((pos[0] - position[0])**2 + (pos[1] - position[1])**2)
        return cost
            
    def calculate_gradient(self, prediction, positions):
        """
        gradient = d(cost_func)/dx
        """
        gradient = [0, 0]
        cost = self.cost_func(prediction, positions)
        for x, y in positions:
            dx = prediction[0] - x
            dy = prediction[1] - y
            r = sqrt(dx**2 + dy**2)
            gradient[0] += (prediction[0] - x) / (r + 1e-9)      # 加上1e-9是为了防止divide by zero
            gradient[1] += (prediction[1] - y) / (r + 1e-9)      
        return gradient
