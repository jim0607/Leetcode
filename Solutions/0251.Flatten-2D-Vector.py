#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (44.94%)
# Likes:    318
# Dislikes: 168
# Total Accepted:    69K
# Total Submissions: 153.5K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n[[[[1,2],[3],[4]]],[null],[null],[null],[null],[null],[null],[null]]'
#
# Design and implement an iterator to flatten a 2d vector. It should support
# the following operations: next and hasNext.
# 
# 
# 
# Example:
# 
# 
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Notes:
# 
# 
# Please remember to RESET your class variables declared in Vector2D, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# You may assume that next() call will always be valid, that is, there will be
# at least a next element in the 2d vector when next() is called.
# 
# 
# 
# 
# Follow up:
# 
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
# 
#

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.row = 0
        self.col = 0
        self.v = v

    def next(self) -> int:
        if self.hasNext():
            res = self.v[self.row][self.col]
            self.col += 1
            return res

    def hasNext(self) -> bool:
        """
        1. skip all the empty rows; 
        2. return True if has next
        """
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):    # if self.col is not at the end of this row and this row is not empty
                return True
            self.row += 1       # elif self.col comes to the end of this row or this row is empty
            self.col = 0
            
        return False
    
    

"""Solution 2: using a queue"""

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.q = collections.deque()
        for lst in v:
            for num in lst:
                self.q.append(num)

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) != 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
