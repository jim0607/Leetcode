"""
335. Self Crossing

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, 
then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. 
In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false 
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true 
"""

"""
这道题给了我们一个一位数组，每个数字是个移动量，按照上左下右的顺序来前进每一个位移量，
问我们会不会和之前的轨迹相交，而且限定了常量的空间复杂度，我立马想到了贪吃蛇游戏，但是这条蛇不会自动向前移动哈。
言归正传，参考的网上大神们的解法，实际上相交的情况只有以下三种情况：

     x(1)
    ┌───┐
x(2)│   │x(0)
    └───┼──>
    x(3)│
        
第一类是第四条边和第一条边相交的情况，需要满足的条件是第一条边大于等于第三条边，第四条边大于等于第二条边。
同样适用于第五条边和第二条边相交，第六条边和第三条边相交等等，依次向后类推的情况...

      x(1)
    ┌──────┐
    │      │x(0)
x(2)│      ^
    │      │x(4)
    └──────│
      x(3)

第二类是第五条边和第一条边重合相交的情况，需要满足的条件是第二条边和第四条边相等，
第五条边大于等于第三条边和第一条边的差值，同样适用于第六条边和第二条边重合相交的情况等等依次向后类推...

      x(1)
    ┌──────┐
    │      │x(0)
x(2)│     <│────│
    │       x(5)│x(4)
    └───────────│
        x(3)

第三类是第六条边和第一条边相交的情况，需要满足的条件是第四条边大于等于第二条边，
第三条边大于等于第五条边，第五条边大于等于第三条边和第一条边的差值，第六条边大于等于第四条边和第二条边的差值，
同样适用于第七条边和第二条边相交的情况等等依次向后类推
"""


"""
              Case 1                  Case 2                  Case 2
                b                       b                       b
       +----------------+      +----------------+      +----------------+
       |                |      |                |      |                |
       |                |      |                |      |                |
     c |                | a  c |                | a  c |                | a
       |                |      |                |      |                |    f
       +--------------->|      |                |      |                | <----+
                d       |      |                ^ e    |                |      | e
                               |                |      |                       |
                               +----------------+      +-----------------------+
                                        d                       d
"""
class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        a = b = c = d = e = f = 0
        for x in arr:
            f, e, d, c, b, a = e, d, c, b, a, x      
            if d > 0 and c <= a and d >= b:        
                return True
            if e > 0 and c > a and d == b and e >= c - a:
                return True
            if f > 0 and c > a and d > b and c - a <= e <= c and f >= d - b:
                return True
        return False
