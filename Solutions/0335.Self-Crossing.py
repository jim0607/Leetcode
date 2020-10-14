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
