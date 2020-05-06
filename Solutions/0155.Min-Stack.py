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


"""
2 5 4

2 
2 5 
2 4 5     2  4

st, minSt
st     2   2 5      2 5     2 5 4
minSt  2            2        2

"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.minSt = []

    def push(self, x: int) -> None:
        self.st.append(x)
        
        # push一个元素进stack之后，要判断这个元素是不是<=最小的元素，如果是，那就append进去
        if len(self.minSt) == 0 or x <= self.minSt[-1]:
            self.minSt.append(x)

    def pop(self) -> None:
        if len(self.st) == 0:
            raise IndexError("The stack is empty")
        else:
            poppedItem = self.st.pop()
            
            # pop出一个元素之后，要判断这个元素是不是最小的元素，如果是，那就要在minStack中pop出这个元素
            if poppedItem == self.minSt[-1]:
                self.minSt.pop()
                
            return poppedItem

    def top(self) -> int:
        if len(self.st) == 0:
            raise IndexError("The stack is empty")
        else:
            return self.st[-1]

    def getMin(self) -> int:
        if len(self.st) == 0:
            raise IndexError("The stack is empty")
        else:
            return self.minSt[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
