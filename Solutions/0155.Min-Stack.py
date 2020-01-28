155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []  # use a stack to store minVal 
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
        # push一个元素进stack之后，要判断这个元素是不是<=最小的元素，如果是，那就append进去
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        
        popItem = self.stack.pop()
        
        # pop出一个元素之后，要判断这个元素是不是最小的元素，如果是，那就要在minStack中pop出这个元素
        if popItem == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        
        return self.minStack[-1]
            
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
