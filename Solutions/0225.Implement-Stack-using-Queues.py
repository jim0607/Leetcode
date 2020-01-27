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

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qA = collections.deque()
        self.qB = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # STEP 1: move all items from A to B
        while self.qA:
            self.qB.append(self.qA.popleft())
        # STEP 2: append x
        self.qA.append(x)
        # STEP 3: move all items from B back to A
        while self.qB:
            self.qA.append(self.qB.popleft())        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.qA:
            return self.qA.popleft()
        else:
            raise IndexError("stack is empty")

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.qA:
            return self.qA[0]
        else:
            raise IndexError("stack is empty")

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.qA

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

