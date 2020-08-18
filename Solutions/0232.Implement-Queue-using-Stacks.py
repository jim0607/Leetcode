#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (46.63%)
# Likes:    785
# Dislikes: 129
# Total Accepted:    184.3K
# Total Submissions: 395.2K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# 
# 
# Example:
# 
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#

"""
use st1 to represent a queue, and st2 as a helper to help enable pop from left
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.st1:             # 把大象装冰箱分三步：1. move all items from st1 to st2
            self.st2.append(self.st1.pop())
        self.st1.append(x)          # 2. put x in st1
        while self.st2:             # 3. move all items back to st1
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.st1) == 0:      # 判断为空就用lens来判断，不要写if self.st1 不规范
            raise IndexError("The queue is empty")
        return self.st1.pop()
            
    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.st1) == 0:
            raise IndexError("The queue is empty")
        return self.st1[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.st1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
