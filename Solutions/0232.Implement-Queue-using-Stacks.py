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

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackA = []        # a main stack
        self.stackB = []        # a backup stack for reversal
        
    # 用一个辅助stack，每次push进一个数的时候都保证把这个数push到栈的最下面，这样就可以保证它最后出来了。
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # put all element in A to B
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        # put x in A
        self.stackA.append(x)
        # put all element back from B to A
        while self.stackB:
            self.stackA.append(self.stackB.pop())    

        # now the last in element x is at the bottom of stackA    

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stackA:
            return self.stackA.pop()
        else:
            raise IndexError("queue is empty")

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stackA:
            return self.stackA[-1]
        else:
            raise IndexError("queue is empty")
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stackA


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

