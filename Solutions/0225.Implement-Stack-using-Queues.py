#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (42.39%)
# Likes:    468
# Dislikes: 504
# Total Accepted:    156.4K
# Total Submissions: 369K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a stack using queues.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# 
# 
# Example:
# 
# 
# MyStack stack = new MyStack();
# 
# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
# 
# 
#

"""
use q1 to represent stack, use q2 to helpe pop from right
"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # first move all elements from q1 to q2, then append x to q1, then move back
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.q1) == 0:
            raise IndexError("The stack is empty")
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q1) == 0:
            raise IndexError("The stack is empty")
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
