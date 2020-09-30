"""
497. Random Point in Non-overlapping Rectangles

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily 
picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. 
Arguments are always wrapped with a list, even if there aren't any.
"""


"""
Similar with random pick with weight, here we use number of points in the rectangle as weight.
Firslty, create a weight list w, where w[i] is the number of points in the rectangle. 
Secondly, use a prefix_sum list to store the prefix_sum of the weight list.
Then generate a rand_int and use binary search to find which rectangle the rand_int belongs to. 
"""
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        
        weights = []            # w[i] is the number of points in the rect, not area of the rect
        for x1, y1, x2, y2 in rects:
            weights.append((x2 - x1 + 1) * (y2 - y1 + 1))
        
        self.pre_sum = [0 for _ in range(len(weights) + 1)]
        for i in range(len(weights)):
            self.pre_sum[i+1] = self.pre_sum[i] + weights[i]

    def pick(self) -> List[int]:
        rand_num = random.randrange(self.pre_sum[-1])
        
        # binary search to find where the rand_num is in the self.pre_sum
        start, end = 0, len(self.pre_sum) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.pre_sum[mid] <= rand_num:        # 这里是往右逼近，在这里debug了一个半小时！！
                start = mid
            else:
                end = mid
        idx = start - 1 if self.pre_sum[start] > rand_num else end - 1   # 减一是因为pre_sum中的idx比rect中大一
        
        # idx represents which rect the rand_int belongs to
        # 到这一步了我们其实可以再call两次random function to generate a random number in range [x1, x2] and another one in [y1, y2]
        # 但实际上我们在生成了一个随机数rand_int之后，确定了矩形rect_chosen，我们根据rand_int，如果把rect_chosen看成是一个2D array，
        # 只需要在rect_chosen中找第rand_int - (prefix_sum[i] - area)个点就可以，area是rect[i]的整数点的数量。这样我们就可以只call一次rand()
        # This strategy is useful when calls to the random number generator are expensive.
        # 下面的其实就是用数学方法找到rand_int所在的那个矩形的位置坐标了
        x1, y1, x2, y2 = self.rects[idx]        
        m, n = y2 - y1 + 1, x2 - x1 + 1
        offset = self.pre_sum[start] - rand_num if self.pre_sum[start] > rand_num else self.pre_sum[end] - rand_num
        offset = m * n - offset
        x = x1 + offset % n
        y = y1 + offset // n
        return [x, y]
